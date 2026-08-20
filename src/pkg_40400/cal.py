#!/usr/bin/env python3
"""CLI calculator using Click."""

import click


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@click.group()
def cli():
    """CLI calculator for basic arithmetic operations."""


@cli.command(name="add")
@click.option("--a", type=float, required=True, help="First number")
@click.option("--b", type=float, required=True, help="Second number")
def add_cmd(a: float, b: float):
    """Add two numbers."""
    result = add(a, b)
    click.echo(f"{a} + {b} = {result}")


@cli.command(name="subtract")
@click.option("--a", type=float, required=True, help="First number")
@click.option("--b", type=float, required=True, help="Second number")
def subtract_cmd(a: float, b: float):
    """Subtract b from a."""
    result = subtract(a, b)
    click.echo(f"{a} - {b} = {result}")


@cli.command(name="multiply")
@click.option("--a", type=float, required=True, help="First number")
@click.option("--b", type=float, required=True, help="Second number")
def multiply_cmd(a: float, b: float):
    """Multiply two numbers."""
    result = multiply(a, b)
    click.echo(f"{a} * {b} = {result}")


@cli.command(name="divide")
@click.option("--a", type=float, required=True, help="First number")
@click.option("--b", type=float, required=True, help="Second number")
def divide_cmd(a: float, b: float):
    """Divide a by b."""
    try:
        result = divide(a, b)
        click.echo(f"{a} / {b} = {result}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == "__main__":
    cli()
