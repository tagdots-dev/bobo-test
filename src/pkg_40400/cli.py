"""
Test Logging and Decorator
"""

from pkg_40400 import (
    ClsFalseError,
    Logger,
    raise_on_false,
    version,
)


@raise_on_false(exception_type=ClsFalseError, custom_message="")
def try_decorator(enable_log: bool = False) -> bool:
    """
    Return False Intentionally To Test Decorator
    """
    return False


def main() -> bool:
    Logger.info(f"{version}")

    try:
        return try_decorator(enable_log=True)
    except ClsFalseError:
        return False


if __name__ == "__main__":
    main()
