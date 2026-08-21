"""
Calculator CLI - Command-line interface for pkg-40400 calculator service
"""

import click
import json

from pkg_40400 import (
    Calculator,
    DivisionByZeroError,
    InvalidInputError,
    Logger,
    version,
)


def _validate_and_convert(value: str, param_name: str) -> float:
    """
    Validate and convert string input to float.
    
    Args:
        value: The string value to convert
        param_name: Name of the parameter for error messages
        
    Returns:
        float: The converted value
        
    Raises:
        InvalidInputError: If the value cannot be converted to a number
    """
    try:
        return float(value)
    except (TypeError, ValueError) as e:
        raise InvalidInputError(f"'{param_name}' must be a numeric value") from e


@click.group()
def main() -> None:
    """pkg-40400 CLI - Calculator Service"""
    Logger.info(f"Calculator version: {version}")


@main.command()
@click.option("--a", "--first", required=True, type=str, help="First operand")
@click.option("--b", "--second", required=True, type=str, help="Second operand")
@click.option(
    "--precision",
    default=10,
    type=int,
    help="Number of decimal places (default: 10)",
)
@click.option("--json", "json_output", is_flag=True, help="Output result in JSON format")
def add(a: str, b: str, precision: int, json_output: bool) -> None:
    """Add two numbers"""
    try:
        a_val = _validate_and_convert(a, "--a")
        b_val = _validate_and_convert(b, "--b")
        result = Calculator.add(a_val, b_val, precision)
        if json_output:
            click.echo(
                json.dumps(
                    {"operation": "add", "operand_a": a_val, "operand_b": b_val, "result": result}
                )
            )
        else:
            click.echo(f"{a_val} + {b_val} = {result:.{precision}f}")
    except InvalidInputError as e:
        Logger.error(f"Invalid input: {e}")
        raise click.ClickException(f"Invalid input: {e}") from e


@main.command()
@click.option("--a", "--first", required=True, type=str, help="First operand")
@click.option("--b", "--second", required=True, type=str, help="Second operand")
@click.option(
    "--precision",
    default=10,
    type=int,
    help="Number of decimal places (default: 10)",
)
@click.option("--json", "json_output", is_flag=True, help="Output result in JSON format")
def subtract(a: str, b: str, precision: int, json_output: bool) -> None:
    """Subtract second number from first"""
    try:
        a_val = _validate_and_convert(a, "--a")
        b_val = _validate_and_convert(b, "--b")
        result = Calculator.subtract(a_val, b_val, precision)
        if json_output:
            click.echo(
                json.dumps(
                    {"operation": "subtract", "operand_a": a_val, "operand_b": b_val, "result": result}
                )
            )
        else:
            click.echo(f"{a_val} - {b_val} = {result:.{precision}f}")
    except InvalidInputError as e:
        Logger.error(f"Invalid input: {e}")
        raise click.ClickException(f"Invalid input: {e}") from e


@main.command()
@click.option("--a", "--first", required=True, type=str, help="First operand")
@click.option("--b", "--second", required=True, type=str, help="Second operand")
@click.option(
    "--precision",
    default=10,
    type=int,
    help="Number of decimal places (default: 10)",
)
@click.option("--json", "json_output", is_flag=True, help="Output result in JSON format")
def multiply(a: str, b: str, precision: int, json_output: bool) -> None:
    """Multiply two numbers"""
    try:
        a_val = _validate_and_convert(a, "--a")
        b_val = _validate_and_convert(b, "--b")
        result = Calculator.multiply(a_val, b_val, precision)
        if json_output:
            click.echo(
                json.dumps(
                    {"operation": "multiply", "operand_a": a_val, "operand_b": b_val, "result": result}
                )
            )
        else:
            click.echo(f"{a_val} * {b_val} = {result:.{precision}f}")
    except InvalidInputError as e:
        Logger.error(f"Invalid input: {e}")
        raise click.ClickException(f"Invalid input: {e}") from e


@main.command()
@click.option("--a", "--first", required=True, type=str, help="First operand")
@click.option("--b", "--second", required=True, type=str, help="Second operand")
@click.option(
    "--precision",
    default=10,
    type=int,
    help="Number of decimal places (default: 10)",
)
@click.option("--json", "json_output", is_flag=True, help="Output result in JSON format")
def divide(a: str, b: str, precision: int, json_output: bool) -> None:
    """Divide first number by second"""
    try:
        a_val = _validate_and_convert(a, "--a")
        b_val = _validate_and_convert(b, "--b")
        result = Calculator.divide(a_val, b_val, precision)
        if json_output:
            click.echo(
                json.dumps(
                    {"operation": "divide", "operand_a": a_val, "operand_b": b_val, "result": result}
                )
            )
        else:
            click.echo(f"{a_val} / {b_val} = {result:.{precision}f}")
    except InvalidInputError as e:
        Logger.error(f"Invalid input: {e}")
        raise click.ClickException(f"Invalid input: {e}") from e
    except DivisionByZeroError as e:
        Logger.error(f"Division by zero: {e}")
        raise click.ClickException("Division by zero is not allowed") from e


if __name__ == "__main__":
    main()
