"""Prosty kalkulator konsolowy wykorzystywany podczas zajęć."""

from typing import Callable, Dict, Tuple


def add(a: int, b: int) -> int:
    """Zwróć sumę argumentów."""
    return a + b


def sub(a: int, b: int) -> int:
    """Zwróć różnicę argumentów."""
    return a - b


def mul(a: int, b: int) -> int:
    """Zwróć iloczyn argumentów."""
    return a * b


def div(a: int, b: int) -> float:
    """Zwróć iloraz argumentów."""
    return a / b


OPERATIONS: Dict[str, Callable[[int, int], float]] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def get_data() -> Tuple[str, int, int]:
    """Pobierz dane od użytkownika, walidując znak operacji."""
    operation = input("Podaj rodzaj operacji (+-/*): ")

    if operation not in OPERATIONS:
        raise ValueError("Podano niepoprawny operator!")

    a = int(input("Podaj pierwszy argument: "))
    b = int(input("Podaj drugi argument: "))
    return operation, a, b


def main() -> None:
    """Zbierz dane, wykonaj działanie i pokaż wynik."""
    operation, a, b = get_data()
    result = OPERATIONS[operation](a, b)
    print(f"Wynik operacji {a}{operation}{b} = {result}")


if __name__ == "__main__":
    main()

# Alias zachowujący kompatybilność ze starszymi materiałami i testami.
operations = OPERATIONS
