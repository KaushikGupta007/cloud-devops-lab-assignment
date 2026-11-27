def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    return "Invalid operation"


def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    print("Result:", calculate(a, b, operation))


if __name__ == "__main__":
    main()
