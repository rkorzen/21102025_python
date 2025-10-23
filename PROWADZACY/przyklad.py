"""Krótki przykład introspekcji przestrzeni nazw w Pythonie."""

a = 1

if __name__ == "__main__":
    print("Zakres dostępnych nazw:", dir())
    print("Zmienne lokalne modułu:", locals())
    print("Zmienne globalne modułu:", {k: type(v).__name__ for k, v in globals().items()})
