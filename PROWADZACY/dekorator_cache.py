"""Przykład prostego dekoratora cache'ującego wyniki funkcji."""


def cache(func):
    """Zapamiętaj wynik funkcji dla danego argumentu i zwróć go przy kolejnych wywołaniach."""
    result = {}

    def wrapper(n):
        if n in result:
            return result[n]
        r = func(n)
        result[n] = r
        return r

    return wrapper


@cache
def fibonacci(n: int) -> int:
    """Rekurencyjna implementacja ciągu Fibonacciego z pamięcią podręczną."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    values = [fibonacci(i) for i in range(10)]
    print("Pierwsze wartości Fibonacciego:", values)
