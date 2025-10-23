"""Dekorator logujący czas wykonania funkcji z obsługą wyjątków."""

import logging
import time
from functools import wraps

logging.basicConfig(
    level=logging.DEBUG,
    filename="example.log",
    format="%(asctime)s %(levelname)s %(name)s | %(funcName)s | %(message)s",
)

logger = logging.getLogger(__name__)


def loguj(funkcja):
    """Dodaj logowanie czasu wykonania funkcji oraz obsługę wyjątków."""

    @wraps(funkcja)
    def opakowanie(*args, **kwargs):
        start = time.perf_counter()
        try:
            wynik = funkcja(*args, **kwargs)
            stop = time.perf_counter()
            elapsed = (stop - start) * 1000
            logger.info(f"{funkcja.__name__} wykonana w {elapsed:.4f} s")
        except Exception as e:

            stop = time.perf_counter()
            elapsed = (stop - start) * 1000

            logger.error(f"Błąd w {funkcja.__name__} po {elapsed:.4f} s:\n {e}", exc_info=True)
            raise

        return wynik

    return opakowanie


@loguj
def policz_sume(n: int):
    """Policz sumę zakresu liczb od 0 do n-1."""
    return sum(range(n))


@loguj
def policz_sume_z_bledem(n: int):
    """Wariant funkcji generujący błąd w połowie obliczeń."""
    suma = 0
    for i in range(n):
        if i == n // 2:
            raise ValueError(f"Nie mozna policzyc sume w punkcie {i}")
        suma += i
    return suma


if __name__ == "__main__":
    print(policz_sume(10))
    try:
        print(policz_sume_z_bledem(10))
    except ValueError:
        print("Obsłużono ValueError – szczegóły w pliku example.log.")
