"""CLI entry point for the `pkg-40400` package.

Implements the event‑driven requirements (REQ‑201‑205) using ``click``.
All commands delegate to the pure‑logic Calculator Service and log
success or error outcomes via the shared ``Logger`` (REQ‑103, 301‑304).
"""

from __future__ import annotations

from typing import Callable

import click
from click import Command

from pkg_40400 import (
    Logger,
    add,
    divide,
    multiply,
    subtract,
    version,
)


def _cli_wrapper(operation: Callable[[float, float], float], op_name: str) -> Command:
    """Return a click command that runs *operation* and logs the result.

    Parameters
    ----------
    operation:
        The arithmetic function to invoke.
    op_name:
        Name of the operation (used for the command name and log messages).
    """

    @click.command(name=op_name)
    @click.option("--a", type=click.FLOAT, required=True, help="First operand (float).")
    @click.option("--b", type=click.FLOAT, required=True, help="Second operand (float).")
    def command(a: float, b: float) -> None:
        """Execute the arithmetic operation and log the outcome."""
        try:
            result = operation(a, b)
            Logger.info(f"{op_name}: {a} {op_name} {b} = {result}")
            click.echo(str(result))
        except Exception as exc:  # includes ZeroDivisionError, etc.
            Logger.error(f"{op_name} failed: {exc}")
            # Propagate a ClickException so the CLI exits with a non‑zero code.
            raise click.ClickException(str(exc))

    # ``@click.command`` decorates ``command`` and returns a ``click.Command``
    # instance, which matches the return annotation above.
    return command  # type: ignore[return-value]


@click.group()
@click.version_option(version, prog_name="pkg-40400")
def cli() -> None:
    """Top‑level command group for the Calculator Service."""
    # No additional startup logic required.


# Register arithmetic commands.
cli.add_command(_cli_wrapper(add, "add"))
cli.add_command(_cli_wrapper(subtract, "subtract"))
cli.add_command(_cli_wrapper(multiply, "multiply"))
cli.add_command(_cli_wrapper(divide, "divide"))


def main() -> None:
    """Entry‑point used by ``scripts.pkg-40400`` defined in pyproject.toml."""
    cli(prog_name="pkg-40400")


if __name__ == "__main__":  # pragma: no cover
    # Allows ``python src/pkg_40400/cli.py`` during development.
    main()
