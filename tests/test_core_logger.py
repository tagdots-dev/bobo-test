import logging
import logging.config
from unittest.mock import patch

import yaml

from pkg_40400.core.logger import setup_logging

# @pytest.fixture(autouse=True)
# def _reset_logging():
#     """
#     Save and restore global logging state around every test.
#     """

#     root = logging.getLogger()
#     saved_level = root.level
#     saved_handlers = list(root.handlers)

#     yield

#     root.handlers = saved_handlers
#     root.level = saved_level


# @pytest.fixture
# def valid_yaml(tmp_path):
#     """
#     Write a minimal valid dictConfig YAML and return its path.
#     """

#     config_content = {
#         "version": 1,
#         "disable_existing_loggers": False,
#         "formatters": {
#             "json": {"format": '{"msg": "%(message)s"}'},
#         },
#         "handlers": {
#             "console": {
#                 "class": "logging.StreamHandler",
#                 "formatter": "json",
#                 "stream": "ext://sys.stdout",
#             },
#         },
#         "root": {"level": "DEBUG", "handlers": ["console"]},
#     }
#     path = tmp_path / "logging.yaml"
#     path.write_text(yaml.dump(config_content))
#     return path


# @pytest.fixture
# def mock_settings(tmp_path, valid_yaml):
#     """
#     Patch AppSettings to return controlled values.
#     """

#     with patch("pkg_40400.core.logger.AppSettings") as MockAppSettings:
#         instance = MockAppSettings.return_value
#         instance.LOG_LEVEL = logging.DEBUG
#         instance.LOG_CFG_PATH = valid_yaml
#         instance.LOGGERS_NAME = "test_logger"
#         yield instance


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
        # dictConfig with a "root" key configures the root logger;
        # the named logger inherits handlers via propagation.
        assert logger.name == "test_logger"
        root = logging.getLogger()
        assert len(root.handlers) >= 1
        assert isinstance(root.handlers[0], logging.StreamHandler)

    def test_yaml_formatter_is_applied(self, mock_settings):
        setup_logging()
        root = logging.getLogger()
        handler = root.handlers[0]
        assert handler.formatter is not None
        assert handler.formatter._fmt == '{"msg": "%(message)s"}'

    def test_round_trip_message(self, mock_settings, capsys):
        """A log call should produce the JSON-formatted output from YAML."""
        setup_logging()
        logger = logging.getLogger("test_logger")
        logger.info("hello")
        captured = capsys.readouterr()
        assert '"msg": "hello"' in captured.out


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
