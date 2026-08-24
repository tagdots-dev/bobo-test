"""Calculator Service for pkg-40400 CLI.

Provides basic arithmetic operations: add, subtract, multiply, divide.
All inputs and outputs are float; results rounded to 4 decimal places.
"""


def add(a: float, b: float) -> float:
    """Return sum of a and b, rounded to 4 decimal places."""
    return round(a + b, 4)


def subtract(a: float, b: float) -> float:
    """Return difference of a and b, rounded to 4 decimal places."""
    return round(a - b, 4)


def multiply(a: float, b: float) -> float:
    """Return product of a and b, rounded to 4 decimal places."""
    return round(a * b, 4)


def divide(a: float, b: float) -> float:
    """Return quotient of a divided by b, rounded to 4 decimal places.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return round(a / b, 4)


__all__ = ["add", "subtract", "multiply", "divide"]
