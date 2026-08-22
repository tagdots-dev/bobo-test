"""
CLI entrypoint for pkg-40400 — Calculator service via click.
"""

import sys

import click

from pkg_40400 import (
    Logger,
    add,
    divide,
    multiply,
    subtract,
    version,
)


@click.group()
def main() -> None:
    """CLI for pkg-40400 Calculator Service."""
    Logger.info(f"pkg-40400 v{version} initialized.")


@main.command(name="add")
@click.option("--a", required=True, type=float, help="First operand")
@click.option("--b", required=True, type=float, help="Second operand")
def add_command(a: float, b: float) -> None:
    """Add two numbers."""
    try:
        result = add(a, b)
        Logger.info(f"add({a}, {b}) = {result}")
    except Exception as e:  # pragma: no cover
        Logger.error(f"Error in add({a}, {b}): {e}")
        sys.exit(1)


@main.command(name="subtract")
@click.option("--a", required=True, type=float, help="First operand")
@click.option("--b", required=True, type=float, help="Second operand")
def subtract_command(a: float, b: float) -> None:
    """Subtract b from a."""
    try:
        result = subtract(a, b)
        Logger.info(f"subtract({a}, {b}) = {result}")
    except Exception as e:  # pragma: no cover
        Logger.error(f"Error in subtract({a}, {b}): {e}")
        sys.exit(1)


@main.command(name="multiply")
@click.option("--a", required=True, type=float, help="First operand")
@click.option("--b", required=True, type=float, help="Second operand")
def multiply_command(a: float, b: float) -> None:
    """Multiply two numbers."""
    try:
        result = multiply(a, b)
        Logger.info(f"multiply({a}, {b}) = {result}")
    except Exception as e:  # pragma: no cover
        Logger.error(f"Error in multiply({a}, {b}): {e}")
        sys.exit(1)


@main.command(name="divide")
@click.option("--a", required=True, type=float, help="First operand")
@click.option("--b", required=True, type=float, help="Second operand")
def divide_command(a: float, b: float) -> None:
    """Divide a by b."""
    try:
        result = divide(a, b)
        Logger.info(f"divide({a}, {b}) = {result}")
    except ZeroDivisionError as e:
        Logger.error(f"ZeroDivisionError: {e}")
        sys.exit(1)
    except Exception as e:  # pragma: no cover
        Logger.error(f"Error in divide({a}, {b}): {e}")
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
