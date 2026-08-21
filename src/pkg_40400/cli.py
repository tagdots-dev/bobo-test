"""
Main CLI entry point with subcommands.
"""

import click

from pkg_40400 import Logger, version
from pkg_40400.arithmetic import calculate
from pkg_40400.logical import evaluate, validate_single_input


@click.group()
def main() -> None:
    """Calculator CLI application"""
    Logger.info(f"Calculator version: {version}")


@main.command()
@click.option(
    "--first",
    "-f",
    required=True,
    type=float,
    help="The first float operand",
)
@click.option(
    "--second",
    "-s",
    required=True,
    type=float,
    help="The second float operand",
)
@click.option(
    "--operation",
    "-o",
    required=True,
    type=click.Choice(["+", "-", "*", "/"], case_sensitive=True),
    help="The operation to perform (+, -, *, /)",
)
def arithmetic(first: float, second: float, operation: str) -> None:
    """
    Perform arithmetic operation on two float values.

    The calculator accepts two float inputs and an operation, then displays
    the result. Division by zero is handled gracefully with an error message.
    """
    Logger.info(f"Operation: {first} {operation} {second}")

    try:
        result = calculate(first, second, operation)
        Logger.info(f"Result: {result}")
    except ZeroDivisionError:
        Logger.error("Error: Cannot divide by zero")
        raise click.exceptions.Exit(code=1)


@main.command()
@click.argument("input_value", type=str, nargs=1)
def logical(input_value: str) -> None:
    """
    Evaluate if an input string contains only valid characters.

    Valid characters are: a-z, A-Z, 0-9, period (.), and hyphen (-).

    INPUT_VALUE is the single string to evaluate.
    """
    validated_input = validate_single_input([input_value])
    Logger.info(f"Input value: {validated_input}")

    result = evaluate(validated_input)
    Logger.info(f"Result: {result}")


if __name__ == "__main__":  # pragma: no cover
    main()
