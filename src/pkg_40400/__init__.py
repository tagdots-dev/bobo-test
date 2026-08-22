"""Top‑level package for ``pkg_40400``.

Exports:
* Core utilities (AppSettings, Logger, decorator helpers)
* Calculator Service functions (add, subtract, multiply, divide)
"""

from pkg_40400.core.config import AppSettings
from pkg_40400.core.decorator import ClsFalseError, raise_on_false
from pkg_40400.core.logger import Logger

# ---- CALCULATOR SERVICE EXPORTS ---------------------------------
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
    "add",
    "subtract",
    "multiply",
    "divide",
    "version",
)
