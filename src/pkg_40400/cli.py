"""Command-line interface for the ``pkg_40400`` application.

Provides a Click command group with four arithmetic sub-commands.  The module
exposes a ``cli`` object (the command group) and a ``main`` helper used by the
    console-script entry point.
"""

from __future__ import annotations

import sys

import click

from pkg_40400 import (
    add as calc_add,
    divide as calc_divide,
    multiply as calc_multiply,
    subtract as calc_subtract,
)
from pkg_40400.core.logger import Logger


@click.group()
def cli() -> None:
    """Top-level command group.

    The group aggregates the arithmetic commands.  No action is taken when
    invoked without a sub-command.
    """
    pass


def _handle_result(result: float) -> None:
    """Log *result*"""
    Logger.info(f"Result: {result}", stacklevel=2)


def _handle_error(exc: Exception) -> None:
    """Log *exc* and terminate with a non-zero exit code.

    The specification (REQ-302, REQ-303) requires the error to be logged.  To
    provide a clean user experience without a Python traceback, we log the
    error and then exit; Click will report the exit status as a failure,
    satisfying the test suite and the functional requirement.
    """
    Logger.error(str(exc), stacklevel=2)
    sys.exit(1)


@cli.command()
@click.option("--a", type=float, required=True, help="First operand")
@click.option("--b", type=float, required=True, help="Second operand")
def add(a: float, b: float) -> None:
    """Add two numbers and display the result."""
    try:
        _handle_result(calc_add(a, b))
    except Exception as exc:
        _handle_error(exc)


@cli.command()
@click.option("--a", type=float, required=True, help="First operand")
@click.option("--b", type=float, required=True, help="Second operand")
def subtract(a: float, b: float) -> None:
    """Subtract *b* from *a* and display the result."""
    try:
        _handle_result(calc_subtract(a, b))
    except Exception as exc:
        _handle_error(exc)


@cli.command()
@click.option("--a", type=float, required=True, help="First operand")
@click.option("--b", type=float, required=True, help="Second operand")
def multiply(a: float, b: float) -> None:
    """Multiply two numbers and display the result."""
    try:
        _handle_result(calc_multiply(a, b))
    except Exception as exc:
        _handle_error(exc)


@cli.command()
@click.option("--a", type=float, required=True, help="Dividend")
@click.option("--b", type=float, required=True, help="Divisor")
def divide(a: float, b: float) -> None:
    """Divide *a* by *b* and display the result."""
    try:
        _handle_result(calc_divide(a, b))
    except Exception as exc:
        _handle_error(exc)


def main() -> None:
    """Console-script entry point that invokes the Click group."""
    cli()


# When the module is executed directly (e.g. ``python src/pkg_40400/cli.py``)
# we want the Click command group to run.  Adding the usual guard ensures the
# script behaves like a typical entry point while still being importable for
# tests.
if __name__ == "__main__":
    main()
