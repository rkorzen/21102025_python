
def funkcja(x):
    """Funkcja progowa, zwraca 1 dla x większy od 0 i 0 w pozostalych przypadach

    np:
    >>> testowana_funkcja(1)
    1
    >>> testowana_funkcja(0)
    0
    >>> testowana_funkcja(-1)
    0

    """
    if x > 0:
        return 1
    else:
        return 0

# assert False
# print(__name__)
if __name__ == "__main__":
    print("Wykonujemy testy")
    assert testowana_funkcja(1) == 2
    print(".", end="")
    assert testowana_funkcja(0) == 0
    print(".", end="")
    assert testowana_funkcja(-1) == 0, "zla wartosc"
    print(".",)
    print("OK")


