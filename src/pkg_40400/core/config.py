import os
import pathlib
from dataclasses import dataclass, field


@dataclass(frozen=True)
class AppSettings:
    """Explicitly typed fields; provide defaults or let them be set via __post_init__"""

    ENV: str = ""
    DEBUG: bool = False

    LOGGERS_NAME: str = ""
    LOG_CFG_FILE: str = ""
    LOG_DST_FILE: str = ""

    PROJECT_ROOT: pathlib.Path = field(default=pathlib.Path(__file__).parent.parent.parent.parent, init=False)
    LOG_CFG_PATH: pathlib.Path = field(init=False)
    LOG_DST_PATH: pathlib.Path = field(init=False)
    LOG_LEVEL: int = field(init=False)

    def __post_init__(self) -> None:
        """Ensure loggers_name_value is in the list"""

        loggers_name_value = os.getenv("LOGGERS_NAME", "default").lower()
        object.__setattr__(
            self,
            "LOGGERS_NAME",
            loggers_name_value if loggers_name_value in ("default", "docker", "local", "lambda", "library") else "default",
        )

        # Set environment-dependent fields at runtime
        object.__setattr__(self, "ENV", os.getenv("ENV", "development"))
        object.__setattr__(self, "DEBUG", os.getenv("DEBUG", "True").lower() in ("true", "1"))
        object.__setattr__(self, "LOG_CFG_FILE", os.getenv("LOG_CFG_FILE", "logging.yaml"))
        object.__setattr__(self, "LOG_DST_FILE", os.getenv("LOG_DST_FILE", "app.log"))

        # Recompute paths using runtime values
        object.__setattr__(self, "PROJECT_ROOT", pathlib.Path(__file__).parent.parent.parent.parent)
        object.__setattr__(self, "LOG_CFG_PATH", self.PROJECT_ROOT / "config" / self.LOG_CFG_FILE)
        object.__setattr__(self, "LOG_DST_PATH", self.PROJECT_ROOT / self.LOG_DST_FILE)
        object.__setattr__(self, "LOG_LEVEL", 10 if self.DEBUG else 20)  # 10: DEBUG, 20: INFO
