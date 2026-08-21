"""
Tests for CLI module.
"""

from click.testing import CliRunner

from pkg_40400 import cli


class TestCLIMain:
    """Test cases for CLI main entry point."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_main_entry(self) -> None:
        """Test main CLI entry point."""
        assert callable(cli.main)

    def test_cli_help(self) -> None:
        """Test CLI help command."""
        result = self.runner.invoke(cli.main, ["--help"])
        assert result.exit_code == 0
        assert "pkg-40400 CLI" in result.output
        assert "Commands:" in result.output
        assert "add" in result.output
        assert "subtract" in result.output
        assert "multiply" in result.output
        assert "divide" in result.output

    def test_cli_add_command(self) -> None:
        """Test add command."""
        result = self.runner.invoke(cli.main, ["add", "--a", "5", "--b", "3"])
        assert result.exit_code == 0

    def test_cli_subtract_command(self) -> None:
        """Test subtract command."""
        result = self.runner.invoke(cli.main, ["subtract", "--a", "10", "--b", "4"])
        assert result.exit_code == 0

    def test_cli_multiply_command(self) -> None:
        """Test multiply command."""
        result = self.runner.invoke(cli.main, ["multiply", "--a", "3", "--b", "7"])
        assert result.exit_code == 0

    def test_cli_divide_command(self) -> None:
        """Test divide command."""
        result = self.runner.invoke(cli.main, ["divide", "--a", "20", "--b", "5"])
        assert result.exit_code == 0

    def test_cli_divide_by_zero(self) -> None:
        """Test divide by zero error handling."""
        result = self.runner.invoke(cli.main, ["divide", "--a", "10", "--b", "0"])
        assert result.exit_code == 1

    def test_cli_add_invalid_input(self) -> None:
        """Test add command with invalid input."""
        result = self.runner.invoke(cli.main, ["add", "--a", "invalid", "--b", "5"])
        assert result.exit_code != 0
        assert "Invalid value" in result.output

    def test_cli_add_missing_option(self) -> None:
        """Test add command with missing option."""
        result = self.runner.invoke(cli.main, ["add", "--a", "5"])
        assert result.exit_code != 0
        assert "Missing option" in result.output or "Missing" in result.output

    def test_cli_add_command_logs(self, caplog) -> None:
        """Test that add command logs the result."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(cli.main, ["add", "--a", "5", "--b", "3"])
            assert result.exit_code == 0
            assert "Result: 5.0 + 3.0 = 8.0" in caplog.text

    def test_cli_divide_command_logs(self, caplog) -> None:
        """Test that divide command logs the result."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(cli.main, ["divide", "--a", "10", "--b", "2"])
            assert result.exit_code == 0
            assert "Result: 10.0 / 2.0 = 5.0" in caplog.text

    def test_cli_subtract_command_logs(self, caplog) -> None:
        """Test that subtract command logs the result."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(cli.main, ["subtract", "--a", "10", "--b", "3"])
            assert result.exit_code == 0
            assert "Result: 10.0 - 3.0 = 7.0" in caplog.text

    def test_cli_multiply_command_logs(self, caplog) -> None:
        """Test that multiply command logs the result."""
        with caplog.at_level("INFO"):
            result = self.runner.invoke(cli.main, ["multiply", "--a", "3", "--b", "4"])
            assert result.exit_code == 0
            assert "Result: 3.0 * 4.0 = 12.0" in caplog.text
