"""
Calculator Service Module.

Provides arithmetic operations: addition, subtraction, multiplication, and division.
All operations work with float types and return results with up to 10 decimal places precision.
"""

from typing import Union


def add(a: Union[float, int, str], b: Union[float, int, str]) -> float:
    """
    Add two numbers and return the result as a float.

    Args:
        a: First number (float, int, or string convertible to float)
        b: Second number (float, int, or string convertible to float)

    Returns:
        Sum as a float rounded to 10 decimal places
    """
    result = float(a) + float(b)
    return round(result, 10)


def subtract(a: Union[float, int, str], b: Union[float, int, str]) -> float:
    """
    Subtract second number from first and return the result as a float.

    Args:
        a: First number (float, int, or string convertible to float)
        b: Second number (float, int, or string convertible to float)

    Returns:
        Difference as a float rounded to 10 decimal places
    """
    result = float(a) - float(b)
    return round(result, 10)


def multiply(a: Union[float, int, str], b: Union[float, int, str]) -> float:
    """
    Multiply two numbers and return the result as a float.

    Args:
        a: First number (float, int, or string convertible to float)
        b: Second number (float, int, or string convertible to float)

    Returns:
        Product as a float rounded to 10 decimal places
    """
    result = float(a) * float(b)
    return round(result, 10)


def divide(a: Union[float, int, str], b: Union[float, int, str]) -> float:
    """
    Divide first number by second and return the result as a float.

    Args:
        a: Dividend (float, int, or string convertible to float)
        b: Divisor (float, int, or string convertible to float)

    Returns:
        Quotient as a float rounded to 10 decimal places

    Raises:
        ZeroDivisionError: If divisor is zero
    """
    float_a = float(a)
    float_b = float(b)

    if float_b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")

    result = float_a / float_b
    return round(result, 10)
