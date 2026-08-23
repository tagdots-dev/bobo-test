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
    "add",
    "AppSettings",
    "ClsFalseError",
    "divide",
    "Logger",
    "multiply",
    "raise_on_false",
    "subtract",
    "version",
)
