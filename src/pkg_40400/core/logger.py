"""Logging module with YAML configuration support."""

import logging
from logging import config

import yaml

from pkg_40400.core.config import ClsSettings

# Placeholder logger - will be replaced on first initialization

Logger: logging.Logger = logging.getLogger("default")
_initialized: bool = False


def initialize_logger() -> logging.Logger:
    """Initialize the package logger with YAML configuration.

    This function configures logging using the YAML file specified in
    config/constants.yaml or environment variables. It should only be called
    once during application startup.

    Returns:
        The configured Logger instance.

    Notes:
        - Environment variables can override logging settings
        - Falls back to basicConfig if YAML file cannot be loaded
    """
    global Logger, _initialized

    if _initialized:
        # On subsequent calls, update the level if needed
        settings = ClsSettings()
        Logger.setLevel(settings.LOG_LEVEL)
        return Logger

    settings = ClsSettings()
    log_level = settings.LOG_LEVEL
    log_config_path = settings.LOG_CFG_PATH
    logger_name = settings.LOGGERS_NAME

    Logger = logging.getLogger(logger_name)

    # If the logger already has handlers attached, assume configuration has
    # already been performed and skip reconfiguration.
    if Logger.handlers:
        Logger.setLevel(log_level)
        _initialized = True
        return Logger

    try:
        with open(log_config_path, "r") as f:
            config_dict = yaml.safe_load(f)
        config.dictConfig(config_dict)
    except Exception as e:
        LOG_FORMAT = "%(asctime)s.%(msecs)03d::%(levelname)s::%(funcName)s::%(filename)s:%(lineno)s::%(message)s"
        logging.basicConfig(level=log_level, format=LOG_FORMAT)
        Logger.warning(e)

    Logger.setLevel(log_level)
    _initialized = True
    return Logger


def get_logger(name: str | None = None) -> logging.Logger:
    """Get a logger instance by name.

    This function provides flexibility to get named loggers throughout the
    application without reinitializing the logging system.

    Args:
        name: The name of the logger to retrieve. If None, uses the configured
            logger name from the global Logger. Defaults to None.

    Returns:
        A Logger instance with the specified name.
    """
    if name is None:
        return Logger
    return logging.getLogger(name)


# Alias for backward compatibility with existing tests
setup_logging = initialize_logger
