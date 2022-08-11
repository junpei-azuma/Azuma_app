from logging.config import dictConfig

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
            "filename": "/usr/local/project/notice_pressure/log/python.log",
            "level": "ERROR",
            "backupCount": 3,
            "when": "D",
        }
    },
    "root": {"level": "ERROR", "handlers": ["file"]},
}
