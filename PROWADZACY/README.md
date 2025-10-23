# Materiały dla prowadzącego

Zebrane tu pliki mają wspierać prowadzenie zajęć – od notatników demonstracyjnych, przez przykładowe skrypty, po gotowe ćwiczenia z testami. Poniżej znajdziesz krótkie omówienie każdego zasobu.

## Przegląd katalogów i plików

### Notatniki

- `01_podstawy.ipynb`, `02_funkcje.ipynb`, `zasiegi_zmiennych.ipynb`, `OOP.ipynb`, `cwiczenie2.ipynb`, `Untitled.ipynb` – notatniki Jupyter z przykładami do omawiania na żywo. Warto sprawdzić przed zajęciami, czy wszystkie komórki wykonują się bez błędów.

### Krótkie przykłady

- `przyklad.py` – introspekcja przestrzeni nazw (`dir()`, `locals()`, `globals()`).
- `przyklad2.py` – demonstracja działania `global` i `nonlocal`.
- `dekorator_cache.py` – prosty dekorator cache’ujący wyniki funkcji na przykładzie ciągu Fibonacciego.
- `logowanie/przyklad.py` – przykład dekoratora dodającego logowanie czasu wykonania wraz z obsługą wyjątków i zapisem do pliku `logowanie/example.log`.

### Ćwiczenia

- `cwiczenie_kalkulator/` – pełne rozwiązanie kalkulatora tekstowego z testami `pytest`. Plik `README.md` zawiera treść zadania i wskazówki do omówienia ze studentami.
- `wprowadzenie_do_testow/` – moduł pokazujący różne style testowania (`pytest` oraz `unittest`) na prostej funkcji progowej.

### Dokumentacja pomocnicza

- `help.md` – krótkie wskazówki organizacyjne i checklista do przygotowania zajęć (uzupełnione w tym zadaniu).

## Wskazówki organizacyjne

1. Przed zajęciami przejdź przez notatniki i upewnij się, że środowisko ma wszystkie wymagane zależności.
2. W folderach z ćwiczeniami znajdziesz zarówno docelowy kod, jak i testy. Zachęcaj uczestników do uruchamiania testów po każdej zmianie.
3. Sekcje „Komentarze” w plikach kodu zawierają teraz krótkie wskazówki dydaktyczne – możesz na nie zwrócić uwagę podczas omawiania zagadnień.

Powodzenia w prowadzeniu warsztatów! Jeśli czegoś brakuje – dopisz uwagi w `help.md`, aby mieć je pod ręką.
