import os
import pathlib
from dataclasses import dataclass


@dataclass(frozen=True)
class ClsSettings:
    """
    Centralized configuration settings.

    This dataclass reads environment variables on instantiation and computes
    derived values. It is designed to be instantiated once at application
    startup and passed to components that need configuration.

    Note: This dataclass is immutable (frozen). All fields are set during
    initialization and cannot be modified afterward.
    """

    # Environment-dependent configuration
    ENV: str
    DEBUG: bool
    LOGGERS_NAME: str

    # Logging file configuration (read from environment)
    LOG_CFG_FILE: str = "logging.yaml"
    LOG_DST_FILE: str = "app.log"

    # File paths (computed from environment variables)
    PROJECT_ROOT: pathlib.Path = None  # type: ignore
    LOG_CFG_PATH: pathlib.Path = None  # type: ignore
    LOG_LEVEL: int = None  # type: ignore

    def __init__(
        self,
        env: str | None = None,
        debug: bool | None = None,
        loggers_name: str | None = None,
    ) -> None:
        """
        Initialize configuration from environment variables.

        Args:
            env: Override ENV value. If None, reads from ENV env var.
            debug: Override DEBUG value. If None, reads from DEBUG env var.
            loggers_name: Override LOGGERS_NAME value. If None, reads from LOGGERS_NAME env var.
        """
        # Set defaults at initialization time
        object.__setattr__(self, "ENV", self._validate_env(env))
        object.__setattr__(self, "DEBUG", self._validate_debug(debug))
        object.__setattr__(self, "LOGGERS_NAME", self._validate_loggers_name(loggers_name))
        object.__setattr__(self, "LOG_CFG_FILE", os.getenv("LOG_CFG_FILE", "logging.yaml"))
        object.__setattr__(self, "LOG_DST_FILE", os.getenv("LOG_DST_FILE", "app.log"))

        # Compute derived values once
        object.__setattr__(self, "PROJECT_ROOT", self._compute_project_root())
        object.__setattr__(self, "LOG_CFG_PATH", self._compute_log_cfg_path())
        object.__setattr__(self, "LOG_LEVEL", self._compute_log_level())

    def _validate_env(self, env: str | None = None) -> str:
        """Validate and normalize ENV value."""
        value = env if env is not None else os.getenv("ENV", "development")
        value = value.lower()
        valid_values = ("development", "production", "local")
        return value if value in valid_values else "development"

    def _validate_debug(self, debug: bool | None = None) -> bool:
        """Validate and normalize DEBUG value."""
        if debug is not None:
            return bool(debug)

        debug_str = os.getenv("DEBUG", "true")
        return debug_str.lower() in ("true", "1", "t", "yes")

    def _validate_loggers_name(self, loggers_name: str | None = None) -> str:
        """Validate and normalize LOGGERS_NAME value."""
        value = loggers_name if loggers_name is not None else os.getenv("LOGGERS_NAME", "default")
        value = value.lower()
        valid_values = ("default", "docker", "local", "lambda", "library")
        return value if value in valid_values else "default"

    def _compute_project_root(self) -> pathlib.Path:
        """Compute the project root directory."""
        # The config module is at src/pkg_40400/core/config.py
        # So we need to go up 3 levels to get to src/, then up 1 more to get to project root
        return pathlib.Path(__file__).parent.parent.parent.parent

    def _compute_log_cfg_path(self) -> pathlib.Path:
        """Compute the path to the logging configuration file."""
        return self.PROJECT_ROOT / "config" / self.LOG_CFG_FILE

    def _compute_log_level(self) -> int:
        """Compute the log level based on DEBUG setting."""
        return 10 if self.DEBUG else 20  # 10: DEBUG, 20: INFO
