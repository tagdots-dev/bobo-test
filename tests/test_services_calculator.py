"""
Unit tests for the Calculator Service.

Tests the arithmetic operations: add, subtract, multiply, divide.
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
        """Test adding two positive numbers."""
        result = add(3.0, 5.0)
        assert result == 8.0

    def test_add_negative_numbers(self) -> None:
        """Test adding two negative numbers."""
        result = add(-3.0, -5.0)
        assert result == -8.0

    def test_add_mixed_numbers(self) -> None:
        """Test adding positive and negative numbers."""
        result = add(-3.0, 5.0)
        assert result == 2.0

    def test_add_with_integers(self) -> None:
        """Test adding integer values (should be converted to float)."""
        result = add(3, 5)
        assert result == 8.0

    def test_add_with_floats(self) -> None:
        """Test adding float values."""
        result = add(3.14159, 2.71828)
        assert result == 5.85987

    def test_add_precision(self) -> None:
        """Test that results are rounded to 10 decimal places."""
        result = add(1.0 / 3.0, 1.0 / 6.0)
        assert result == 0.5
        assert len(str(result).split(".")[-1]) <= 10

    def test_add_invalid_type(self) -> None:
        """Test that adding non-numeric types raises ValueError (from float conversion)."""
        with pytest.raises(ValueError):
            add("abc", 5)
        with pytest.raises(ValueError):
            add(3, "xyz")


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_numbers(self) -> None:
        """Test subtracting two positive numbers."""
        result = subtract(10.0, 3.0)
        assert result == 7.0

    def test_subtract_negative_result(self) -> None:
        """Test subtracting to get a negative result."""
        result = subtract(3.0, 10.0)
        assert result == -7.0

    def test_subtract_with_integers(self) -> None:
        """Test subtracting integer values."""
        result = subtract(10, 3)
        assert result == 7.0

    def test_subtract_precision(self) -> None:
        """Test that results are rounded to 10 decimal places."""
        result = subtract(1.0, 0.3333333333)
        assert len(str(result).split(".")[-1]) <= 10

    def test_subtract_invalid_type(self) -> None:
        """Test that subtracting non-numeric types raises ValueError (from float conversion)."""
        with pytest.raises(ValueError):
            subtract("abc", 3)
        with pytest.raises(ValueError):
            subtract(10, "xyz")


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_numbers(self) -> None:
        """Test multiplying two positive numbers."""
        result = multiply(4.0, 5.0)
        assert result == 20.0

    def test_multiply_negative_numbers(self) -> None:
        """Test multiplying two negative numbers."""
        result = multiply(-4.0, -5.0)
        assert result == 20.0

    def test_multiply_mixed_numbers(self) -> None:
        """Test multiplying positive and negative numbers."""
        result = multiply(-4.0, 5.0)
        assert result == -20.0

    def test_multiply_by_zero(self) -> None:
        """Test multiplying by zero."""
        result = multiply(4.0, 0.0)
        assert result == 0.0

    def test_multiply_with_integers(self) -> None:
        """Test multiplying integer values."""
        result = multiply(4, 5)
        assert result == 20.0

    def test_multiply_precision(self) -> None:
        """Test that results are rounded to 10 decimal places."""
        result = multiply(1.0 / 3.0, 3.0)
        assert result == 1.0

    def test_multiply_invalid_type(self) -> None:
        """Test that multiplying non-numeric types raises ValueError (from float conversion)."""
        with pytest.raises(ValueError):
            multiply("abc", 5)
        with pytest.raises(ValueError):
            multiply(4, "xyz")


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_numbers(self) -> None:
        """Test dividing two positive numbers."""
        result = divide(10.0, 2.0)
        assert result == 5.0

    def test_divide_negative_numbers(self) -> None:
        """Test dividing two negative numbers."""
        result = divide(-10.0, -2.0)
        assert result == 5.0

    def test_divide_mixed_numbers(self) -> None:
        """Test dividing positive by negative number."""
        result = divide(-10.0, 2.0)
        assert result == -5.0

    def test_divide_with_integers(self) -> None:
        """Test dividing integer values."""
        result = divide(10, 2)
        assert result == 5.0

    def test_divide_precision(self) -> None:
        """Test that results are rounded to 10 decimal places."""
        result = divide(1.0, 3.0)
        assert len(str(result).split(".")[-1]) <= 10

    def test_divide_by_zero(self) -> None:
        """Test that dividing by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            divide(10.0, 0.0)

    def test_divide_invalid_type(self) -> None:
        """Test that dividing non-numeric types raises ValueError (from float conversion)."""
        with pytest.raises(ValueError):
            divide("abc", 2)
        with pytest.raises(ValueError):
            divide(10, "xyz")
