"""
Tests for the Calculator Service
"""

import pytest

from pkg_40400.services.calculator import add, divide, multiply, subtract


class TestAdd:
    """Tests for the add function"""

    def test_add_positive_numbers(self) -> None:
        assert add(2.0, 3.0) == 5.0

    def test_add_negative_numbers(self) -> None:
        assert add(-2.0, -3.0) == -5.0

    def test_add_mixed_numbers(self) -> None:
        assert add(-2.0, 3.0) == 1.0

    def test_add_with_decimals(self) -> None:
        assert add(1.2345, 2.3456) == 3.5801

    def test_add_rounds_to_4_decimals(self) -> None:
        assert add(0.12345, 0.6789) == 0.8023

    def test_add_zero(self) -> None:
        assert add(0.0, 5.0) == 5.0


class TestSubtract:
    """Tests for the subtract function"""

    def test_subtract_positive_numbers(self) -> None:
        assert subtract(5.0, 3.0) == 2.0

    def test_subtract_negative_result(self) -> None:
        assert subtract(3.0, 5.0) == -2.0

    def test_subtract_with_decimals(self) -> None:
        assert subtract(3.5795, 1.2345) == 2.345

    def test_subtract_rounds_to_4_decimals(self) -> None:
        assert subtract(0.80235, 0.12345) == 0.6789

    def test_subtract_zero(self) -> None:
        assert subtract(5.0, 0.0) == 5.0


class TestMultiply:
    """Tests for the multiply function"""

    def test_multiply_positive_numbers(self) -> None:
        assert multiply(2.0, 3.0) == 6.0

    def test_multiply_negative_numbers(self) -> None:
        assert multiply(-2.0, -3.0) == 6.0

    def test_multiply_mixed_numbers(self) -> None:
        assert multiply(-2.0, 3.0) == -6.0

    def test_multiply_with_decimals(self) -> None:
        assert multiply(1.5, 2.5) == 3.75

    def test_multiply_rounds_to_4_decimals(self) -> None:
        assert multiply(0.12345, 0.67890) == 0.0838

    def test_multiply_by_zero(self) -> None:
        assert multiply(0.0, 5.0) == 0.0


class TestDivide:
    """Tests for the divide function"""

    def test_divide_positive_numbers(self) -> None:
        assert divide(6.0, 3.0) == 2.0

    def test_divide_negative_numbers(self) -> None:
        assert divide(-6.0, -3.0) == 2.0

    def test_divide_mixed_numbers(self) -> None:
        assert divide(-6.0, 3.0) == -2.0

    def test_divide_with_decimals(self) -> None:
        assert divide(1.0, 4.0) == 0.25

    def test_divide_rounds_to_4_decimals(self) -> None:
        assert divide(1.0, 3.0) == 0.3333

    def test_divide_by_zero_raises_exception(self) -> None:
        with pytest.raises(ZeroDivisionError) as excinfo:
            divide(5.0, 0.0)
        assert "division by zero" in str(excinfo.value)