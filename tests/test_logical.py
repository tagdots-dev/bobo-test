"""
Tests for the logical CLI application.

Tests cover:
- String validation with valid characters (a-zA-Z0-9.-)
- String validation with invalid characters
- Input constraint validation (exactly one input)
- CLI argument handling
- Edge cases
"""

import logging

import pytest
from click.testing import CliRunner

from pkg_40400.cli import main
from pkg_40400.logical import evaluate, validate_single_input


class TestEvaluateFunction:
    """Tests for the evaluate function."""

    def test_valid_string_alphanumeric(self) -> None:
        """When the user inputs a value with only alphanumeric characters, the function shall return True."""
        result = evaluate("abc123")
        assert result is True

    def test_valid_string_with_period(self) -> None:
        """When the user inputs a value with period characters, the function shall return True."""
        result = evaluate("file.txt")
        assert result is True

    def test_valid_string_with_hyphen(self) -> None:
        """When the user inputs a value with hyphen characters, the function shall return True."""
        result = evaluate("my-file")
        assert result is True

    def test_valid_string_with_mixed_valid_chars(self) -> None:
        """When the user inputs a value with mixed valid characters, the function shall return True."""
        result = evaluate("test-file.name123")
        assert result is True

    def test_valid_string_uppercase(self) -> None:
        """When the user inputs a value with uppercase letters, the function shall return True."""
        result = evaluate("ABC123")
        assert result is True

    def test_valid_string_empty_string(self) -> None:
        """When the user inputs an empty string, the function shall return False."""
        result = evaluate("")
        assert result is False

    def test_invalid_string_with_space(self) -> None:
        """If the input contains a space character, the function shall return False."""
        result = evaluate("hello world")
        assert result is False

    def test_invalid_string_with_special_char(self) -> None:
        """If the input contains special characters, the function shall return False."""
        result = evaluate("hello@world")
        assert result is False

    def test_invalid_string_with_exclamation(self) -> None:
        """If the input contains exclamation marks, the function shall return False."""
        result = evaluate("hello!")
        assert result is False

    def test_invalid_string_with_at_symbol(self) -> None:
        """If the input contains @ symbol, the function shall return False."""
        result = evaluate("user@example.com")
        assert result is False

    def test_invalid_string_with_plus(self) -> None:
        """If the input contains plus sign, the function shall return False."""
        result = evaluate("test+value")
        assert result is False

    def test_invalid_string_with_underscore(self) -> None:
        """If the input contains underscore, the function shall return False."""
        result = evaluate("test_value")
        assert result is False


class TestValidateSingleInputFunction:
    """Tests for the validate_single_input function."""

    def test_single_valid_input(self) -> None:
        """When the user inputs exactly one value, the function shall return that value."""
        result = validate_single_input(["test"])
        assert result == "test"

    def test_single_empty_string(self) -> None:
        """When the user inputs an empty string as the only value, the function shall return it."""
        result = validate_single_input([""])
        assert result == ""

    def test_no_inputs_raises_error(self) -> None:
        """If the user inputs no values, the function shall raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            validate_single_input([])
        assert "No input provided" in str(exc_info.value)

    def test_two_inputs_raises_error(self) -> None:
        """If the user inputs more than one value, the function shall raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            validate_single_input(["first", "second"])
        assert "Too many inputs" in str(exc_info.value)


class TestLogicalCLI:
    """Tests for the logical CLI command."""

    @pytest.fixture
    def runner(self) -> CliRunner:
        """Create a CliRunner for testing CLI commands."""
        return CliRunner()

    def test_cli_single_valid_input(self, runner: CliRunner, caplog) -> None:
        """When the user inputs a valid string, the CLI shall output True."""
        result = runner.invoke(main, ["logical", "valid123"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: True" in caplog.text

    def test_cli_single_invalid_input_with_space(self, runner: CliRunner, caplog) -> None:
        """When the user inputs a string with invalid characters, the CLI shall output False."""
        result = runner.invoke(main, ["logical", "hello world"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: False" in caplog.text

    def test_cli_no_input_raises_error(self, runner: CliRunner) -> None:
        """If the user provides no input, the CLI shall exit with error code 1."""
        result = runner.invoke(main, ["logical"])
        assert result.exit_code != 0

    def test_cli_multiple_inputs_raises_error(self, runner: CliRunner) -> None:
        """If the user provides multiple inputs, the CLI shall reject and display error message."""
        result = runner.invoke(main, ["logical", "first", "second"])
        assert result.exit_code != 0

    def test_cli_input_with_special_char(self, runner: CliRunner, caplog) -> None:
        """When the user inputs a string with special characters, the CLI shall output False."""
        result = runner.invoke(main, ["logical", "test@value"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: False" in caplog.text

    def test_cli_input_with_period(self, runner: CliRunner, caplog) -> None:
        """When the user inputs a string with period, the CLI shall output True."""
        result = runner.invoke(main, ["logical", "file.txt"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: True" in caplog.text

    def test_cli_input_with_hyphen(self, runner: CliRunner, caplog) -> None:
        """When the user inputs a string with hyphen, the CLI shall output True."""
        result = runner.invoke(main, ["logical", "my-file"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: True" in caplog.text

    def test_cli_input_with_complex_valid_string(self, runner: CliRunner, caplog) -> None:
        """When the user inputs a complex valid string, the CLI shall output True."""
        result = runner.invoke(main, ["logical", "test-file.name123"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: True" in caplog.text
