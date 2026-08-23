"""
Unit tests for the Calculator Service.
"""

import pytest

from pkg_40400.services.calculator import add, subtract, multiply, divide


class TestAdd:
    def test_add_two_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(1.0, 2.0) == 3.0

    def test_add_two_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-1.0, -2.0) == -3.0

    def test_add_positive_and_negative(self):
        """Test adding a positive and a negative number."""
        assert add(5.0, -3.0) == 2.0

    def test_add_zeros(self):
        """Test adding zeros."""
        assert add(0.0, 0.0) == 0.0

    def test_add_returns_float(self):
        """Test that add returns a float."""
        assert isinstance(add(1.0, 2.0), float)

    def test_add_rounds_to_4_decimal_places(self):
        """Test that add rounds to 4 decimal places."""
        assert add(1.11111, 2.22222) == 3.3333


class TestSubtract:
    def test_subtract_two_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5.0, 3.0) == 2.0

    def test_subtract_returns_float(self):
        """Test that subtract returns a float."""
        assert isinstance(subtract(5.0, 3.0), float)

    def test_subtract_rounds_to_4_decimal_places(self):
        """Test that subtract rounds to 4 decimal places."""
        assert subtract(5.55555, 2.22222) == 3.3333


class TestMultiply:
    def test_multiply_two_numbers(self):
        """Test multiplying two numbers."""
        assert multiply(3.0, 4.0) == 12.0

    def test_multiply_returns_float(self):
        """Test that multiply returns a float."""
        assert isinstance(multiply(3.0, 4.0), float)

    def test_multiply_rounds_to_4_decimal_places(self):
        """Test that multiply rounds to 4 decimal places."""
        assert multiply(1.1111, 2.2222) == 2.4691


class TestDivide:
    def test_divide_two_numbers(self):
        """Test dividing two numbers."""
        assert divide(10.0, 2.0) == 5.0

    def test_divide_returns_float(self):
        """Test that divide returns a float."""
        assert isinstance(divide(10.0, 2.0), float)

    def test_divide_by_zero_raises(self):
        """Test that dividing by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            divide(10.0, 0.0)

    def test_divide_rounds_to_4_decimal_places(self):
        """Test that divide rounds to 4 decimal places."""
        assert divide(1.0, 3.0) == 0.3333
