import logging
from logging import config

import yaml

from pkg_40400.core.config import AppSettings


def setup_logging() -> logging.Logger:
    """Configure the package logger"""
    settings = AppSettings()
    log_level = settings.LOG_LEVEL
    log_config_path = settings.LOG_CFG_PATH
    loggers_name = settings.LOGGERS_NAME

    logger = logging.getLogger(loggers_name)

    # If the logger already has handlers attached, assume skip
    # re-configuration to prevent duplicate log entries when
    # the module is imported multiple times.
    if logger.handlers:
        logger.setLevel(log_level)
        return logger

    try:
        """Load logging configuration from the YAML file defined in settings."""
        with open(log_config_path, "r") as f:
            config_dict = yaml.safe_load(f)
        config.dictConfig(config_dict)
    except Exception as e:
        """Fallback to a simple ``basicConfig`` when the config file cannot be
        loaded (e.g., missing file or parsing error)."""
        # LOG_FORMAT = (
        #     '{"_t": "%(asctime)s.%(msecs)03d", '
        #     '"_l": "%(levelname)s", '
        #     '"_f": "%(funcName)s", '
        #     '"_m": "%(filename)s:%(lineno)s", '
        #     '"_d": "%(message)s"}'
        # )
        LOG_FORMAT = "%(asctime)s.%(msecs)03d::%(levelname)s::%(funcName)s::%(filename)s:%(lineno)s::%(message)s"
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
        logger.warning(e)

    logger.setLevel(log_level)
    return logger


Logger = setup_logging()
