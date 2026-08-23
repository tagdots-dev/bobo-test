"""
CLI Entry Point for pkg-40400 Calculator Service.

Provides command-line interface for arithmetic operations: add, subtract,
multiply, and divide using click.
"""

import sys

import click

from pkg_40400 import (
    Logger,
    add as calc_add,
    divide as calc_divide,
    multiply as calc_multiply,
    subtract as calc_subtract,
    version,
)


@click.group()
def main() -> None:
    """pkg-40400: A CLI calculator service."""
    Logger.info(f"pkg-40400 version {version}")


@main.command("add")
@click.option("--a", required=True, type=float, help="First operand.")
@click.option("--b", required=True, type=float, help="Second operand.")
def add_cmd(a: float, b: float) -> None:
    """Add two numbers."""
    try:
        result = calc_add(a, b)
        Logger.info(f"{a} + {b} = {result}")
    except Exception as e:
        Logger.error(f"Error in add: {e}")
        sys.exit(1)


@main.command("subtract")
@click.option("--a", required=True, type=float, help="First operand (minuend).")
@click.option("--b", required=True, type=float, help="Second operand (subtrahend).")
def subtract_cmd(a: float, b: float) -> None:
    """Subtract two numbers."""
    try:
        result = calc_subtract(a, b)
        Logger.info(f"{a} - {b} = {result}")
    except Exception as e:
        Logger.error(f"Error in subtract: {e}")
        sys.exit(1)


@main.command("multiply")
@click.option("--a", required=True, type=float, help="First operand.")
@click.option("--b", required=True, type=float, help="Second operand.")
def multiply_cmd(a: float, b: float) -> None:
    """Multiply two numbers."""
    try:
        result = calc_multiply(a, b)
        Logger.info(f"{a} * {b} = {result}")
    except Exception as e:
        Logger.error(f"Error in multiply: {e}")
        sys.exit(1)


@main.command("divide")
@click.option("--a", required=True, type=float, help="Dividend.")
@click.option("--b", required=True, type=float, help="Divisor.")
def divide_cmd(a: float, b: float) -> None:
    """Divide two numbers."""
    try:
        result = calc_divide(a, b)
        Logger.info(f"{a} / {b} = {result}")
    except ZeroDivisionError as e:
        Logger.error(f"Error in divide: {e}")
        sys.exit(1)
    except Exception as e:
        Logger.error(f"Error in divide: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
