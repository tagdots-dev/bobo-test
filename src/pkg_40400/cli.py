"""
Project Script
"""

import sys

import click

from pkg_40400 import (
    Logger,
    add as add_,
    divide as divide_,
    multiply as multiply_,
    subtract as subtract_,
    version,
)


@click.group()
def main() -> None:
    """pkg-40400 CLI - Calculator Service"""
    pass


@main.command()
@click.option("--a", required=True, type=float, help="First number")
@click.option("--b", required=True, type=float, help="Second number")
def add(a: float, b: float) -> None:
    """Add two numbers"""
    try:
        result = add_(a, b)
        Logger.info(f"add({a}, {b}) = {result}")
    except Exception as e:  # pragma: no cover
        Logger.error(str(e))
        sys.exit(1)


@main.command()
@click.option("--a", required=True, type=float, help="First number")
@click.option("--b", required=True, type=float, help="Second number")
def subtract(a: float, b: float) -> None:
    """Subtract b from a"""
    try:
        result = subtract_(a, b)
        Logger.info(f"subtract({a}, {b}) = {result}")
    except Exception as e:  # pragma: no cover
        Logger.error(str(e))
        sys.exit(1)


@main.command()
@click.option("--a", required=True, type=float, help="First number")
@click.option("--b", required=True, type=float, help="Second number")
def multiply(a: float, b: float) -> None:
    """Multiply two numbers"""
    try:
        result = multiply_(a, b)
        Logger.info(f"multiply({a}, {b}) = {result}")
    except Exception as e:  # pragma: no cover
        Logger.error(str(e))
        sys.exit(1)


@main.command()
@click.option("--a", required=True, type=float, help="First number")
@click.option("--b", required=True, type=float, help="Second number")
def divide(a: float, b: float) -> None:
    """Divide a by b"""
    try:
        result = divide_(a, b)
        Logger.info(f"divide({a}, {b}) = {result}")
    except ZeroDivisionError as e:
        Logger.error(str(e))
        sys.exit(1)
    except Exception as e:  # pragma: no cover
        Logger.error(str(e))
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
