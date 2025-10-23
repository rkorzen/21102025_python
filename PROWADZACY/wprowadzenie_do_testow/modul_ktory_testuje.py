"""Moduł z prostą funkcją progową – materiał do ćwiczeń z testów."""


def funkcja(x: int) -> int:
    """Zwróć 1 dla wartości dodatnich, w przeciwnym razie 0.

    Przykłady:

    >>> funkcja(1)
    1
    >>> funkcja(0)
    0
    >>> funkcja(-1)
    0
    """
    if x > 0:
        return 1
    return 0


if __name__ == "__main__":
    print("Wykonujemy szybkie testy ręczne...")
    assert funkcja(1) == 1
    print(".", end="")
    assert funkcja(0) == 0
    print(".", end="")
    assert funkcja(-1) == 0
    print(". OK")
