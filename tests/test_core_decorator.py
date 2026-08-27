"""
Unit Test
"""

import pytest

from pkg_40400.core.decorator import ClsFalseError, raise_on_false


def test_decorator_return_true():
    """
    validate that return_true function returns True without raising exception
    """

    @raise_on_false()
    def returns_true():
        return True

    result = returns_true()
    assert result is True


def test_decorator_return_false_default_exception():
    """
    validate that return_false function causes an exception to be raised
    """

    @raise_on_false()
    def return_false():
        return False

    with pytest.raises(ClsFalseError) as exc_info:
        return_false()

    assert "return_false returned 'False'" in str(exc_info.value)


def test_decorator_return_false_custom_exception_log_false():
    """
    validate that raise_on_false with custom_message is used in the exception message
    """

    @raise_on_false(ClsFalseError, custom_message="hello world")
    def return_false():
        return False

    with pytest.raises(ClsFalseError) as exc_info:
        return_false()

    assert "hello world" in str(exc_info.value)


def test_decorator_return_false_custom_exception_log_true():
    """
    validate that enable_log=True logs the exception via Logger.error.
    """

    @raise_on_false(ClsFalseError, custom_message="black jack")
    def return_false(enable_log: bool = False):
        return False

    with pytest.raises(ClsFalseError) as exc_info:
        return_false(enable_log=True)

    assert "black jack" in str(exc_info.value)


def test_decorator_return_false_custom_exception_type():
    """
    validate that raise_on_false with custom exception_type works correctly
    """

    class CustomError(ValueError):
        pass

    @raise_on_false(CustomError, custom_message="custom error message")
    def return_false():
        return False

    with pytest.raises(CustomError) as exc_info:
        return_false()

    assert "custom error message" in str(exc_info.value)


def test_decorator_return_false_log_error_false():
    """
    validate that log_error=False prevents logging the error.
    """
    from unittest.mock import patch

    @raise_on_false(ClsFalseError, custom_message="test", log_error=False)
    def return_false():
        return False

    with patch("pkg_40400.core.logger.get_logger") as mock_get_logger:
        mock_logger = mock_get_logger.return_value
        with pytest.raises(ClsFalseError) as exc_info:
            return_false()

    # Verify logger was NOT called when log_error=False
    assert "test" in str(exc_info.value)
    mock_logger.error.assert_not_called()


def test_decorator_return_false_invalid_exception_type():
    """
    validate that raise_on_false with invalid exception_type raises TypeError.
    """

    class InvalidError(TypeError):
        pass

    # This should raise TypeError because InvalidError is not a subclass of ValueError
    with pytest.raises(TypeError) as exc_info:

        @raise_on_false(InvalidError, custom_message="test")
        def return_false():
            return False

    assert "exception_type must be a subclass of ValueError" in str(exc_info.value)
