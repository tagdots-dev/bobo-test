"""
Calculator Service providing basic arithmetic operations.
"""


def add(a: float, b: float) -> float:
    """Add two numbers and return the result rounded to 4 decimal places."""
    return round(a + b, 4)


def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result rounded to 4 decimal places."""
    return round(a - b, 4)


def multiply(a: float, b: float) -> float:
    """Multiply two numbers and return the result rounded to 4 decimal places."""
    return round(a * b, 4)


def divide(a: float, b: float) -> float:
    """Divide a by b and return the result rounded to 4 decimal places.

    Raises ZeroDivisionError if b is zero.
    """
    return round(a / b, 4)
