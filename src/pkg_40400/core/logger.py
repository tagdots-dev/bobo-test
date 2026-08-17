import logging
from logging import config

import yaml

from pkg_40400.core.config import AppSettings


def setup_logging() -> logging.Logger:
    settings = AppSettings()
    log_level = settings.LOG_LEVEL
    log_config_path = settings.LOG_CFG_PATH
    loggers_name = settings.LOGGERS_NAME

    try:
        """
        Use AppSettings to open logging config file.
        """
        with open(log_config_path, "r") as f:
            config_dict = yaml.safe_load(f)
        config.dictConfig(config_dict)

    except Exception as e:
        """
        Exception if logging config file is not avilable,
        use basicConfig to setup logging.
        """
        LOG_FORMAT = (
            '{"_t": "%(asctime)s.%(msecs)03d", '
            '"_l": "%(levelname)s", '
            '"_f": "%(funcName)s", '
            '"_m": "%(filename)s:%(lineno)s", '
            '"_d": "%(message)s"}'
        )
        logging.basicConfig(
            level=logging.INFO,
            format=LOG_FORMAT,
        )
        logger = logging.getLogger(loggers_name)
        logger.warning(e)

    Logger = logging.getLogger(loggers_name)
    Logger.setLevel(log_level)
    return Logger


Logger = setup_logging()
