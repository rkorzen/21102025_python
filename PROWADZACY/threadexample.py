import time
import requests
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    response = requests.get(url)
    data = response.text
    print(f"Pobrano {len(data)} bajtów z {url}")


def main():

    urls = [
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com",
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com",
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com",
    ]

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(fetch, urls)

    elapsed = time.perf_counter() - start

    print(f"Czas wykonania (synchr): {elapsed:.2f} s")

main()
