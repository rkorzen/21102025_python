import random
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Direction(Enum):
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @staticmethod
    def from_input(value: str) -> "Direction":
        mapping = {
            "w": Direction.UP,
            "s": Direction.DOWN,
            "a": Direction.LEFT,
            "d": Direction.RIGHT,
        }
        v = value.strip().lower()
        if v in mapping:
            return mapping[v]
        raise ValueError(f"Invalid direction: {value}. Choices are: w, a, s, d")


@dataclass(frozen=True)
class Position:
    """Represents a position on the board. (0, 0) is the boottom left corner."""
    x: int
    y: int

    def move(self, direction: Direction) -> "Position":
        dx, dy = direction.value
        return Position(self.x + dx, self.y + dy)

    def distance(self, other: "Position") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)


class Board:
    def __init__(self, width: int, height: int):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self.width = width
        self.height = height

    def is_valid(self, pos: Position) -> bool:
        return (
            0 <= pos.x < self.width
            and 0 <= pos.y < self.height
        )

    def random_position(self, exclude: Optional[Position] = None) -> Position:
        while True:
            pos_x = random.randint(0, self.width - 1)
            pos_y = random.randint(0, self.height - 1)
            pos = Position(pos_x, pos_y)
            if pos != exclude:
                return pos


class Player:
    """Represents a player in the game."""

    def __init__(self, poistion: Position):
        self.position = poistion
        self.moves = 0

    def caluclate_new_position(self, direction: Direction) -> Position:
        return self.position.move(direction)

    def move(self, board: Board, direction: Direction) -> bool:
        new_position = self.caluclate_new_position(direction)
        if not board.is_valid(new_position):
            raise ValueError("Invalid move. You can't move outside the board.")

        self.position = new_position
        self.moves += 1

class Treasure:
    """Represents a treasure on the board."""

    def __init__(self, position: Position):
        self.position = position
        self.found = False

    def is_at(self, position: Position) -> bool:
        return self.position == position

    def mark_as_found(self):
        self.found = True

class Game:
    def __init__(self, width: int, height: int, debug: bool = False):
        self.debug = debug
        self.board = Board(width, height)
        self.player = Player(self.board.random_position())
        self.treasure = Treasure(self.board.random_position(exclude=self.player.position))
        self.last_distance = self.player.position.distance(self.treasure.position)

    def state(self) -> dict:
        return {
            "width": self.board.width,
            "height": self.board.height,
            "player": self.player.position,
            "treasure": self.treasure.position,
            "treasure_found": self.treasure.found,
            "moves": self.player.moves,
        }

    def step(self, direction: Direction) -> dict:
        """Make move and return state information."""
        before = self.player.position
        self.player.move(self.board, direction)
        after = self.player.position

        if self.treasure.is_at(after):
            self.treasure.mark_as_found()
            msg = f"Gratulacje! Znalazles skarb po {self.player.moves} ruchach."
            return {"message": msg, "found": True}

        current_distance = after.distance(self.treasure.position)
        if current_distance < self.last_distance:
            msg = "Ciepło. Zbliżyłeś się do Skarbu"
        elif current_distance > self.last_distance:
            msg = "Zimno. Oddaliłeś sie od Skarbu"
        else:
            msg = "Bez zmian"

        self.last_distance = current_distance
        return {"message": msg, "found": False}

    def size(self) -> tuple[int, int]:
        return self.board.width, self.board.height

class GameView:
    """Abstract class for displaying the game state."""

    def display_board(self, state: dict, debug: bool = False) -> None:
        raise NotImplementedError

    def get_direction(self) -> Direction:
        raise NotImplementedError

    def show_info(self, message: str) -> None:
        raise NotImplementedError


class ConsoleView(GameView):
    def display_board(self, state: dict, debug: bool = False) -> None:
        width: int = state["width"]
        height: int = state["height"]
        player: Position = state["player"]
        treasure: Position = state["treasure"]
        # treasure_found: bool = state["treasure_found"]


        for y in reversed(range(height)):
            row = []
            for x in range(width):
                pos = Position(x, y)
                if pos == player:
                    row.append("P")
                elif pos == treasure and debug:
                    row.append("T")
                else:
                    row.append(".")
            print(" ".join(row))
        print()

    def get_direction(self) -> Direction:
        raw = input("Podaj kierunek [w a s d]: ").strip().lower()

        return Direction.from_input(raw)

    def show_info(self, message: str) -> None:
        print(message)


class GameController:
    def __init__(self, game: Game, view: GameView):
        self.game = game
        self.view = view

    def play(self):
        w, h = self.game.size()

        print("Plansza o wymiarach:", w, "x", h)
        print(f"Start: pozycja gracza: {self.game.player.position}")

        if self.game.debug:
            print(f"DEBUG: pozycja skarbu: {self.game.treasure.position}")


        while True:
            self.view.display_board(self.game.state(), self.game.debug)
            direction = self.view.get_direction()
            result = self.game.step(direction)

            if result["found"]:
                self.view.display_board(self.game.state(), self.game.debug)
                self.view.show_info(result["message"])
                break
            else:
                self.view.show_info(result["message"])
                self.view.show_info(f"Twoja pozycja: {self.game.player.position}")


if __name__ == "__main__":
    game = Game(10, 10, debug=True)
    view = ConsoleView()
    controller = GameController(game, view)
    controller.play()

