"""Tests for the calculator service functions.

The tests verify correct arithmetic, rounding behaviour, type handling and the
ZeroDivisionError raised by ``divide`` when the divisor is zero.  They are placed
in the ``tests`` package so that ``pytest`` discovers them automatically.
"""

import math

import pytest

from pkg_40400 import (
    add,
    divide,
    multiply,
    subtract,
)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1.0, 2.0, 3.0),
        (0.1, 0.2, 0.3),  # rounding to 4 decimals should keep 0.3
        (12345.6789, 0.0001, 12345.679),
    ],
)
def test_add(a: float, b: float, expected: float) -> None:
    assert math.isclose(add(a, b), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5.0, 3.0, 2.0),
        (0.3, 0.1, 0.2),
        (100.0, 0.1234, 99.8766),
    ],
)
def test_subtract(a: float, b: float, expected: float) -> None:
    assert math.isclose(subtract(a, b), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2.0, 3.0, 6.0),
        (0.1, 0.2, 0.02),
        (123.456, 0.001, 0.1235),  # 0.123456 rounded to 4 dp -> 0.1235
    ],
)
def test_multiply(a: float, b: float, expected: float) -> None:
    assert math.isclose(multiply(a, b), expected, rel_tol=1e-9)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6.0, 3.0, 2.0),
        (1.0, 3.0, 0.3333),
        (10.0, 4.0, 2.5),
    ],
)
def test_divide(a: float, b: float, expected: float) -> None:
    assert math.isclose(divide(a, b), expected, rel_tol=1e-9)


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1.0, 0.0)
