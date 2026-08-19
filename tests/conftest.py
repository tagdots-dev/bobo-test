import logging
import pytest
from unittest.mock import patch

import yaml


@pytest.fixture(autouse=True)
def _reset_logging():
    """
    Save and restore global logging state around every test.
    """

    root = logging.getLogger()
    saved_level = root.level
    saved_handlers = list(root.handlers)

    yield

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
            "json": {"format": '{"msg": "%(message)s"}'},
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "json",
                "stream": "ext://sys.stdout",
            },
        },
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }
    path = tmp_path / "logging.yaml"
    path.write_text(yaml.dump(config_content))
    return path


@pytest.fixture
def mock_settings(tmp_path, valid_yaml):
    """
    Patch AppSettings to return controlled values.
    """

    with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
        instance = MockAppSettings.return_value
        instance.LOG_LEVEL = logging.DEBUG
        instance.LOG_CFG_PATH = valid_yaml
        instance.LOGGERS_NAME = "test_logger"
        yield instance
