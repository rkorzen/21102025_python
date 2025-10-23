## Checklist przed zajęciami

- [ ] Sprawdź, czy środowisko wirtualne jest aktywne i ma zainstalowane potrzebne pakiety (`pytest`, `jupyter`, `ipython`).
- [ ] Uruchom próbnie każdy z notatników (`01_podstawy.ipynb`, `02_funkcje.ipynb`, `OOP.ipynb` i pozostałe) – upewnij się, że wszystkie komórki wykonują się bez błędów.
- [ ] Przejrzyj skrypty demonstracyjne (`przyklad.py`, `przyklad2.py`, `dekorator_cache.py`, `logowanie/przyklad.py`) i przygotuj krótkie wprowadzenie do każdego tematu.
- [ ] W katalogu `cwiczenie_kalkulator/` przygotuj pokaz działania kalkulatora oraz uruchomienie testów `pytest -q`.
- [ ] W katalogu `wprowadzenie_do_testow/` uruchom zarówno `pytest`, jak i `python -m unittest` dla przykładowych testów.
- [ ] Zadbaj o czystość repozytorium: usuń pliki tymczasowe i sprawdź `git status` przed zajęciami.

## Przydatne polecenia

```bash
# Uruchomienie wszystkich testów w katalogu prowadzącego
pytest PROWADZACY

# Sprawdzenie notatnika w trybie tylko do odczytu (bez uruchamiania)
jupyter nbconvert --to html --execute 01_podstawy.ipynb
```

Dodawaj własne notatki poniżej, aby mieć je pod ręką.
