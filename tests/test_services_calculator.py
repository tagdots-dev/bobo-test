"""
Unit tests for Calculator Service.
"""

import pytest

from pkg_40400.services.calculator import (
    add,
    divide,
    multiply,
    subtract,
)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1.5, 2.5, 4.0),
        (-1.0, 1.0, 0.0),
        (0.0, 0.0, 0.0),
        (1.0, 1.0, 2.0),
    ],
)
def test_add(a: float, b: float, expected: float) -> None:
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5.0, 3.0, 2.0),
        (3.0, 5.0, -2.0),
        (0.0, 0.0, 0.0),
        (1.0, 1.0, 0.0),
    ],
)
def test_subtract(a: float, b: float, expected: float) -> None:
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2.0, 3.0, 6.0),
        (-1.0, 5.0, -5.0),
        (0.0, 100.0, 0.0),
        (1.0, 1.0, 1.0),
    ],
)
def test_multiply(a: float, b: float, expected: float) -> None:
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6.0, 2.0, 3.0),
        (10.0, 4.0, 2.5),
        (1.0, 2.0, 0.5),
        (1.0, 3.0, 0.3333),
    ],
)
def test_divide(a: float, b: float, expected: float) -> None:
    assert divide(a, b) == expected


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1.0, 0.0)
