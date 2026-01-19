class Calculator:
    """Simple calculator that supports basic arithmetic operations."""

    def add(self, x, y):
        """Return the sum of two numbers."""
        return x + y

    def subtract(self, x, y):
        """Return the difference of two numbers (x - y)."""
        return x - y

    def multiply(self, x, y):
        """Return the product of two numbers."""
        return x * y


if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
    print("Supported operations: addition, subtraction, multiplication")
    print("Example: 5 + 3 =", calc.add(5, 3))
    print("Example: 5 - 3 =", calc.subtract(5, 3))
    print("Example: 5 * 3 =", calc.multiply(5, 3))