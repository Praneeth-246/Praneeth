class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == "addition":
            return self.a + self.b
        elif self.operation == "subtraction":
            return self.a - self.b
        elif self.operation == "multiplication":
            return self.a * self.b
        elif self.operation == "division":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Error: Invalid operation type"


# Example usage
if __name__ == "__main__":
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    operation = input("Enter operation (Addition, Subtraction, Multiplication, Division): ")

    calc = Calculator(a, b, operation)
    result = calc.calculate()
    print(f"Result: {result}")
