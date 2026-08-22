"""Calculator Service – provides basic arithmetic operations.

All functions:
* accept two ``float`` arguments,
* return a ``float`` rounded to at most 4 decimal places,
* raise ``ZeroDivisionError`` for division by zero (REQ‑401).

The module is deliberately free of any CLI or logging concerns –
it is pure business logic (REQ‑111‑115).
"""

from __future__ import annotations

from typing import Final

# Helper constant – used by all functions for consistent rounding
_MAX_DECIMALS: Final[int] = 4


def _round(value: float) -> float:
    """Round ``value`` to at most 4 decimal places, removing trailing zeros.

    ``round`` already drops unnecessary trailing zeros when the result is
    converted back to ``float`` (e.g. ``round(2.0, 4)`` → ``2.0``).
    """
    return round(value, _MAX_DECIMALS)


def add(a: float, b: float) -> float:
    """Return the sum of *a* and *b*."""
    return _round(a + b)


def subtract(a: float, b: float) -> float:
    """Return the difference *a* – *b*."""
    return _round(a - b)


def multiply(a: float, b: float) -> float:
    """Return the product of *a* and *b*."""
    return _round(a * b)


def divide(a: float, b: float) -> float:
    """Return the quotient *a* / *b*.

    Raises
    ------
    ZeroDivisionError
        If ``b`` is ``0.0`` (REQ‑401).
    """
    if b == 0.0:
        # Propagate the built‑in ZeroDivisionError with its default message.
        raise ZeroDivisionError("float division by zero")
    return _round(a / b)
