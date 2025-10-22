import logging
from functools import wraps
import time

logging.basicConfig(
    level=logging.DEBUG,
    filename="example.log",
    format='%(asctime)s %(levelname)s %(name)s | %(funcName)s | %(message)s'
)

logger = logging.getLogger(__name__)

def loguj(funkcja):

    @wraps(funkcja)
    def opakowanie(*args, **kwargs):
        start = time.perf_counter()
        try:
            wynik = funkcja(*args, **kwargs)
            stop = time.perf_counter()
            elapsed = (stop - start) * 1000
            logger.info(f"{funkcja.__name__} wykonana w {elapsed:.4f} s")
        except Exception as e:

            stop = time.perf_counter()
            elapsed = (stop - start) * 1000

            logger.error(f"Błąd w {funkcja.__name__} po {elapsed:.4f} s:\n {e}", exc_info=True)
            raise

        return wynik

    return opakowanie

@loguj
def policz_sume(n: int):
    return sum(range(n))

@loguj
def policz_sume_z_bledem(n: int):
    suma=0
    for i in range(n):
        if i == n // 2:
            raise ValueError(f"Nie mozna policzyc sume w punkcie {i}")
        suma += i
    return suma

print(policz_sume(10))
print(policz_sume_z_bledem(10))
