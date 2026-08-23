"""
Project Script
"""

from pkg_40400 import (
    Logger,
    version,
)


def main() -> None:
    Logger.info(f"{version}")


if __name__ == "__main__":
    main()
