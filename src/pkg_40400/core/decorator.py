from functools import wraps

from pkg_40400.core.logger import Logger


class ClsFalseError(ValueError):
    def __init__(self, func, return_value=None) -> None:
        self.func_name = func
        self.return_value = return_value

        # return_value : custom_message from decorated function OR
        #              : if None, will be processed below
        if return_value is not None:
            clserr_message = f"Function '{func}' returned '{return_value}'"
        else:
            clserr_message = f"Function {func} returned 'False'"
        super().__init__(clserr_message)


def raise_on_false(exception_type=ClsFalseError, custom_message=None):
    """
    Raise an exception if the decorated function returns False
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not result:
                """
                custom_message : defined in decorated function; pass return_value = custom_message to ClsFalseError
                clserr_message : defined in ClsFalseError     ; pass return_value = None to ClsFalseError
                """
                if exception_type is ClsFalseError and not custom_message:
                    exception = exception_type(func.__name__)
                else:
                    exception = exception_type(func.__name__, custom_message)

                if kwargs.get("enable_log"):
                    Logger.error(f"{str(exception)}", stacklevel=2)
                raise exception
            return result

        return wrapper

    return decorator
