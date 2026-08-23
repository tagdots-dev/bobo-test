"""
Calculator Service

Provides basic arithmetic operations: add, subtract, multiply, and divide.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b, rounded to 4 decimal places."""
    return round(a + b, 4)


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b, rounded to 4 decimal places."""
    return round(a - b, 4)


def multiply(a: float, b: float) -> float:
    """Return the product of a and b, rounded to 4 decimal places."""
    return round(a * b, 4)


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b, rounded to 4 decimal places.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return round(a / b, 4)