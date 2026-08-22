"""
Integration tests for CLI using CliRunner.
"""

from click.testing import CliRunner

from pkg_40400.cli import main


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "add" in result.output
    assert "subtract" in result.output
    assert "multiply" in result.output
    assert "divide" in result.output


def test_cli_add_success(caplog):
    runner = CliRunner()
    result = runner.invoke(main, ["add", "--a", "2.5", "--b", "3.5"])
    assert result.exit_code == 0
    assert any("add(2.5, 3.5) = 6.0" in record.message for record in caplog.records)


def test_cli_subtract_success(caplog):
    runner = CliRunner()
    result = runner.invoke(main, ["subtract", "--a", "10.0", "--b", "4.0"])
    assert result.exit_code == 0
    assert any("subtract(10.0, 4.0) = 6.0" in record.message for record in caplog.records)


def test_cli_multiply_success(caplog):
    runner = CliRunner()
    result = runner.invoke(main, ["multiply", "--a", "2.5", "--b", "4.0"])
    assert result.exit_code == 0
    assert any("multiply(2.5, 4.0) = 10.0" in record.message for record in caplog.records)


def test_cli_divide_success(caplog):
    runner = CliRunner()
    result = runner.invoke(main, ["divide", "--a", "10.0", "--b", "2.0"])
    assert result.exit_code == 0
    assert any("divide(10.0, 2.0) = 5.0" in record.message for record in caplog.records)


def test_cli_divide_by_zero(caplog):
    runner = CliRunner()
    result = runner.invoke(main, ["divide", "--a", "1.0", "--b", "0.0"])
    assert result.exit_code != 0
    assert any("ZeroDivisionError" in record.message for record in caplog.records)


def test_cli_missing_option():
    runner = CliRunner()
    result = runner.invoke(main, ["add", "--a", "1.0"])
    assert result.exit_code != 0
    assert "Missing option '--b'" in result.output
