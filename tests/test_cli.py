"""
Integration tests for the Calculator CLI.

Tests the CLI interface using Click's CliRunner.
"""

from click.testing import CliRunner

from pkg_40400.cli import main


class TestCalculatorCLI:
    """Tests for the Calculator CLI commands."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_help(self) -> None:
        """Test that --help displays available commands."""
        result = self.runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "add" in result.output
        assert "subtract" in result.output
        assert "multiply" in result.output
        assert "divide" in result.output

    def test_cli_version(self) -> None:
        """Test that --version displays the version."""
        result = self.runner.invoke(main, ["--version"])
        assert result.exit_code == 0
        assert "pkg-40400" in result.output

    def test_add_command_success(self, caplog) -> None:
        """Test the add command with valid inputs."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(main, ["add", "5.0", "3.0"])
            assert result.exit_code == 0
            assert "8.0" in caplog.text

    def test_add_command_with_integers(self, caplog) -> None:
        """Test the add command with integer inputs."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(main, ["add", "5", "3"])
            assert result.exit_code == 0
            assert "8.0" in caplog.text

    def test_subtract_command_success(self, caplog) -> None:
        """Test the subtract command with valid inputs."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(main, ["subtract", "10.0", "3.0"])
            assert result.exit_code == 0
            assert "7.0" in caplog.text

    def test_multiply_command_success(self, caplog) -> None:
        """Test the multiply command with valid inputs."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(main, ["multiply", "4.0", "5.0"])
            assert result.exit_code == 0
            assert "20.0" in caplog.text

    def test_divide_command_success(self, caplog) -> None:
        """Test the divide command with valid inputs."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(main, ["divide", "10.0", "2.0"])
            assert result.exit_code == 0
            assert "5.0" in caplog.text

    def test_divide_by_zero(self, caplog) -> None:
        """Test that dividing by zero exits with status code 1."""
        with caplog.at_level("ERROR"):
            result = self.runner.invoke(main, ["divide", "10.0", "0.0"])
            assert result.exit_code == 1
            assert "Division by zero" in caplog.text

    def test_invalid_input_for_add(self) -> None:
        """Test that invalid input causes error."""
        result = self.runner.invoke(main, ["add", "abc", "3.0"])
        assert result.exit_code == 1

    def test_invalid_input_for_subtract(self) -> None:
        """Test that invalid input causes error for subtract."""
        result = self.runner.invoke(main, ["subtract", "10.0", "xyz"])
        assert result.exit_code == 1

    def test_invalid_input_for_multiply(self) -> None:
        """Test that invalid input causes error for multiply."""
        result = self.runner.invoke(main, ["multiply", "abc", "def"])
        assert result.exit_code == 1

    def test_invalid_input_for_divide(self) -> None:
        """Test that invalid input causes error for divide."""
        result = self.runner.invoke(main, ["divide", "10.0", "xyz"])
        assert result.exit_code == 1

    def test_missing_arguments(self) -> None:
        """Test that missing arguments causes error (exit code 2 for click usage error)."""
        result = self.runner.invoke(main, ["add", "5.0"])
        assert result.exit_code == 2

    def test_unrecognized_command(self) -> None:
        """Test that unrecognized commands exit with status code 2 (click usage error)."""
        result = self.runner.invoke(main, ["unknown-cmd"])
        assert result.exit_code == 2
