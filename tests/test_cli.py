import pytest
from click.testing import CliRunner

from pkg_40400.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.parametrize(
    "command,args,expected_output",
    [
        ("add", ["--a", "1.2", "--b", "3.4"], "4.6"),
        ("subtract", ["--a", "5", "--b", "2"], "3.0"),
        ("multiply", ["--a", "2", "--b", "3"], "6.0"),
        ("divide", ["--a", "10", "--b", "4"], "2.5"),
    ],
)
def test_cli_operations(runner, command, args, expected_output):
    result = runner.invoke(cli, [command] + args)
    assert result.exit_code == 0
    # click prints the result on stdout; strip to ignore trailing newline
    assert result.output.strip() == expected_output


def test_cli_divide_by_zero(runner):
    result = runner.invoke(cli, ["divide", "--a", "5", "--b", "0"])
    # click.ClickException results in a non‑zero exit code and prints the error
    assert result.exit_code != 0
    assert "float division by zero" in result.output
