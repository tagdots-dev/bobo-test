"""
Calculator Service Tests - Unit tests for pkg-40400 calculator service
"""

import pytest

from pkg_40400.services.calculator import Calculator
from pkg_40400.services.exceptions import DivisionByZeroError, InvalidInputError


class TestCalculatorAdd:
    """
    Add operation tests
    """

    def test_add_two_positive_integers(self):
        """Adding two positive integers should return their sum."""
        result = Calculator.add(2, 3)
        assert result == 5.0

    def test_add_two_positive_floats(self):
        """Adding two positive floats should return their sum."""
        result = Calculator.add(2.5, 3.7)
        assert result == 6.2

    def test_add_negative_and_positive(self):
        """Adding negative and positive should return correct sum."""
        result = Calculator.add(-5, 10)
        assert result == 5.0

    def test_add_two_negative_numbers(self):
        """Adding two negative numbers should return their sum."""
        result = Calculator.add(-3, -7)
        assert result == -10.0

    def test_add_with_scientific_notation(self):
        """Adding numbers in scientific notation should work."""
        result = Calculator.add(1e2, 2e1)
        assert result == 120.0

    def test_add_with_precision(self):
        """Adding with precision should round to specified decimal places."""
        result = Calculator.add(2.333333333, 3.666666666, precision=2)
        assert result == 6.0

    def test_add_zero_values(self):
        """Adding zero values should return the other operand."""
        result = Calculator.add(0, 42)
        assert result == 42.0

    def test_add_type_error_with_string(self):
        """Adding with string input should raise InvalidInputError."""
        with pytest.raises(InvalidInputError) as exc_info:
            Calculator.add("abc", 5)
        assert "'a' must be a numeric value" in str(exc_info.value)

    def test_add_type_error_with_none(self):
        """Adding with None input should raise InvalidInputError."""
        with pytest.raises(InvalidInputError) as exc_info:
            Calculator.add(None, 5)
        assert "'a' must be a numeric value" in str(exc_info.value)


class TestCalculatorSubtract:
    """
    Subtract operation tests
    """

    def test_subtract_two_positive_integers(self):
        """Subtracting two positive integers should return their difference."""
        result = Calculator.subtract(10, 3)
        assert result == 7.0

    def test_subtract_resulting_in_negative(self):
        """Subtracting larger from smaller should return negative."""
        result = Calculator.subtract(3, 10)
        assert result == -7.0

    def test_subtract_with_precision(self):
        """Subtracting with precision should round to specified decimal places."""
        result = Calculator.subtract(10.555, 3.333, precision=1)
        assert result == 7.2

    def test_subtract_type_error_with_string(self):
        """Subtracting with string input should raise InvalidInputError."""
        with pytest.raises(InvalidInputError) as exc_info:
            Calculator.subtract(10, "xyz")
        assert "'b' must be a numeric value" in str(exc_info.value)


class TestCalculatorMultiply:
    """
    Multiply operation tests
    """

    def test_multiply_two_positive_integers(self):
        """Multiplying two positive integers should return their product."""
        result = Calculator.multiply(4, 5)
        assert result == 20.0

    def test_multiply_positive_and_negative(self):
        """Multiplying positive and negative should return negative result."""
        result = Calculator.multiply(6, -3)
        assert result == -18.0

    def test_multiply_two_negative_numbers(self):
        """Multiplying two negative numbers should return positive."""
        result = Calculator.multiply(-4, -7)
        assert result == 28.0

    def test_multiply_with_precision(self):
        """Multiplying with precision should round to specified decimal places."""
        result = Calculator.multiply(3.333, 2.222, precision=3)
        assert result == 7.406

    def test_multiply_type_error_with_string(self):
        """Multiplying with string input should raise InvalidInputError."""
        with pytest.raises(InvalidInputError) as exc_info:
            Calculator.multiply("abc", 5)
        assert "'a' must be a numeric value" in str(exc_info.value)


class TestCalculatorDivide:
    """
    Divide operation tests
    """

    def test_divide_two_positive_integers(self):
        """Dividing two positive integers should return their quotient."""
        result = Calculator.divide(10, 2)
        assert result == 5.0

    def test_divide_resulting_in_decimal(self):
        """Dividing with remainder should return decimal result."""
        result = Calculator.divide(7, 2)
        assert result == 3.5

    def test_divide_with_precision(self):
        """Dividing with precision should round to specified decimal places."""
        result = Calculator.divide(10, 3, precision=2)
        assert result == 3.33

    def test_divide_by_zero_raises_error(self):
        """Dividing by zero should raise DivisionByZeroError."""
        with pytest.raises(DivisionByZeroError) as exc_info:
            Calculator.divide(10, 0)
        assert "Division by zero is not allowed" in str(exc_info.value)

    def test_divide_type_error_with_string(self):
        """Dividing with string input should raise InvalidInputError."""
        with pytest.raises(InvalidInputError) as exc_info:
            Calculator.divide(10, "xyz")
        assert "'b' must be a numeric value" in str(exc_info.value)


class TestCalculatorEdgeCases:
    """
    Edge cases and integration tests
    """

    def test_large_numbers(self):
        """Operations with large numbers should work correctly."""
        result = Calculator.add(1e10, 1e10)
        assert result == 2e10

    def test_small_decimal_numbers(self):
        """Operations with small decimals should preserve precision."""
        result = Calculator.add(0.000000001, 0.000000002)
        assert result == 0.000000003

    def test_chained_operations(self):
        """Multiple operations should work correctly."""
        result = Calculator.add(1, 2)
        result = Calculator.multiply(result, 3)
        assert result == 9.0

    def test_subtraction_with_negative_result(self):
        """Subtracting larger from smaller should return negative."""
        result = Calculator.subtract(5, 10)
        assert result == -5.0

    def test_division_negative_by_positive(self):
        """Dividing negative by positive should return negative."""
        result = Calculator.divide(-10, 2)
        assert result == -5.0

    def test_division_positive_by_negative(self):
        """Dividing positive by negative should return negative."""
        result = Calculator.divide(10, -2)
        assert result == -5.0

    def test_division_negative_by_negative(self):
        """Dividing negative by negative should return positive."""
        result = Calculator.divide(-10, -2)
        assert result == 5.0

    def test_multiplication_by_zero(self):
        """Multiplying by zero should return zero."""
        result = Calculator.multiply(42, 0)
        assert result == 0.0

    def test_add_with_different_precisions(self):
        """Different precision values should produce correct rounded results."""
        result = Calculator.add(1.999999999, 2.111111111, precision=5)
        assert result == 4.11111

    def test_invalid_input_non_numeric_string(self):
        """Input that is non-numeric string should fail."""
        with pytest.raises(InvalidInputError) as exc_info:
            Calculator.add("abc", "def")
        assert "'a' must be a numeric value" in str(exc_info.value)
