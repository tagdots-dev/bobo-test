import pytest
from src.pkg_40400.cal import add, subtract, multiply, divide


class TestCalculator:
    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(-5, -3) == -8

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(-1, 1) == -2
        assert subtract(0, 0) == 0
        assert subtract(-5, -3) == -2

    def test_multiply(self):
        assert multiply(2, 3) == 6
        assert multiply(-1, 1) == -1
        assert multiply(0, 5) == 0
        assert multiply(-5, -3) == 15

    def test_divide(self):
        assert divide(6, 3) == 2
        assert divide(-1, 1) == -1
        assert divide(0, 5) == 0
        assert divide(-6, -3) == 2
        assert divide(5, 2) == 2.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(5, 0)
