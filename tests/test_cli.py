"""Integration tests for the CLI built with ``click``.

The tests use :class:`click.testing.CliRunner` to invoke each arithmetic command
with ``--a`` and ``--b`` options.  The ``caplog`` fixture captures the messages
sent to the shared ``Logger`` instance so we can assert that ``Logger.info`` is
used for successful results and ``Logger.error`` for failure cases (division by
zero).
"""

import pytest
from click.testing import CliRunner

from pkg_40400 import Logger, cli


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.mark.parametrize(
    "command, a, b, expected",
    [
        ("add", 1.0, 2.0, "3.0"),
        ("subtract", 5.0, 3.0, "2.0"),
        ("multiply", 2.0, 4.0, "8.0"),
        ("divide", 6.0, 3.0, "2.0"),
    ],
)
def test_cli_success(runner: CliRunner, command: str, a: float, b: float, expected: str, caplog) -> None:
    # Ensure logger captures info level messages.
    caplog.set_level("INFO", logger=Logger.name)
    result = runner.invoke(cli, [command, "--a", str(a), "--b", str(b)])
    assert result.exit_code == 0
    # Verify that an info log containing the result was emitted.
    assert any("Result:" in record.message for record in caplog.records)


def test_cli_divide_by_zero(runner: CliRunner, caplog) -> None:
    caplog.set_level("ERROR", logger=Logger.name)
    result = runner.invoke(cli, ["divide", "--a", "1", "--b", "0"])
    # The CLI logs the error and exits with a non‑zero status.
    assert result.exit_code != 0
    # Ensure an error log was produced.
    assert any(record.levelname == "ERROR" for record in caplog.records)
