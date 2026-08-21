"""
Calculator Service Module

Provides basic arithmetic operations: add, subtract, multiply, and divide.
"""

# Division by zero is handled by raising ZeroDivisionError (Python built-in)


def add(a: float, b: float) -> float:
    """Add two numbers."""
    result = a + b
    return round(result, 4)


def subtract(a: float, b: float) -> float:
    """Subtract second number from first."""
    result = a - b
    return round(result, 4)


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    result = a * b
    return round(result, 4)


def divide(a: float, b: float) -> float:
    """Divide first number by second."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = a / b
    return round(result, 4)
