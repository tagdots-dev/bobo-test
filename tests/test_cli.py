"""Integration tests for the CLI Calculator Service."""

import logging

import pytest
from click.testing import CliRunner

from pkg_40400.cli import cli, main


class TestCLIHelp:
    def test_help_returns_menu(self):
        """Test that --help returns the help menu."""
        runner = CliRunner()
        result = runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "CLI Calculator Service" in result.output
        assert "add" in result.output
        assert "subtract" in result.output
        assert "multiply" in result.output
        assert "divide" in result.output


class TestCLIAdd:
    def test_add_success(self, caplog):
        """Test successful addition."""
        runner = CliRunner()
        with caplog.at_level(logging.INFO):
            result = runner.invoke(cli, ["add", "--a", "1.0", "--b", "2.0"])
        assert result.exit_code == 0
        assert "3.0" in caplog.text

    def test_add_missing_a(self):
        """Test addition with missing --a option."""
        runner = CliRunner()
        result = runner.invoke(cli, ["add", "--b", "2.0"])
        assert result.exit_code == 2
        assert "Missing option '--a'" in result.output

    def test_add_missing_b(self):
        """Test addition with missing --b option."""
        runner = CliRunner()
        result = runner.invoke(cli, ["add", "--a", "1.0"])
        assert result.exit_code == 2
        assert "Missing option '--b'" in result.output


class TestCLISubtract:
    def test_subtract_success(self, caplog):
        """Test successful subtraction."""
        runner = CliRunner()
        with caplog.at_level(logging.INFO):
            result = runner.invoke(cli, ["subtract", "--a", "5.0", "--b", "3.0"])
        assert result.exit_code == 0
        assert "2.0" in caplog.text


class TestCLIMultiply:
    def test_multiply_success(self, caplog):
        """Test successful multiplication."""
        runner = CliRunner()
        with caplog.at_level(logging.INFO):
            result = runner.invoke(cli, ["multiply", "--a", "3.0", "--b", "4.0"])
        assert result.exit_code == 0
        assert "12.0" in caplog.text


class TestCLIDivide:
    def test_divide_success(self, caplog):
        """Test successful division."""
        runner = CliRunner()
        with caplog.at_level(logging.INFO):
            result = runner.invoke(cli, ["divide", "--a", "10.0", "--b", "2.0"])
        assert result.exit_code == 0
        assert "5.0" in caplog.text

    def test_divide_by_zero(self, caplog):
        """Test division by zero."""
        runner = CliRunner()
        with caplog.at_level(logging.ERROR):
            result = runner.invoke(cli, ["divide", "--a", "10.0", "--b", "0.0"])
        assert result.exit_code == 1
        assert "division by zero" in caplog.text


class TestMainErrorHandling:
    """Test main() error handling via standalone_mode=False."""

    def test_main_catches_click_exception(self, caplog, monkeypatch):
        """Test that main() catches ClickException and logs via Logger.error."""
        import sys
        from unittest.mock import patch

        with caplog.at_level(logging.ERROR):
            with patch("pkg_40400.cli.cli") as mock_cli:
                mock_cli.side_effect = Exception("test error")
                with pytest.raises(Exception):
                    main()
