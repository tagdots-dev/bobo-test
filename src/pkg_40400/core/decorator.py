from functools import wraps
from typing import Callable, Optional, TypeVar

from pkg_40400.core.logger import get_logger

F = TypeVar("F", bound=Callable[..., bool])


class ClsFalseError(ValueError):
    """Exception raised when a function decorated with @raise_on_false returns False."""

    def __init__(self, func_name: str, custom_message: Optional[str] = None) -> None:
        """
        Initialize the exception.

        Args:
            func_name: Name of the function that returned False.
            custom_message: Optional custom message to include in the error.
        """
        self.func_name = func_name
        self.custom_message = custom_message

        if custom_message is not None:
            message = f"{func_name} returned '{custom_message}'"
        else:
            message = f"{func_name} returned 'False'"
        super().__init__(message)


def raise_on_false(
    exception_type: type[ValueError] = ClsFalseError,
    custom_message: Optional[str] = None,
    log_error: bool = True,
):
    """
    Decorator that raises an exception if the decorated function returns False.

    Args:
        exception_type: The exception type to raise. Must be a subclass of ValueError.
        custom_message: Optional custom message to include in the exception.
        log_error: If True, log the error using the configured logger before raising.

    Returns:
        A decorator function.

    Usage:
        @raise_on_false()
        def validate_input(data: dict) -> bool:
            return "required_key" in data

        @raise_on_false(custom_message="Data validation failed", log_error=False)
        def process_data(data: dict) -> bool:
            return validate_required_fields(data)
    """
    if not issubclass(exception_type, ValueError):
        raise TypeError(f"exception_type must be a subclass of ValueError, got {exception_type}")

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if not result:
                exception = exception_type(func.__name__, custom_message)

                if log_error:
                    logger = get_logger()
                    # Use stacklevel=2 to point to the caller (wrapper's caller), not the decorator
                    logger.error(str(exception), stacklevel=2)

                raise exception

            return result

        return wrapper  # type: ignore[return-value]

    return decorator
