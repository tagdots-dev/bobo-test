"""Calculator service providing basic arithmetic operations.

All functions accept ``float`` arguments and return a ``float`` rounded to at most
four decimal places using ``round(value, 4)``.  The rounding rule matches the
requirement REQ-115 – trailing zeros are trimmed by the ``float`` conversion
after rounding, e.g. ``round(2.0, 4)`` yields ``2.0`` not ``2.0000``.

The ``divide`` function raises ``ZeroDivisionError`` when the divisor is zero
as required by REQ-401.
"""

from __future__ import annotations

__all__ = ["add", "subtract", "multiply", "divide"]


def _round_result(value: float) -> float:
    """Round *value* to at most four decimal places.

    The built-in ``round`` returns a ``float`` that may contain trailing zeros
    when represented as a string.  Converting the rounded value back to ``float``
    ensures the representation drops unnecessary zeros, satisfying REQ-115.
    """
    return float(round(value, 4))


def add(a: float, b: float) -> float:
    """Return the sum of *a* and *b*.

    Parameters
    ----------
    a, b: float
        Operands to be added.
    """
    return _round_result(a + b)


def subtract(a: float, b: float) -> float:
    """Return the difference ``a - b``."""
    return _round_result(a - b)


def multiply(a: float, b: float) -> float:
    """Return the product of *a* and *b*."""
    return _round_result(a * b)


def divide(a: float, b: float) -> float:
    """Return the quotient ``a / b``.

    Raises
    ------
        ZeroDivisionError
        If *b* is zero, as mandated by REQ-401.
    """
    if b == 0:
        # The explicit message mirrors Python's built-in exception wording.
        raise ZeroDivisionError("division by zero")
    return _round_result(a / b)
