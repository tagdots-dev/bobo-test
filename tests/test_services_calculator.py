"""Unit tests for Calculator Service."""

import pytest

from pkg_40400.services.calculator import (
    add,
    divide,
    multiply,
    subtract,
)


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (1.0, 2.0, 3.0),
        (-1.0, 1.0, 0.0),
        (0.0, 0.0, 0.0),
        (1.23456, 0.0, 1.2346),  # rounded to 4 decimals
        (1.11115, 0.0, 1.1112),  # round half up
    ],
)
def test_add(a: float, b: float, expected: float) -> None:
    """Test add() with various inputs."""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (5.0, 3.0, 2.0),
        (1.0, 1.0, 0.0),
        (0.0, 0.0, 0.0),
        (1.23456, 0.0, 1.2346),
        (-1.0, 1.0, -2.0),
    ],
)
def test_subtract(a: float, b: float, expected: float) -> None:
    """Test subtract() with various inputs."""
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2.0, 3.0, 6.0),
        (0.0, 5.0, 0.0),
        (1.0, 1.0, 1.0),
        (1.23456, 1.0, 1.2346),
        (-2.0, 3.0, -6.0),
    ],
)
def test_multiply(a: float, b: float, expected: float) -> None:
    """Test multiply() with various inputs."""
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (6.0, 3.0, 2.0),
        (1.0, 2.0, 0.5),
        (0.0, 5.0, 0.0),
        (1.23456, 1.0, 1.2346),
        (-6.0, 2.0, -3.0),
    ],
)
def test_divide(a: float, b: float, expected: float) -> None:
    """Test divide() with various inputs."""
    assert divide(a, b) == expected


def test_divide_by_zero_raises() -> None:
    """Test divide() raises ZeroDivisionError when b is zero."""
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide(1.0, 0.0)
    assert str(exc_info.value) == "division by zero"
