import pytest

from pkg_40400 import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1.0, 2.0, 3.0),
        (1.1234, 2.8766, 4.0),  # rounding to 4 decimals yields exact 4.0
        (-5.5, 2.0, -3.5),
    ],
)
def test_add(a: float, b: float, expected: float):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5.0, 3.0, 2.0),
        (2.5555, 1.5555, 1.0),
        (-1.0, -1.0, 0.0),
    ],
)
def test_subtract(a: float, b: float, expected: float):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2.0, 3.0, 6.0),
        (1.2345, 2.0, 2.469),
        (-2.0, -2.5, 5.0),
    ],
)
def test_multiply(a: float, b: float, expected: float):
    assert multiply(a, b) == expected


def test_divide_normal():
    assert divide(10.0, 4.0) == 2.5


def test_divide_zero_error():
    with pytest.raises(ZeroDivisionError):
        divide(1.0, 0.0)
