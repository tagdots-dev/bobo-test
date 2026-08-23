"""CLI entry point for pkg-40400 Calculator Service."""

import sys

import click

from pkg_40400 import (
    Logger,
    add as calc_add,
    subtract as calc_sub,
    multiply as calc_mul,
    divide as calc_div,
)


@click.group()
def cli():
    """CLI Calculator Service."""


@cli.command(name="add")
@click.option("--a", required=True, type=float)
@click.option("--b", required=True, type=float)
def add_cmd(a: float, b: float) -> None:
    """Add two numbers."""
    result = calc_add(a, b)
    Logger.info(f"{a} + {b} = {result}")


@cli.command(name="subtract")
@click.option("--a", required=True, type=float)
@click.option("--b", required=True, type=float)
def subtract_cmd(a: float, b: float) -> None:
    """Subtract two numbers."""
    result = calc_sub(a, b)
    Logger.info(f"{a} - {b} = {result}")


@cli.command(name="multiply")
@click.option("--a", required=True, type=float)
@click.option("--b", required=True, type=float)
def multiply_cmd(a: float, b: float) -> None:
    """Multiply two numbers."""
    result = calc_mul(a, b)
    Logger.info(f"{a} * {b} = {result}")


@cli.command(name="divide")
@click.option("--a", required=True, type=float)
@click.option("--b", required=True, type=float)
def divide_cmd(a: float, b: float) -> None:
    """Divide two numbers."""
    try:
        result = calc_div(a, b)
        Logger.info(f"{a} / {b} = {result}")
    except ZeroDivisionError as e:
        Logger.error(str(e))
        sys.exit(1)


def main() -> None:
    """Main entry point."""
    try:
        cli(standalone_mode=False)
    except (click.ClickException, ZeroDivisionError) as e:
        Logger.error(str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
