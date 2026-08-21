"""
Calculator Service Exceptions
"""


class CalculatorError(Exception):
    """Base exception for calculator errors."""


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""


class InvalidInputError(CalculatorError):
    """Raised when input values cannot be converted to numbers."""