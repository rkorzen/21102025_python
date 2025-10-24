import time
import requests
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    """Pobiera zawartość strony (blokująco)."""
    response = requests.get(url)
    data = response.text
    print(f"Pobrano {len(data)} bajtów z {url}")

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

    # ThreadPoolExecutor uruchamia fetch() równolegle w wielu wątkach
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(fetch, urls)

    elapsed = time.perf_counter() - start
    print(f"\n⏱️ Czas wykonania (threading): {elapsed:.2f} s")

if __name__ == "__main__":
    main()

