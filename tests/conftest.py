import logging
from unittest.mock import patch

import pytest
import yaml


@pytest.fixture(autouse=True)
def _reset_logging():
    """
    Save and restore global logging state around every test.
    """

    # Save global logger state
    import pkg_40400.core.logger as logger_module

    saved_logger = logger_module.Logger
    saved_initialized = logger_module._initialized

    root = logging.getLogger()
    saved_level = root.level
    saved_handlers = list(root.handlers)

    yield

    # Restore global logger state
    logger_module.Logger = saved_logger
    logger_module._initialized = saved_initialized

    root.handlers = saved_handlers
    root.level = saved_level


@pytest.fixture
def valid_yaml(tmp_path):
    """
    Write a minimal valid dictConfig YAML and return its path.
    """

    config_content = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "plain": {
                "format": "%(asctime)s.%(msecs)03d::%(levelname)s::%(funcName)s::%(filename)s:%(lineno)s::%(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "plain",
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "test_logger": {
                "level": "DEBUG",
                "handlers": ["console"],
                "propagate": False,
            },
        },
    }
    path = tmp_path / "logging.yaml"
    path.write_text(yaml.dump(config_content))
    return path


@pytest.fixture
def mock_settings(tmp_path, valid_yaml):
    """
    Patch ClsSettings to return controlled values.
    """

    with patch("pkg_40400.core.logger.ClsSettings") as MockClsSettings:
        instance = MockClsSettings.return_value
        instance.LOG_LEVEL = logging.DEBUG
        instance.LOG_CFG_PATH = valid_yaml
        instance.LOGGERS_NAME = "test_logger"
        yield instance
