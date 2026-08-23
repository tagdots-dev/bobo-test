"""
Calculator Service - Core arithmetic operations module.

This module provides basic arithmetic functions: add, subtract, multiply, divide.
It does NOT contain any CLI logic - it is a pure service layer.
"""


def add(a: float, b: float) -> float:
    """
    Compute the sum of two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The sum of a and b, rounded to at most 4 decimal places.
    """
    result = a + b
    return round(result, 4)


def subtract(a: float, b: float) -> float:
    """
    Compute the difference of two numbers.

    Args:
        a: First operand (minuend).
        b: Second operand (subtrahend).

    Returns:
        The difference of a and b (a - b), rounded to at most 4 decimal places.

    Raises:
        ZeroDivisionError: This function does not raise ZeroDivisionError,
            but is included for API consistency with other operations.
    """
    result = a - b
    return round(result, 4)


def multiply(a: float, b: float) -> float:
    """
    Compute the product of two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The product of a and b, rounded to at most 4 decimal places.
    """
    result = a * b
    return round(result, 4)


def divide(a: float, b: float) -> float:
    """
    Compute the quotient of two numbers.

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        The quotient of a divided by b, rounded to at most 4 decimal places.

    Raises:
        ZeroDivisionError: If b is zero, a ZeroDivisionError is raised
            with a Python built-in error message.
    """
    if b == 0:
        raise ZeroDivisionError("float division by zero")
    result = a / b
    return round(result, 4)
