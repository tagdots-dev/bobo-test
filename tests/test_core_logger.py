"""
Unit Test
"""

import pathlib
from unittest.mock import patch

import yaml

from pkg_40400.core.logger import Logger, setup_logging


def test_setup_logging_successfully_loads_yaml(tmp_path):
    config_content = {
        "version": 1,
        "formatters": {"json": {"format": '{"msg": "%(message)s"}'}},
        "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "json"}},
        "root": {"level": "DEBUG", "handlers": ["console"]},
    }

    yaml_file = tmp_path / "test_logging.yaml"
    yaml_file.write_text(yaml.dump(config_content))

    with patch("pkg_40400.core.config.AppSettings") as mock_settings:
        instance = mock_settings.return_value
        instance.LOG_CFG_PATH = yaml_file
        instance.LOGGERS_NAME = "test_logger"

        logger = setup_logging()
        assert isinstance(logger, Logger.__class__)


def test_setup_logging_falls_back_to_basic_config_on_exception():
    with patch("builtins.open", side_effect=Exception("YAML not found")):
        with patch("pkg_40400.core.config.AppSettings") as mock_settings:
            instance = mock_settings.return_value
            instance.LOG_CFG_PATH = pathlib.Path("/invalid/config.yaml")
            instance.LOGGERS_NAME = "fallback_logger"

            logger = setup_logging()
            # Basic logging configured, fallback works
            assert isinstance(logger, Logger.__class__)
