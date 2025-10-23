"""Demonstracja słów kluczowych `global` i `nonlocal`."""

a = 1


def foo():
    """Modyfikuj zmienne globalne i domknięte."""
    global a
    a = 10  # modyfikujemy zmienną globalną
    b = 20  # lokalne w foo, ale dostępne dla bar dzięki nonlocal

    def bar():
        """Zmieniamy zmienną z leżącej wyżej przestrzeni nazw."""
        nonlocal b
        b = 30

    print("Przed bar, b =", b)
    bar()
    print("Po bar,  b =", b)
    print("\nW funkcji foo (lokalne):", locals())
    print("W funkcji foo (globalne):", {k: type(v).__name__ for k, v in globals().items() if not k.startswith("__")})


if __name__ == "__main__":
    print("Poziom modułu (globalne):", {k: type(v).__name__ for k, v in globals().items() if not k.startswith("__")})
    foo()
    print("\nPo wywołaniu foo, globalne:", {k: type(v).__name__ for k, v in globals().items() if not k.startswith("__")})
