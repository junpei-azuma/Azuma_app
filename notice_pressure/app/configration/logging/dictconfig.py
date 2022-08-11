from logging.config import dictConfig
import pathlib

log_dir_path = pathlib.Path(__file__).parent.parent.parent.parent / "log/"

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "file": {
            "format": "%(asctime)s %(levelname)s in %(module)s: %(message)s",
        }
    },
    "handlers": {
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "file",
            "filename": log_dir_path / "python.log",
            "level": "ERROR",
            "backupCount": 3,
            "when": "D",
        }
    },
    "root": {"level": "ERROR", "handlers": ["file"]},
}
