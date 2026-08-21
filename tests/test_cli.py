"""
CLI Tests - Integration tests for pkg-40400 calculator CLI
"""
import pytest
import json
from click.testing import CliRunner
from pkg_40400.cli import main


@pytest.fixture
def cli_runner():
    """Create a Click test runner."""
    return CliRunner()


class TestCalculatorCLI:
    """Test the calculator CLI commands."""

    def test_cli_addition(self, cli_runner):
        """Test basic addition."""
        result = cli_runner.invoke(main, ["add", "--a", "5", "--b", "3"])
        assert result.exit_code == 0
        assert "5.0 + 3.0 = 8.0" in result.output

    def test_cli_subtraction(self, cli_runner):
        """Test basic subtraction."""
        result = cli_runner.invoke(main, ["subtract", "--a", "10", "--b", "4"])
        assert result.exit_code == 0
        assert "10.0 - 4.0 = 6.0" in result.output

    def test_cli_multiplication(self, cli_runner):
        """Test basic multiplication."""
        result = cli_runner.invoke(main, ["multiply", "--a", "2", "--b", "3"])
        assert result.exit_code == 0
        assert "2.0 * 3.0 = 6.0" in result.output

    def test_cli_division(self, cli_runner):
        """Test basic division."""
        result = cli_runner.invoke(main, ["divide", "--a", "10", "--b", "2"])
        assert result.exit_code == 0
        assert "10.0 / 2.0 = 5.0" in result.output

    def test_cli_negative_numbers(self, cli_runner):
        """Test negative number operations."""
        result = cli_runner.invoke(main, ["add", "--a", "-5", "--b", "-3"])
        assert result.exit_code == 0
        assert "-5.0 + -3.0 = -8.0" in result.output

    def test_cli_decimal_numbers(self, cli_runner):
        """Test decimal number operations."""
        result = cli_runner.invoke(main, ["add", "--a", "5.5", "--b", "3.2"])
        assert result.exit_code == 0
        assert "5.5 + 3.2 = 8.7" in result.output

    def test_cli_missing_arguments(self, cli_runner):
        """Test missing arguments raises error."""
        result = cli_runner.invoke(main, ["add", "--a", "5"])
        assert result.exit_code != 0
        assert "Missing option" in result.output or "No such option" in result.output

    def test_cli_invalid_input(self, cli_runner):
        """Test invalid input raises error."""
        result = cli_runner.invoke(main, ["add", "--a", "abc", "--b", "3"])
        assert result.exit_code != 0
        assert "Invalid input" in result.output

    def test_cli_division_by_zero(self, cli_runner):
        """Test division by zero raises error."""
        result = cli_runner.invoke(main, ["divide", "--a", "10", "--b", "0"])
        assert result.exit_code != 0
        assert "Division by zero is not allowed" in result.output

    def test_cli_precision(self, cli_runner):
        """Test precision flag."""
        result = cli_runner.invoke(main, ["add", "--a", "5", "--b", "3", "--precision", "2"])
        assert result.exit_code == 0
        assert "8.00" in result.output

    def test_cli_json_output(self, cli_runner):
        """Test JSON output format."""
        result = cli_runner.invoke(main, ["add", "--a", "5", "--b", "3", "--json"])
        assert result.exit_code == 0
        output = json.loads(result.output.strip())
        assert output["operation"] == "add"
        assert output["operand_a"] == 5.0
        assert output["operand_b"] == 3.0
        assert output["result"] == 8.0

    # Edge Cases
    def test_cli_zero_addend(self, cli_runner):
        """Test adding zero."""
        result = cli_runner.invoke(main, ["add", "--a", "5", "--b", "0"])
        assert result.exit_code == 0
        assert "5.0" in result.output

    def test_cli_both_zeros(self, cli_runner):
        """Test adding two zeros."""
        result = cli_runner.invoke(main, ["add", "--a", "0", "--b", "0"])
        assert result.exit_code == 0
        assert "0.0" in result.output

    def test_cli_negative_result(self, cli_runner):
        """Test subtraction resulting in negative."""
        result = cli_runner.invoke(main, ["subtract", "--a", "3", "--b", "10"])
        assert result.exit_code == 0
        assert "-7.0" in result.output

    def test_cli_negative_number_input(self, cli_runner):
        """Test negative number input."""
        result = cli_runner.invoke(main, ["add", "--a", "-5", "--b", "-3"])
        assert result.exit_code == 0
        assert "-8.0" in result.output

    def test_cli_decimal_result(self, cli_runner):
        """Test decimal result."""
        result = cli_runner.invoke(main, ["divide", "--a", "10", "--b", "4"])
        assert result.exit_code == 0
        assert "2.5" in result.output

    def test_cli_large_numbers(self, cli_runner):
        """Test large numbers."""
        result = cli_runner.invoke(main, ["add", "--a", "1000000", "--b", "2000000"])
        assert result.exit_code == 0
        assert "3000000.0" in result.output

    def test_cli_small_decimals(self, cli_runner):
        """Test small decimals."""
        result = cli_runner.invoke(main, ["add", "--a", "0.0001", "--b", "0.0002"])
        assert result.exit_code == 0
        assert "0.0003" in result.output

    def test_cli_precision_zero(self, cli_runner):
        """Test precision with zero."""
        result = cli_runner.invoke(main, ["add", "--a", "5", "--b", "3", "--precision", "0"])
        assert result.exit_code == 0
        assert "8" in result.output

    def test_cli_precision_high(self, cli_runner):
        """Test high precision."""
        result = cli_runner.invoke(main, ["add", "--a", "1.123456789", "--b", "2.987654321", "--precision", "10"])
        assert result.exit_code == 0
        assert "4.11111111" in result.output

    def test_cli_invalid_input_subtract(self, cli_runner):
        """Test invalid input for subtraction."""
        result = cli_runner.invoke(main, ["subtract", "--a", "abc", "--b", "3"])
        assert result.exit_code != 0
        assert "Invalid input" in result.output or result.exit_code != 0

    def test_cli_invalid_input_multiply(self, cli_runner):
        """Test invalid input for multiplication."""
        result = cli_runner.invoke(main, ["multiply", "--a", "abc", "--b", "3"])
        assert result.exit_code != 0
        assert "Invalid input" in result.output or result.exit_code != 0

    def test_cli_invalid_input_divide(self, cli_runner):
        """Test invalid input for division."""
        result = cli_runner.invoke(main, ["divide", "--a", "abc", "--b", "3"])
        assert result.exit_code != 0
        assert "Invalid input" in result.output or result.exit_code != 0

    def test_cli_empty_string_input(self, cli_runner):
        """Test empty string input."""
        result = cli_runner.invoke(main, ["add", "--a", "", "--b", "3"])
        assert result.exit_code != 0

    def test_cli_missing_a_arg(self, cli_runner):
        """Test missing --a argument."""
        result = cli_runner.invoke(main, ["add", "--b", "3"])
        assert result.exit_code != 0
        assert "Missing option" in result.output or "No such option" in result.output

    def test_cli_missing_b_arg(self, cli_runner):
        """Test missing --b argument."""
        result = cli_runner.invoke(main, ["add", "--a", "5"])
        assert result.exit_code != 0
        assert "Missing option" in result.output or "No such option" in result.output

    def test_cli_missing_operation(self, cli_runner):
        """Test missing operation."""
        result = cli_runner.invoke(main, ["--a", "5", "--b", "3"])
        assert result.exit_code != 0
        assert "Missing option" in result.output or "No such option" in result.output

    def test_cli_add_negative_result(self, cli_runner):
        """Test addition resulting in negative."""
        result = cli_runner.invoke(main, ["add", "--a", "-15", "--b", "5"])
        assert result.exit_code == 0
        assert "-10.0" in result.output

    def test_cli_help(self, cli_runner):
        """Test help command outputs usage information."""
        result = cli_runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "pkg-40400" in result.output
        assert "add" in result.output
        assert "subtract" in result.output
        assert "multiply" in result.output
        assert "divide" in result.output
