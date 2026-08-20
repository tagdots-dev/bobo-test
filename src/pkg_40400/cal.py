import click


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@click.group()
def cli():
    """A simple calculator CLI tool."""
    pass


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def add_op(a, b):
    """Add two numbers."""
    result = add(a, b)
    click.echo(f"{a} + {b} = {result}")


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def subtract_op(a, b):
    """Subtract two numbers."""
    result = subtract(a, b)
    click.echo(f"{a} - {b} = {result}")


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def multiply_op(a, b):
    """Multiply two numbers."""
    result = multiply(a, b)
    click.echo(f"{a} * {b} = {result}")


@cli.command()
@click.argument("a", type=float)
@click.argument("b", type=float)
def divide_op(a, b):
    """Divide two numbers."""
    try:
        result = divide(a, b)
        click.echo(f"{a} / {b} = {result}")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == "__main__":
    cli()
