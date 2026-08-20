def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation, a, b):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return operations[operation](a, b)


def main():
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'quit' to exit\n")

    while True:
        operation = input("Operation: ").strip().lower()
        if operation == "quit":
            print("Goodbye!")
            break

        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            result = calculate(operation, a, b)
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
