"""
Unit tests for the Calculator Service.

Tests all arithmetic functions: add, subtract, multiply, divide.
Ensures >90% coverage per REQ-105.
"""

import pytest

from pkg_40400.services.calculator import (
    add,
    divide,
    multiply,
    subtract,
)


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self) -> None:
        """WHEN adding two positive numbers THEN the sum is returned."""
        assert add(2.0, 3.0) == 5.0

    def test_add_negative_numbers(self) -> None:
        """WHEN adding two negative numbers THEN the sum is returned."""
        assert add(-2.0, -3.0) == -5.0

    def test_add_mixed_signs(self) -> None:
        """WHEN adding numbers with mixed signs THEN the correct sum is returned."""
        assert add(-2.0, 3.0) == 1.0

    def test_add_zeros(self) -> None:
        """WHEN adding two zeros THEN zero is returned."""
        assert add(0.0, 0.0) == 0.0

    def test_add_floats_rounded(self) -> None:
        """WHEN adding floats with many decimal places THEN result is rounded to 4."""
        assert add(1.11111, 2.22222) == 3.3333

    def test_add_returns_float(self) -> None:
        """WHEN adding two numbers THEN the result is a float."""
        result = add(1.0, 2.0)
        assert isinstance(result, float)


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self) -> None:
        """WHEN subtracting two positive numbers THEN the difference is returned."""
        assert subtract(5.0, 3.0) == 2.0

    def test_subtract_negative_numbers(self) -> None:
        """WHEN subtracting two negative numbers THEN the difference is returned."""
        assert subtract(-5.0, -3.0) == -2.0

    def test_subtract_mixed_signs(self) -> None:
        """WHEN subtracting numbers with mixed signs THEN the correct difference is returned."""
        assert subtract(-2.0, 3.0) == -5.0

    def test_subtract_zeros(self) -> None:
        """WHEN subtracting zero from zero THEN zero is returned."""
        assert subtract(0.0, 0.0) == 0.0

    def test_subtract_floats_rounded(self) -> None:
        """WHEN subtracting floats with many decimal places THEN result is rounded to 4."""
        assert subtract(5.55555, 2.22222) == 3.3333

    def test_subtract_returns_float(self) -> None:
        """WHEN subtracting two numbers THEN the result is a float."""
        result = subtract(1.0, 2.0)
        assert isinstance(result, float)


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self) -> None:
        """WHEN multiplying two positive numbers THEN the product is returned."""
        assert multiply(2.0, 3.0) == 6.0

    def test_multiply_negative_numbers(self) -> None:
        """WHEN multiplying two negative numbers THEN the positive product is returned."""
        assert multiply(-2.0, -3.0) == 6.0

    def test_multiply_mixed_signs(self) -> None:
        """WHEN multiplying numbers with mixed signs THEN the negative product is returned."""
        assert multiply(-2.0, 3.0) == -6.0

    def test_multiply_by_zero(self) -> None:
        """WHEN multiplying by zero THEN zero is returned."""
        assert multiply(5.0, 0.0) == 0.0

    def test_multiply_floats_rounded(self) -> None:
        """WHEN multiplying floats with many decimal places THEN result is rounded to 4."""
        assert multiply(1.11111, 2.22222) == 2.4691

    def test_multiply_returns_float(self) -> None:
        """WHEN multiplying two numbers THEN the result is a float."""
        result = multiply(1.0, 2.0)
        assert isinstance(result, float)


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_numbers(self) -> None:
        """WHEN dividing two positive numbers THEN the quotient is returned."""
        assert divide(6.0, 3.0) == 2.0

    def test_divide_negative_numbers(self) -> None:
        """WHEN dividing two negative numbers THEN the positive quotient is returned."""
        assert divide(-6.0, -3.0) == 2.0

    def test_divide_mixed_signs(self) -> None:
        """WHEN dividing numbers with mixed signs THEN the negative quotient is returned."""
        assert divide(-6.0, 3.0) == -2.0

    def test_divide_by_zero_raises_error(self) -> None:
        """WHEN dividing by zero THEN ZeroDivisionError is raised."""
        with pytest.raises(ZeroDivisionError):
            divide(5.0, 0.0)

    def test_divide_floats_rounded(self) -> None:
        """WHEN dividing floats THEN result is rounded to 4 decimal places."""
        assert divide(1.0, 3.0) == 0.3333

    def test_divide_returns_float(self) -> None:
        """WHEN dividing two numbers THEN the result is a float."""
        result = divide(6.0, 3.0)
        assert isinstance(result, float)

    def test_divide_exact_result_not_padded(self) -> None:
        """WHEN dividing to an exact result THEN trailing zeros are not added."""
        result = divide(2.0, 1.0)
        assert result == 2.0
        assert str(result) == "2.0"
