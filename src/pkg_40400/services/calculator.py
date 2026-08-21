"""
Calculator Service - Provides arithmetic operations
"""

from typing import Union, Any

from pkg_40400.services.exceptions import (
    DivisionByZeroError,
    InvalidInputError,
)

Number = Union[int, float]


def _convert_to_number(value: Any, param_name: str = "value") -> Number:
    """Convert value to Number, raising InvalidInputError if not possible."""
    try:
        return float(value)
    except (TypeError, ValueError) as e:
        raise InvalidInputError(f"Invalid input: '{param_name}' must be a numeric value") from e


class Calculator:
    """Calculator service providing four basic arithmetic operations."""

    @staticmethod
    def _validate_input(value: Any, param_name: str = "value") -> float:
        """
        Validate and convert input to float.

        Args:
            value: The value to validate (int, float, or numeric string)
            param_name: Name of the parameter for error messages

        Returns:
            float: The validated value as a float

        Raises:
            InvalidInputError: If the value cannot be converted to a number
        """
        try:
            return float(value)
        except (TypeError, ValueError) as e:
            raise InvalidInputError(f"Invalid input: '{param_name}' must be a numeric value") from e

    @staticmethod
    def add(a: Any, b: Any, precision: int = 10) -> float:
        """
        Add two numbers.

        Args:
            a: First number (int or float)
            b: Second number (int or float)
            precision: Number of decimal places (default: 10)

        Returns:
            float: Sum of a and b, rounded to specified precision
        """
        result = Calculator._validate_input(a, "a") + Calculator._validate_input(b, "b")
        return round(result, precision)

    @staticmethod
    def subtract(a: Any, b: Any, precision: int = 10) -> float:
        """
        Subtract second number from first.

        Args:
            a: First number (int or float)
            b: Second number (int or float)
            precision: Number of decimal places (default: 10)

        Returns:
            float: Difference of a and b, rounded to specified precision
        """
        result = Calculator._validate_input(a, "a") - Calculator._validate_input(b, "b")
        return round(result, precision)

    @staticmethod
    def multiply(a: Any, b: Any, precision: int = 10) -> float:
        """
        Multiply two numbers.

        Args:
            a: First number (int or float)
            b: Second number (int or float)
            precision: Number of decimal places (default: 10)

        Returns:
            float: Product of a and b, rounded to specified precision
        """
        result = Calculator._validate_input(a, "a") * Calculator._validate_input(b, "b")
        return round(result, precision)

    @staticmethod
    def divide(a: Any, b: Any, precision: int = 10) -> float:
        """
        Divide first number by second.

        Args:
            a: Dividend (int or float)
            b: Divisor (int or float)
            precision: Number of decimal places (default: 10)

        Returns:
            float: Quotient of a and b, rounded to specified precision

        Raises:
            DivisionByZeroError: If b is zero
            InvalidInputError: If inputs are not valid numbers
        """
        dividend = Calculator._validate_input(a, "a")
        divisor = Calculator._validate_input(b, "b")

        if divisor == 0:
            raise DivisionByZeroError("Division by zero is not allowed")

        result = dividend / divisor
        return round(result, precision)
