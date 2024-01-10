#!/usr/bin/python3
"""Module for basic operations."""


class Calculator:
    """A simple calculator class."""

    def add(self, x, y):
        """Add two numbers."""
        result = x + y
        return result

    def subtract(self, x, y):
        """Subtract y from x."""
        result = x - y
        return result


def main():
    """Main function."""
    calc = Calculator()
    result_add = calc.add(5, 7)
    result_subtract = calc.subtract(10, 3)

    print("Addition result:", result_add)
    print("Subtraction result:", result_subtract)


if __name__ == "__main__":
    main()
