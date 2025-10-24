
import time
import requests
from multiprocessing import Pool

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

    with Pool(processes=9) as pool:
        pool.map(fetch, urls)

    elapsed = time.perf_counter() - start

    print(f"Czas wykonania (synchr): {elapsed:.2f} s")

if __name__ == "__main__":
    main()
