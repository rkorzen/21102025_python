def cache(func):
    result = {}

    def wrapper(n):
        if n in result:
            return result[n]
        r = func(n)
        result[n] = r
        return r

    return wrapper


@cache
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


[fibonacci(i) for i in range(20)]