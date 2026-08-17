"""
Unit Test
"""

import pytest

from pkg_40400.core.decorator import ClsFalseError, raise_on_false


def test_decorator_returns_true():
    """
    validate that return_true function causes result is True
    """

    @raise_on_false()
    def returns_true():
        return True

    result = returns_true()
    assert result is True


def test_decorator_return_false_default_exception():
    """
    validate that return_false function causes result is False
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
    validate that raise_on_false with custom_message is used in the exception message with enable_log=True
    """

    @raise_on_false(ClsFalseError, custom_message="black jack")
    def return_false(enable_log: bool = False):
        return False

    with pytest.raises(ClsFalseError) as exc_info:
        return_false(enable_log=True)

    assert "black jack" in str(exc_info.value)
