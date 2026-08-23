"""
Integration tests for the CLI
"""

import logging

from click.testing import CliRunner

from pkg_40400.cli import main, divide, multiply, subtract


class TestCLIHelp:
    """Tests for CLI help functionality"""

    def test_cli_returns_help(self) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "pkg-40400 CLI - Calculator Service" in result.output
        assert "add" in result.output
        assert "subtract" in result.output
        assert "multiply" in result.output
        assert "divide" in result.output


class TestCLIAdd:
    """Tests for the add command"""

    def test_add_success(self, caplog) -> None:
        runner = CliRunner()
        with caplog.at_level(logging.INFO):
            result = runner.invoke(main, ["add", "--a", "2.0", "--b", "3.0"])
        assert result.exit_code == 0
        assert "add(2.0, 3.0) = 5.0" in caplog.text

    def test_add_missing_option_a(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["add", "--b", "3.0"])
        assert result.exit_code != 0

    def test_add_missing_option_b(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["add", "--a", "2.0"])
        assert result.exit_code != 0

    def test_add_invalid_type_a(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["add", "--a", "invalid", "--b", "3.0"])
        assert result.exit_code != 0

    def test_add_invalid_type_b(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["add", "--a", "2.0", "--b", "invalid"])
        assert result.exit_code != 0


class TestCLISubtract:
    """Tests for the subtract command"""

    def test_subtract_success(self, caplog) -> None:
        runner = CliRunner()
        with caplog.at_level(logging.INFO):
            result = runner.invoke(main, ["subtract", "--a", "5.0", "--b", "3.0"])
        assert result.exit_code == 0
        assert "subtract(5.0, 3.0) = 2.0" in caplog.text

    def test_subtract_missing_option_a(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["subtract", "--b", "3.0"])
        assert result.exit_code != 0

    def test_subtract_missing_option_b(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["subtract", "--a", "5.0"])
        assert result.exit_code != 0


class TestCLIMultiply:
    """Tests for the multiply command"""

    def test_multiply_success(self, caplog) -> None:
        runner = CliRunner()
        with caplog.at_level(logging.INFO):
            result = runner.invoke(main, ["multiply", "--a", "2.0", "--b", "3.0"])
        assert result.exit_code == 0
        assert "multiply(2.0, 3.0) = 6.0" in caplog.text

    def test_multiply_missing_option_a(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["multiply", "--b", "3.0"])
        assert result.exit_code != 0

    def test_multiply_missing_option_b(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["multiply", "--a", "2.0"])
        assert result.exit_code != 0


class TestCLIDivide:
    """Tests for the divide command"""

    def test_divide_success(self, caplog) -> None:
        runner = CliRunner()
        with caplog.at_level(logging.INFO):
            result = runner.invoke(main, ["divide", "--a", "6.0", "--b", "3.0"])
        assert result.exit_code == 0
        assert "divide(6.0, 3.0) = 2.0" in caplog.text

    def test_divide_by_zero_exits_with_error(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["divide", "--a", "5.0", "--b", "0.0"])
        assert result.exit_code == 1

    def test_divide_missing_option_a(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["divide", "--b", "3.0"])
        assert result.exit_code != 0

    def test_divide_missing_option_b(self, caplog) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["divide", "--a", "5.0"])
        assert result.exit_code != 0
