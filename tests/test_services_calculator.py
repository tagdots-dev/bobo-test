"""
Tests for Calculator Service Module.
"""

import pytest

from pkg_40400 import (
    add,
    divide,
    multiply,
    subtract,
)


class TestCalculatorService:
    """Test cases for calculator service functions."""

    class TestAdd:
        """Tests for add function."""

        def test_add_positive_numbers(self) -> None:
            """Test adding two positive numbers."""
            result = add(3.5, 2.5)
            assert result == 6.0

        def test_add_negative_numbers(self) -> None:
            """Test adding two negative numbers."""
            result = add(-3.5, -2.5)
            assert result == -6.0

        def test_add_mixed_numbers(self) -> None:
            """Test adding positive and negative numbers."""
            result = add(5.0, -3.0)
            assert result == 2.0

        def test_add_with_decimals(self) -> None:
            """Test adding numbers with decimal precision."""
            result = add(1.12345, 2.56789)
            assert result == 3.6913  # Rounded to 4 decimal places

        def test_add_with_zero(self) -> None:
            """Test adding with zero."""
            result = add(5.0, 0.0)
            assert result == 5.0

    class TestSubtract:
        """Tests for subtract function."""

        def test_subtract_positive_numbers(self) -> None:
            """Test subtracting two positive numbers."""
            result = subtract(10.0, 4.0)
            assert result == 6.0

        def test_subtract_negative_numbers(self) -> None:
            """Test subtracting two negative numbers."""
            result = subtract(-5.0, -3.0)
            assert result == -2.0

        def test_subtract_mixed_numbers(self) -> None:
            """Test subtracting positive and negative numbers."""
            result = subtract(5.0, -3.0)
            assert result == 8.0

        def test_subtract_with_decimals(self) -> None:
            """Test subtracting numbers with decimal precision."""
            result = subtract(5.56789, 2.12345)
            assert result == 3.4444  # Rounded to 4 decimal places

        def test_subtract_with_zero(self) -> None:
            """Test subtracting with zero."""
            result = subtract(5.0, 0.0)
            assert result == 5.0

    class TestMultiply:
        """Tests for multiply function."""

        def test_multiply_positive_numbers(self) -> None:
            """Test multiplying two positive numbers."""
            result = multiply(4.0, 5.0)
            assert result == 20.0

        def test_multiply_negative_numbers(self) -> None:
            """Test multiplying two negative numbers."""
            result = multiply(-3.0, -2.0)
            assert result == 6.0

        def test_multiply_mixed_numbers(self) -> None:
            """Test multiplying positive and negative numbers."""
            result = multiply(5.0, -3.0)
            assert result == -15.0

        def test_multiply_with_decimals(self) -> None:
            """Test multiplying numbers with decimal precision."""
            result = multiply(2.2222, 3.3333)
            assert result == 7.4073  # Rounded to 4 decimal places

        def test_multiply_with_zero(self) -> None:
            """Test multiplying with zero."""
            result = multiply(5.0, 0.0)
            assert result == 0.0

    class TestDivide:
        """Tests for divide function."""

        def test_divide_positive_numbers(self) -> None:
            """Test dividing two positive numbers."""
            result = divide(10.0, 2.0)
            assert result == 5.0

        def test_divide_negative_numbers(self) -> None:
            """Test dividing two negative numbers."""
            result = divide(-10.0, -2.0)
            assert result == 5.0

        def test_divide_mixed_numbers(self) -> None:
            """Test dividing positive by negative."""
            result = divide(10.0, -2.0)
            assert result == -5.0

        def test_divide_with_decimals(self) -> None:
            """Test dividing numbers with decimal precision."""
            result = divide(10.0, 3.0)
            assert result == 3.3333  # Rounded to 4 decimal places

        def test_divide_by_zero(self) -> None:
            """Test that dividing by zero raises ZeroDivisionError."""
            with pytest.raises(ZeroDivisionError) as exc_info:
                divide(10.0, 0.0)
            assert str(exc_info.value) == "Cannot divide by zero"
