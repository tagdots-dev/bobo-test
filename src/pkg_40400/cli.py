"""CLI entry point for pkg-40400 using click."""

import sys

import click

from pkg_40400 import (
    Logger,
    add,
    divide,
    multiply,
    subtract,
)


@click.group()
def cli():
    """CLI for pkg-40400 calculator service."""
    pass  # pragma: no cover


@cli.command()
@click.option("--a", required=True, type=float, help="First operand (float)")
@click.option("--b", required=True, type=float, help="Second operand (float)")
def add_cmd(a: float, b: float) -> None:
    """Add two numbers: a + b."""
    try:
        result = add(a, b)
        Logger.info(f"{a} + {b} = {result}")
    except Exception as exc:  # pragma: no cover
        Logger.error(f"Error in add: {exc}")
        sys.exit(1)


@cli.command()
@click.option("--a", required=True, type=float, help="First operand (float)")
@click.option("--b", required=True, type=float, help="Second operand (float)")
def subtract_cmd(a: float, b: float) -> None:
    """Subtract two numbers: a - b."""
    try:
        result = subtract(a, b)
        Logger.info(f"{a} - {b} = {result}")
    except Exception as exc:  # pragma: no cover
        Logger.error(f"Error in subtract: {exc}")
        sys.exit(1)


@cli.command()
@click.option("--a", required=True, type=float, help="First operand (float)")
@click.option("--b", required=True, type=float, help="Second operand (float)")
def multiply_cmd(a: float, b: float) -> None:
    """Multiply two numbers: a * b."""
    try:
        result = multiply(a, b)
        Logger.info(f"{a} * {b} = {result}")
    except Exception as exc:  # pragma: no cover
        Logger.error(f"Error in multiply: {exc}")
        sys.exit(1)


@cli.command()
@click.option("--a", required=True, type=float, help="First operand (float)")
@click.option("--b", required=True, type=float, help="Second operand (float)")
def divide_cmd(a: float, b: float) -> None:
    """Divide two numbers: a / b."""
    try:
        result = divide(a, b)
        Logger.info(f"{a} / {b} = {result}")
    except ZeroDivisionError as exc:
        Logger.error(f"Error in divide: {exc}")
        sys.exit(1)
    except Exception as exc:  # pragma: no cover
        Logger.error(f"Unexpected error in divide: {exc}")
        sys.exit(1)


def main() -> None:
    """CLI main entry point."""
    if len(sys.argv) == 1:
        cli(["--help"])
        return
    cli()


if __name__ == "__main__":  # pragma: no cover
    main()
