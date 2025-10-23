# Warsztaty Python

Material wspiera zajecia z Pythona w wariancie warsztatowym. W repozytorium znajdziesz zarowno pliki dla prowadzacego, jak i zestaw cwiczen dla uczestnikow.

## Plan dnia

- 09:00-10:30 praca warsztatowa  
- 10:30-10:45 przerwa kawowa  
- 10:45-12:15 praca warsztatowa  
- 12:15-13:15 przerwa obiadowa  
- 13:15-14:45 praca warsztatowa  
- 14:45-15:00 przerwa kawowa  
- 15:00-17:00 praca warsztatowa

## Struktura repozytorium

- `PROWADZACY/` - materialy dydaktyczne, przyklady, gotowe rozwiazania oraz testy (opis szczegolowy w `PROWADZACY/README.md`).  
- `STUDENT/` - notatniki i cwiczenia dla uczestnikow.  
- `README.md` (biezacy plik) - skrocona sciaga organizacyjna.

## Przygotowanie srodowiska

### Wirtualne srodowisko

```bash
python -m venv .venv          # utworzenie srodowiska
source .venv/bin/activate     # aktywacja (Linux / macOS)
.venv\Scripts\activate        # aktywacja (Windows PowerShell)
deactivate                    # wyjscie
```

### Jupyter Notebook / Lab

```bash
pip install jupyter           # klasyczny interfejs
pip install jupyterlab        # alternatywnie JupyterLab

jupyter notebook              # uruchomienie w biezacym katalogu
python -m jupyter lab         # wariant polecany dla Lab
```

## Podstawowe polecenia Git

```bash
git status
git add <sciezka>
git add .
git commit -m "komentarz"
git pull origin main
```

Przed zajeciami upewnij sie, ze srodowisko jest gotowe, a lokalne zmiany zostaly zarejestrowane lub odrzucone w zaleznosci od potrzeby. Powodzenia!


15:11 przerwa
