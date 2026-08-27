"""
Calculator CLI - pkg-40400

A command-line interface for basic arithmetic operations using click.
"""

import sys

from pkg_40400 import get_logger, initialize_logger, version


def main():
    """Main entry point for the CLI."""
    initialize_logger()
    logger = get_logger()
    try:
        logger.info(version)
    except Exception as e:
        logger = get_logger()
        logger.error(str(e))
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
