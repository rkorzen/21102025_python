def add(a, b):
    return a + b

def sub(a, b): return a - b

def mul(a, b): return a * b

def div(a, b): return a / b

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def get_data():
    operation = input("Podaj rodzaj operacji (+-/*): ")

    if operation not in operations:
        raise ValueError("Podano niepoprawny operator!!")

    a = int(input("Podaj pierwszy argument: "))
    b = int(input("Podaj drugi argument: "))
    # print(dir())
    # print(locals())
    # print(globals())
    return operation, a, b


def main():
    operation, a, b = get_data()

    result = operations[operation](a, b)
    print(f"Wynik operacji {a}{operation}{b} = {result}")


print(dir())

if __name__ == "__main__":
    main()
    ...

