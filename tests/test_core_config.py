"""
Unit Test
"""

import os
from unittest.mock import patch

from pkg_40400.core.config import AppSettings


def test_app_settings_env_default():
    """
    validate that environment variables use default value
    """
    settings = AppSettings()
    assert settings.ENV == "development"
    assert settings.DEBUG is True  # default per "True" in code
    assert settings.LOG_CFG_FILE == "logging.yaml"
    assert settings.LOG_DST_FILE == "app.log"


@patch.dict(
    os.environ,
    {"ENV": "production", "DEBUG": "false", "LOG_CFG_FILE": "prod_logging.yaml", "LOG_DST_FILE": "prod_app.log"},
    clear=True,
)
def test_app_settings_env_override():
    """
    validate that environment variables use overriden value
    """
    settings = AppSettings()
    assert settings.ENV == "production"
    assert settings.DEBUG is False
    assert settings.LOG_CFG_FILE == "prod_logging.yaml"
    assert settings.LOG_DST_FILE == "prod_app.log"


@patch.dict(
    os.environ,
    {"LOGGERS_NAME": "hello"},
    clear=True,
)
def test_app_settings_loggers_name_not_in_list():
    """
    validate that invalid LOGGERS_NAME revert to "default"
    """
    settings = AppSettings()
    assert settings.LOGGERS_NAME == "default"


def test_app_settings_env_debug_true():
    """
    validate that environment variable LOG_LEVEL is 10 when DEBUG is true
    """
    with patch.dict(os.environ, {"DEBUG": "true"}, clear=True):
        settings = AppSettings()
        assert settings.LOG_LEVEL == 10  # DEBUG


def test_app_settings_env_debug_false():
    """
    validate that environment variable LOG_LEVEL is 20 when DEBUG is false
    """
    with patch.dict(os.environ, {"DEBUG": "false"}, clear=True):
        settings = AppSettings()
        assert settings.LOG_LEVEL == 20  # INFO
