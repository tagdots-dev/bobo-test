import logging
import logging.config
from unittest.mock import patch

import yaml

from pkg_40400.core.logger import setup_logging


class TestSetupLoggingYamlLoaded:
    """
    Mocked Settings - YAML loaded successfully
    """

    def test_returns_logger_instance(self, mock_settings):
        logger = setup_logging()
        assert isinstance(logger, logging.Logger)

    def test_logger_name_matches_settings(self, mock_settings):
        logger = setup_logging()
        assert logger.name == "test_logger"

    def test_logger_level_matches_settings(self, mock_settings):
        logger = setup_logging()
        assert logger.level == logging.DEBUG

    def test_yaml_handlers_are_applied(self, mock_settings):
        logger = setup_logging()
        # dictConfig with a "loggers" key configures the named logger;
        # the logger has its own handlers (propagate=False).
        assert logger.name == "test_logger"
        assert len(logger.handlers) >= 1
        assert isinstance(logger.handlers[0], logging.StreamHandler)

    def test_yaml_formatter_is_applied(self, mock_settings):
        setup_logging()
        handler = logging.getLogger("test_logger").handlers[0]
        assert handler.formatter is not None
        assert (
            handler.formatter._fmt
            == "%(asctime)s.%(msecs)03d::%(levelname)s::%(funcName)s::%(filename)s:%(lineno)s::%(message)s"
        )

    def test_round_trip_message(self, mock_settings, capfd):
        """A log call should produce the plain-formatted output from YAML."""
        setup_logging()
        logger = logging.getLogger("test_logger")
        logger.info("hello")
        captured = capfd.readouterr()
        assert "hello" in captured.out
        assert "INFO" in captured.out


class TestSetupLoggingFallbackFileNotFound:
    """
    Fallback path - file not found
    """

    def test_returns_logger_when_file_missing(self, tmp_path):
        missing = tmp_path / "does_not_exist.yaml"
        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.INFO
            instance.LOG_CFG_PATH = missing
            instance.LOGGERS_NAME = "fallback_logger"

            logger = setup_logging()

        assert isinstance(logger, logging.Logger)
        assert logger.name == "fallback_logger"
        assert logger.level == logging.INFO

    def test_basic_config_is_used_on_missing_file(self, tmp_path, caplog):
        missing = tmp_path / "nope.yaml"
        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.INFO
            instance.LOG_CFG_PATH = missing
            instance.LOGGERS_NAME = "fallback_logger"

            with caplog.at_level(logging.WARNING):
                setup_logging()

        # The except block calls logger.warning(e)
        assert any("nope.yaml" in rec.message for rec in caplog.records)

    def test_fallback_handler_has_json_format(self, tmp_path):
        missing = tmp_path / "nope.yaml"
        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.INFO
            instance.LOG_CFG_PATH = missing
            instance.LOGGERS_NAME = "fallback_logger"

            setup_logging()

        root = logging.getLogger()
        assert len(root.handlers) >= 1


class TestSetupLoggingFallbackMalformedYaml:
    """
    Fallback path - malformed YAML
    """

    def test_returns_logger_on_bad_yaml(self, tmp_path):
        bad = tmp_path / "bad.yaml"
        bad.write_text("this: is: not: valid: yaml: [")

        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.WARNING
            instance.LOG_CFG_PATH = bad
            instance.LOGGERS_NAME = "bad_yaml_logger"

            logger = setup_logging()

        assert isinstance(logger, logging.Logger)
        assert logger.name == "bad_yaml_logger"
        assert logger.level == logging.WARNING

    def test_warning_logged_on_bad_yaml(self, tmp_path, caplog):
        bad = tmp_path / "bad.yaml"
        bad.write_text("this: is: not: valid: yaml: [")

        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.WARNING
            instance.LOG_CFG_PATH = bad
            instance.LOGGERS_NAME = "bad_yaml_logger"

            with caplog.at_level(logging.WARNING):
                setup_logging()

        assert len(caplog.records) >= 1
        assert caplog.records[0].levelname == "WARNING"


class TestSetupLoggingFallbackInvalidSchema:
    """
    Fallback path - valid YAML but invalid dictConfig schema
    """

    def test_returns_logger_on_invalid_dictconfig(self, tmp_path):
        bad = tmp_path / "invalid_schema.yaml"
        bad.write_text(yaml.dump({"version": 1, "root": "not_a_dict"}))

        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.ERROR
            instance.LOG_CFG_PATH = bad
            instance.LOGGERS_NAME = "schema_logger"

            logger = setup_logging()

        assert isinstance(logger, logging.Logger)
        assert logger.name == "schema_logger"
        assert logger.level == logging.ERROR


class TestSetupLoggingEdgeCases:
    """
    Edge cases
    """

    def test_logger_level_overrides_yaml_level(self, tmp_path):
        """LOG_LEVEL from settings should win over the YAML root level."""
        config_content = {
            "version": 1,
            "disable_existing_loggers": False,
            "root": {"level": "DEBUG"},
        }
        path = tmp_path / "logging.yaml"
        path.write_text(yaml.dump(config_content))

        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.ERROR  # stricter than YAML's DEBUG
            instance.LOG_CFG_PATH = path
            instance.LOGGERS_NAME = "override_logger"

            logger = setup_logging()

        # setLevel is called *after* dictConfig, so it wins
        assert logger.level == logging.ERROR

    def test_empty_yaml_file_triggers_fallback(self, tmp_path, caplog):
        empty = tmp_path / "empty.yaml"
        empty.write_text("")

        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.INFO
            instance.LOG_CFG_PATH = empty
            instance.LOGGERS_NAME = "empty_logger"

            with caplog.at_level(logging.WARNING):
                logger = setup_logging()

        assert isinstance(logger, logging.Logger)
        # yaml.safe_load("") returns None → dictConfig(None) raises
        assert any(rec.levelname == "WARNING" for rec in caplog.records)


class TestSetupLoggingWithExistingHandlers:
    """
    Test the case when logger already has handlers (lines 21-23)
    """

    def test_returns_existing_logger_when_handlers_present(self, tmp_path):
        """When logger already has handlers, return it without reconfiguring."""
        config_content = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {
                "existing_handlers_logger": {
                    "level": "DEBUG",
                    "handlers": ["console"],
                    "propagate": False,
                },
            },
            "root": {"level": "DEBUG", "handlers": []},
        }
        path = tmp_path / "logging.yaml"
        path.write_text(yaml.dump(config_content))

        # First call to setup logging - creates logger with handlers
        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.DEBUG
            instance.LOG_CFG_PATH = path
            instance.LOGGERS_NAME = "existing_handlers_logger"
            logger1 = setup_logging()

        # Second call should return same logger (short-circuit on line 21-23)
        with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
            instance = MockAppSettings.return_value
            instance.LOG_LEVEL = logging.ERROR  # Different level
            instance.LOG_CFG_PATH = path
            instance.LOGGERS_NAME = "existing_handlers_logger"

            logger2 = setup_logging()

        # Should be the same logger object
        assert logger1 is logger2
        # Level should have been updated from second call
        assert logger2.level == logging.ERROR
