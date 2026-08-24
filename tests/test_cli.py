"""Integration tests for CLI using click.testing.CliRunner."""

import pytest
from click.testing import CliRunner

from pkg_40400.cli import (
    add_cmd,
    cli,
    divide_cmd,
    multiply_cmd,
    subtract_cmd,
)


@pytest.fixture
def runner():
    """Return CliRunner instance."""
    return CliRunner()


def test_cli_help(runner):
    """Test that --help shows usage."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "add " in result.output
    assert "subtract " in result.output
    assert "multiply " in result.output
    assert "divide " in result.output


@pytest.mark.parametrize(
    ("cmd", "expected_cmd_name"),
    [
        (add_cmd, "add "),
        (subtract_cmd, "subtract "),
        (multiply_cmd, "multiply "),
        (divide_cmd, "divide "),
    ],
)
def test_cli_commands_show_help(cmd, expected_cmd_name, runner):
    """Test that each command shows its own help."""
    result = runner.invoke(cmd, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.output
    assert "--a" in result.output
    assert "--b" in result.output


def test_add_command_success(runner, caplog):
    """Test add command with valid inputs."""
    with caplog.at_level("INFO"):
        result = runner.invoke(add_cmd, ["--a", "1.5", "--b", "2.5"])
    assert result.exit_code == 0
    assert any("1.5 + 2.5 = 4.0" in record.message for record in caplog.records)


def test_subtract_command_success(runner, caplog):
    """Test subtract command with valid inputs."""
    with caplog.at_level("INFO"):
        result = runner.invoke(subtract_cmd, ["--a", "5.0", "--b", "3.0"])
    assert result.exit_code == 0
    assert any("5.0 - 3.0 = 2.0" in record.message for record in caplog.records)


def test_multiply_command_success(runner, caplog):
    """Test multiply command with valid inputs."""
    with caplog.at_level("INFO"):
        result = runner.invoke(multiply_cmd, ["--a", "2.0", "--b", "3.0"])
    assert result.exit_code == 0
    assert any("2.0 * 3.0 = 6.0" in record.message for record in caplog.records)


def test_divide_command_success(runner, caplog):
    """Test divide command with valid inputs."""
    with caplog.at_level("INFO"):
        result = runner.invoke(divide_cmd, ["--a", "6.0", "--b", "2.0"])
    assert result.exit_code == 0
    assert any("6.0 / 2.0 = 3.0" in record.message for record in caplog.records)


def test_divide_by_zero_error(runner, caplog):
    """Test divide command with zero divisor."""
    with caplog.at_level("ERROR"):
        result = runner.invoke(divide_cmd, ["--a", "1.0", "--b", "0.0"])
    assert result.exit_code == 1
    assert any("division by zero" in record.message for record in caplog.records)


def test_missing_required_option(runner, caplog):
    """Test that missing required option exits with error."""
    with caplog.at_level("ERROR"):
        result = runner.invoke(add_cmd, ["--a", "1.0"])
    assert result.exit_code == 2  # click's exit code for usage error
    assert "Missing option" in result.output


def test_invalid_type(runner, caplog):
    """Test that non-float input raises validation error."""
    with caplog.at_level("ERROR"):
        result = runner.invoke(add_cmd, ["--a", "not_a_number", "--b", "2.0"])
    assert result.exit_code == 2
    assert "Invalid value" in result.output


def test_rounding_behavior(runner, caplog):
    """Test that results are rounded to 4 decimal places."""
    with caplog.at_level("INFO"):
        result = runner.invoke(add_cmd, ["--a", "1.11115", "--b", "0.0"])
    assert result.exit_code == 0
    assert any("1.11115 + 0.0 = 1.1112" in record.message for record in caplog.records)
