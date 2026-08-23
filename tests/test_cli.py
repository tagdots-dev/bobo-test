"""
Integration tests for the CLI entry point.

Tests the Click CLI interface using CliRunner.
Covers all commands: add, subtract, multiply, divide, and --help.
"""

import logging

import pytest
from click.testing import CliRunner

from pkg_40400.cli import main


@pytest.fixture
def runner() -> CliRunner:
    """Provide a Click CliRunner instance."""
    return CliRunner()


class TestHelp:
    """Tests for --help output."""

    def test_main_help(self, runner: CliRunner) -> None:
        """WHEN --help is executed THEN the help menu is displayed."""
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "pkg-40400" in result.output

    def test_add_help(self, runner: CliRunner) -> None:
        """WHEN add --help is executed THEN the help menu for add is displayed."""
        result = runner.invoke(main, ["add", "--help"])
        assert result.exit_code == 0
        assert "--a" in result.output
        assert "--b" in result.output

    def test_subtract_help(self, runner: CliRunner) -> None:
        """WHEN subtract --help is executed THEN the help menu for subtract is displayed."""
        result = runner.invoke(main, ["subtract", "--help"])
        assert result.exit_code == 0
        assert "--a" in result.output
        assert "--b" in result.output

    def test_multiply_help(self, runner: CliRunner) -> None:
        """WHEN multiply --help is executed THEN the help menu for multiply is displayed."""
        result = runner.invoke(main, ["multiply", "--help"])
        assert result.exit_code == 0
        assert "--a" in result.output
        assert "--b" in result.output

    def test_divide_help(self, runner: CliRunner) -> None:
        """WHEN divide --help is executed THEN the help menu for divide is displayed."""
        result = runner.invoke(main, ["divide", "--help"])
        assert result.exit_code == 0
        assert "--a" in result.output
        assert "--b" in result.output


class TestAdd:
    """Integration tests for the add command."""

    def test_add_success(self, runner: CliRunner, caplog: pytest.LogCaptureFixture) -> None:
        """WHEN user executes add with valid inputs THEN result is logged."""
        with caplog.at_level(logging.INFO):
            result = runner.invoke(main, ["add", "--a", "2.0", "--b", "3.0"])
            assert result.exit_code == 0
            assert any("2.0 + 3.0 = 5.0" in record.message for record in caplog.records)

    def test_add_missing_options(self, runner: CliRunner) -> None:
        """IF click fails to parse user input (missing options) THEN error is logged and exit(1)."""
        result = runner.invoke(main, ["add"])
        assert result.exit_code == 2  # Click returns 2 for missing required args


class TestSubtract:
    """Integration tests for the subtract command."""

    def test_subtract_success(self, runner: CliRunner, caplog: pytest.LogCaptureFixture) -> None:
        """WHEN user executes subtract with valid inputs THEN result is logged."""
        with caplog.at_level(logging.INFO):
            result = runner.invoke(main, ["subtract", "--a", "5.0", "--b", "3.0"])
            assert result.exit_code == 0
            assert any("5.0 - 3.0 = 2.0" in record.message for record in caplog.records)

    def test_subtract_missing_options(self, runner: CliRunner) -> None:
        """IF click fails to parse user input (missing options) THEN error is logged and exit(1)."""
        result = runner.invoke(main, ["subtract"])
        assert result.exit_code == 2


class TestMultiply:
    """Integration tests for the multiply command."""

    def test_multiply_success(self, runner: CliRunner, caplog: pytest.LogCaptureFixture) -> None:
        """WHEN user executes multiply with valid inputs THEN result is logged."""
        with caplog.at_level(logging.INFO):
            result = runner.invoke(main, ["multiply", "--a", "2.0", "--b", "3.0"])
            assert result.exit_code == 0
            assert any("2.0 * 3.0 = 6.0" in record.message for record in caplog.records)

    def test_multiply_missing_options(self, runner: CliRunner) -> None:
        """IF click fails to parse user input (missing options) THEN error is logged and exit(1)."""
        result = runner.invoke(main, ["multiply"])
        assert result.exit_code == 2


class TestDivide:
    """Integration tests for the divide command."""

    def test_divide_success(self, runner: CliRunner, caplog: pytest.LogCaptureFixture) -> None:
        """WHEN user executes divide with valid inputs THEN result is logged."""
        with caplog.at_level(logging.INFO):
            result = runner.invoke(main, ["divide", "--a", "6.0", "--b", "3.0"])
            assert result.exit_code == 0
            assert any("6.0 / 3.0 = 2.0" in record.message for record in caplog.records)

    def test_divide_by_zero(self, runner: CliRunner, caplog: pytest.LogCaptureFixture) -> None:
        """IF divisor is zero THEN ZeroDivisionError is caught, logged, and exit(1)."""
        with caplog.at_level(logging.ERROR):
            result = runner.invoke(main, ["divide", "--a", "5.0", "--b", "0.0"])
            assert result.exit_code == 1
            assert any("Error in divide" in record.message for record in caplog.records)

    def test_divide_missing_options(self, runner: CliRunner) -> None:
        """IF click fails to parse user input (missing options) THEN error is logged and exit(1)."""
        result = runner.invoke(main, ["divide"])
        assert result.exit_code == 2
