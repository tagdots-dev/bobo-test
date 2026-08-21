"""
Tests for the calculator CLI application.

Tests cover:
- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Float input handling
- Division by zero error handling
- Invalid operation handling
- CLI argument validation
"""

import logging

import pytest
from click.testing import CliRunner

from pkg_40400 import cli
from pkg_40400.arithmetic import calculate


class TestCalculateFunction:
    """Tests for the calculate function."""

    def test_addition_positive_numbers(self) -> None:
        """When adding two positive floats, the function shall return their sum."""
        result = calculate(3.5, 2.5, "+")
        assert result == 6.0

    def test_addition_negative_numbers(self) -> None:
        """When adding negative floats, the function shall return their sum."""
        result = calculate(-3.5, -2.5, "+")
        assert result == -6.0

    def test_addition_mixed_sign(self) -> None:
        """When adding floats with mixed signs, the function shall return correct sum."""
        result = calculate(5.0, -3.0, "+")
        assert result == 2.0

    def test_subtraction_positive_numbers(self) -> None:
        """When subtracting two positive floats, the function shall return their difference."""
        result = calculate(10.5, 3.5, "-")
        assert result == 7.0

    def test_subtraction_negative_result(self) -> None:
        """When subtracting to produce negative result, the function shall handle correctly."""
        result = calculate(3.5, 10.5, "-")
        assert result == -7.0

    def test_multiplication_positive_numbers(self) -> None:
        """When multiplying two positive floats, the function shall return their product."""
        result = calculate(4.0, 3.0, "*")
        assert result == 12.0

    def test_multiplication_negative_numbers(self) -> None:
        """When multiplying negative floats, the function shall return correct product."""
        result = calculate(-4.0, -3.0, "*")
        assert result == 12.0

    def test_multiplication_mixed_sign(self) -> None:
        """When multiplying with mixed signs, the function shall return negative product."""
        result = calculate(-4.0, 3.0, "*")
        assert result == -12.0

    def test_division_positive_numbers(self) -> None:
        """When dividing two positive floats, the function shall return their quotient."""
        result = calculate(10.0, 2.0, "/")
        assert result == 5.0

    def test_division_negative_numbers(self) -> None:
        """When dividing negative floats, the function shall return positive quotient."""
        result = calculate(-10.0, -2.0, "/")
        assert result == 5.0

    def test_division_mixed_sign(self) -> None:
        """When dividing with mixed signs, the function shall return negative quotient."""
        result = calculate(-10.0, 2.0, "/")
        assert result == -5.0

    def test_division_by_zero(self) -> None:
        """If the second operand is zero during division, the function shall raise ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError) as exc_info:
            calculate(10.0, 0.0, "/")
        assert str(exc_info.value) == "Cannot divide by zero"

    def test_division_by_zero_first_operand(self) -> None:
        """When dividing zero by a non-zero float, the function shall return zero."""
        result = calculate(0.0, 5.0, "/")
        assert result == 0.0

    def test_invalid_operation(self) -> None:
        """If an unsupported operation is provided, the function shall raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            calculate(10.0, 5.0, "^")
        assert "Unsupported operation" in str(exc_info.value)

    def test_addition_with_decimals(self) -> None:
        """When adding floats with decimal places, the function shall preserve precision."""
        result = calculate(0.1, 0.2, "+")
        assert result == pytest.approx(0.3)

    def test_large_numbers(self) -> None:
        """When handling large float values, the function shall calculate correctly."""
        result = calculate(1e10, 1e10, "+")
        assert result == 2e10

    def test_small_numbers(self) -> None:
        """When handling small float values, the function shall calculate correctly."""
        result = calculate(1e-10, 1e-10, "+")
        assert result == pytest.approx(2e-10)

    def test_identity_addition(self) -> None:
        """When adding zero, the function shall return the original value."""
        result = calculate(5.5, 0.0, "+")
        assert result == 5.5

    def test_identity_subtraction(self) -> None:
        """When subtracting zero, the function shall return the original value."""
        result = calculate(5.5, 0.0, "-")
        assert result == 5.5

    def test_multiplication_by_zero(self) -> None:
        """When multiplying by zero, the function shall return zero."""
        result = calculate(5.5, 0.0, "*")
        assert result == 0.0

    def test_multiplication_by_one(self) -> None:
        """When multiplying by one, the function shall return the original value."""
        result = calculate(5.5, 1.0, "*")
        assert result == 5.5


class TestArithmeticCLI:
    """Tests for the arithmetic CLI command."""

    @pytest.fixture
    def runner(self) -> CliRunner:
        """Create a CliRunner for testing CLI commands."""
        return CliRunner()

    def test_cli_addition(self, runner: CliRunner, caplog) -> None:
        """When adding two numbers via CLI, the command shall return the sum."""
        result = runner.invoke(cli.main, ["arithmetic", "-f", "10.5", "-s", "3.5", "-o", "+"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: 14.0" in caplog.text

    def test_cli_subtraction(self, runner: CliRunner, caplog) -> None:
        """When subtracting two numbers via CLI, the command shall return the difference."""
        result = runner.invoke(cli.main, ["arithmetic", "-f", "10.5", "-s", "3.5", "-o", "-"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: 7.0" in caplog.text

    def test_cli_multiplication(self, runner: CliRunner, caplog) -> None:
        """When multiplying two numbers via CLI, the command shall return the product."""
        result = runner.invoke(cli.main, ["arithmetic", "-f", "4.0", "-s", "3.0", "-o", "*"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: 12.0" in caplog.text

    def test_cli_division(self, runner: CliRunner, caplog) -> None:
        """When dividing two numbers via CLI, the command shall return the quotient."""
        result = runner.invoke(cli.main, ["arithmetic", "-f", "10.0", "-s", "2.0", "-o", "/"])
        assert result.exit_code == 0
        with caplog.at_level(logging.INFO):
            assert "Result: 5.0" in caplog.text

    def test_cli_division_by_zero(self, runner: CliRunner, caplog) -> None:
        """If dividing by zero via CLI, the command shall return an error."""
        result = runner.invoke(cli.main, ["arithmetic", "-f", "10.0", "-s", "0.0", "-o", "/"])
        assert result.exit_code == 1
        with caplog.at_level(logging.ERROR):
            assert "Error: Cannot divide by zero" in caplog.text

    def test_cli_invalid_operation(self, runner: CliRunner) -> None:
        """If an invalid operation is provided via CLI, the command shall return an error."""
        result = runner.invoke(cli.main, ["arithmetic", "-f", "10.0", "-s", "5.0", "-o", "^"])
        assert result.exit_code == 2
        assert "Invalid value" in result.output or "Invalid value" in str(result.exception)

    def test_cli_missing_first_operand(self, runner: CliRunner) -> None:
        """If the first operand is missing, the command shall return an error."""
        result = runner.invoke(cli.main, ["arithmetic", "-s", "5.0", "-o", "+"])
        assert result.exit_code == 2

    def test_cli_missing_second_operand(self, runner: CliRunner) -> None:
        """If the second operand is missing, the command shall return an error."""
        result = runner.invoke(cli.main, ["arithmetic", "-f", "10.0", "-o", "+"])
        assert result.exit_code == 2

    def test_cli_missing_operation(self, runner: CliRunner) -> None:
        """If the operation is missing, the command shall return an error."""
        result = runner.invoke(cli.main, ["arithmetic", "-f", "10.0", "-s", "5.0"])
        assert result.exit_code == 2
