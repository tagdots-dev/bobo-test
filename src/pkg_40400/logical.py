"""
Logical CLI Utility Module.

This module provides logical validation functionality for string inputs.
It validates that inputs contain only allowed characters (a-zA-Z0-9.-).
"""

import re

from pkg_40400 import Logger


def evaluate(input_value: str) -> bool:
    """
    Evaluate if the input string contains only valid characters.

    The valid characters are: a-z, A-Z, 0-9, period (.), and hyphen (-).

    Args:
        input_value: The string to evaluate

    Returns:
        True if the string contains only valid characters, False otherwise
    """
    pattern = r'^[a-zA-Z0-9.-]+$'
    return bool(re.match(pattern, input_value))


def validate_single_input(args: list) -> str:
    """
    Validate that exactly one input argument is provided.

    Args:
        args: List of command line arguments

    Returns:
        The single input argument

    Raises:
        ValueError: If zero arguments or more than one argument is provided
    """
    if len(args) == 0:
        raise ValueError("Error: No input provided. Please provide exactly one string value.")
    if len(args) > 1:
        raise ValueError(f"Error: Too many inputs provided. Expected exactly one string value, got {len(args)}.")
    return args[0]
