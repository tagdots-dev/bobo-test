"""
Calculator Service — Pure arithmetic operations using float types.
"""

# from typing import Final


def add(a: float, b: float) -> float:
    """Return the sum of two numbers, rounded to 4 decimal places."""
    return round(a + b, 4)


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers, rounded to 4 decimal places."""
    return round(a - b, 4)


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers, rounded to 4 decimal places."""
    return round(a * b, 4)


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers, rounded to 4 decimal places.

    Raises:
        ZeroDivisionError: If divisor `b` is zero.
    """
    if b == 0.0:
        raise ZeroDivisionError("division by zero")
    return round(a / b, 4)


# __all__: Final[tuple[str, ...]] = ("add", "subtract", "multiply", "divide")
