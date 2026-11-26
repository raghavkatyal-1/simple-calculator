"""Simple command-line calculator.

UCS 745 Cloud and DevOps - Lab Assignment (Q1)
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return round(a / b, 4)


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"Unsupported operator: {op}")
    return OPERATIONS[op](a, b)


def main():
    print("Simple Calculator (type 'q' to quit)")
    while True:
        expr = input("Enter expression (e.g. 8 / 2): ").strip()
        if expr.lower() == "q":
            break
        try:
            a, op, b = expr.split()
            print("Result:", calculate(float(a), op, float(b)))
        except ValueError as err:
            print("Error:", err)


if __name__ == "__main__":
    main()
