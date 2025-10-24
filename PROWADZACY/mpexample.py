import time
import requests
from multiprocessing import Pool

def fetch(url):
    """Pobiera zawartość strony (blokująco)."""
    response = requests.get(url)
    data = response.text
    print(f"Pobrano {len(data)} bajtów z {url}")
    return len(data)

def main():
    urls = [
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com/",
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com/",
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com/",
    ]

    start = time.perf_counter()

    # Utwórz pulę procesów — np. 4 równoległe procesy
    with Pool(processes=4) as pool:
        results = pool.map(fetch, urls)

    elapsed = time.perf_counter() - start
    print(f"\n⏱️ Czas wykonania (multiprocessing): {elapsed:.2f} s")
    print(f"Wyniki (długości stron): {results}")

if __name__ == "__main__":
    main()
