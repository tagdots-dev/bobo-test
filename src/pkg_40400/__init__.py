from pkg_40400.core.config import AppSettings
from pkg_40400.core.decorator import ClsFalseError, raise_on_false
from pkg_40400.core.logger import Logger
from pkg_40400.logical import evaluate, validate_single_input

__version__ = "0.0.0"
version = __version__

__all__ = (
    "AppSettings",
    "ClsFalseError",
    "Logger",
    "evaluate",
    "raise_on_false",
    "validate_single_input",
    "version",
)
