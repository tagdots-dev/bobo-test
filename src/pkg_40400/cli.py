"""
Application Entry Point
"""

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
def main() -> None:
    """
    pkg-40400 CLI - A calculator service.
    """
    pass


@main.command()
@click.option("--a", "a_value", type=float, required=True, help="First number")
@click.option("--b", "b_value", type=float, required=True, help="Second number")
def add_cmd(a_value: float, b_value: float) -> None:
    """
    Add two numbers: a + b
    """
    try:
        result = add(a_value, b_value)
        Logger.info(f"Result: {a_value} + {b_value} = {result}")
    except Exception:  # pragma: no cover
        Logger.error("Addition failed")
        sys.exit(1)


@main.command()
@click.option("--a", "a_value", type=float, required=True, help="First number")
@click.option("--b", "b_value", type=float, required=True, help="Second number")
def subtract_cmd(a_value: float, b_value: float) -> None:
    """
    Subtract two numbers: a - b
    """
    try:
        result = subtract(a_value, b_value)
        Logger.info(f"Result: {a_value} - {b_value} = {result}")
    except Exception:  # pragma: no cover
        Logger.error("Subtraction failed")
        sys.exit(1)


@main.command()
@click.option("--a", "a_value", type=float, required=True, help="First number")
@click.option("--b", "b_value", type=float, required=True, help="Second number")
def multiply_cmd(a_value: float, b_value: float) -> None:
    """
    Multiply two numbers: a * b
    """
    try:
        result = multiply(a_value, b_value)
        Logger.info(f"Result: {a_value} * {b_value} = {result}")
    except Exception:  # pragma: no cover
        Logger.error("Multiplication failed")
        sys.exit(1)


@main.command()
@click.option("--a", "a_value", type=float, required=True, help="First number")
@click.option("--b", "b_value", type=float, required=True, help="Second number")
def divide_cmd(a_value: float, b_value: float) -> None:
    """
    Divide two numbers: a / b
    """
    try:
        result = divide(a_value, b_value)
        Logger.info(f"Result: {a_value} / {b_value} = {result}")
    except ZeroDivisionError:
        Logger.error("Division by zero error")
        sys.exit(1)
    except Exception:  # pragma: no cover
        Logger.error("Division failed")
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
