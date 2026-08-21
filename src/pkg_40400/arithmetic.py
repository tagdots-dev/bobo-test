"""
Calculator CLI Application

A simple calculator that performs basic arithmetic operations on two float values.
Supports addition, subtraction, multiplication, and division.
"""


def calculate(first: float, second: float, operation: str) -> float:
    """
    Perform arithmetic operation on two float values.

    Args:
        first: The first operand (must be a float)
        second: The second operand (must be a float)
        operation: The operation to perform (+, -, *, /)

    Returns:
        The result of the calculation

    Raises:
        ZeroDivisionError: If attempting to divide by zero
    """
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return round(first / second, 4)
    else:
        raise ValueError(f"Unsupported operation: {operation}")
