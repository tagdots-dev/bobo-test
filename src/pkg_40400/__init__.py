"""Top-level package for **pkg_40400**.

Exports the core utilities, the calculator service functions and the CLI entry
point so that they can be imported directly from ``pkg_40400``.
"""

from pkg_40400.cli import cli  # expose the Click command group as a top-level attribute
from pkg_40400.core.config import AppSettings
from pkg_40400.core.decorator import ClsFalseError, raise_on_false
from pkg_40400.core.logger import Logger
from pkg_40400.services.calculator import (
    add,
    divide,
    multiply,
    subtract,
)

__version__ = "0.0.0"
version = __version__

__all__ = (
    "AppSettings",
    "ClsFalseError",
    "Logger",
    "raise_on_false",
    "version",
    "add",
    "subtract",
    "multiply",
    "divide",
    "cli",
)

# No lazy import needed for ``cli`` because it is imported eagerly above.
