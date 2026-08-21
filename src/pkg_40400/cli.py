"""
Calculator CLI - Command Line Interface for pkg-40400.

This module provides a CLI interface for the Calculator Service using Click.
"""

import sys

import click

from pkg_40400 import Logger, version
from pkg_40400.services.calculator import (
    add as calc_add,
    divide as calc_divide,
    multiply as calc_multiply,
    subtract as calc_subtract,
)


@click.group()
@click.version_option(version=version, prog_name="pkg-40400")
def main() -> None:
    """
    pkg-40400 - A CLI-based calculator service.

    Commands:
      add      Add two numbers
      subtract Subtract two numbers
      multiply Multiply two numbers
      divide   Divide two numbers
    """
    Logger.info(f"Calculator version: {version}")


@main.command()
@click.argument("a", type=str)
@click.argument("b", type=str)
def add(a: str, b: str) -> None:
    """
    Add two numbers A and B.

    Example:
        pkg-40400 add 5.0 3.0
    """
    try:
        float_a = float(a)
        float_b = float(b)
        result = calc_add(float_a, float_b)
        Logger.info(f"Result: {a} + {b} = {result}")
    except ValueError:
        Logger.error("Invalid input: both arguments must be numeric")
        sys.exit(1)


@main.command()
@click.argument("a", type=str)
@click.argument("b", type=str)
def subtract(a: str, b: str) -> None:
    """
    Subtract B from A.

    Example:
        pkg-40400 subtract 5.0 3.0
    """
    try:
        float_a = float(a)
        float_b = float(b)
        result = calc_subtract(float_a, float_b)
        Logger.info(f"Result: {a} - {b} = {result}")
    except ValueError:
        Logger.error("Invalid input: both arguments must be numeric")
        sys.exit(1)


@main.command()
@click.argument("a", type=str)
@click.argument("b", type=str)
def multiply(a: str, b: str) -> None:
    """
    Multiply two numbers A and B.

    Example:
        pkg-40400 multiply 5.0 3.0
    """
    try:
        float_a = float(a)
        float_b = float(b)
        result = calc_multiply(float_a, float_b)
        Logger.info(f"Result: {a} * {b} = {result}")
    except ValueError:
        Logger.error("Invalid input: both arguments must be numeric")
        sys.exit(1)


@main.command()
@click.argument("a", type=str)
@click.argument("b", type=str)
def divide(a: str, b: str) -> None:
    """
    Divide A by B.

    Example:
        pkg-40400 divide 6.0 3.0
    """
    try:
        float_a = float(a)
        float_b = float(b)
        result = calc_divide(float_a, float_b)
        Logger.info(f"Result: {a} / {b} = {result}")
    except ValueError:
        Logger.error("Invalid input: both arguments must be numeric")
        sys.exit(1)
    except ZeroDivisionError as err:
        Logger.error(err)
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
