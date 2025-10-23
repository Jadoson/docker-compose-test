import os import logging import logging.config

def setup_logging(): from logging.handlers import RotatingFileHandler

LOG_DIR = os.environ.get("LOG_DIR", os.path.expanduser("~/logs"))
os.makedirs(LOG_DIR, exist_ok=True)
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": "%(asctime)s %(levelname)s %(name)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOG_DIR, "app.log"),
            "maxBytes": 5 * 1024 * 1024,
            "backupCount": 5,
            "encoding": "utf-8",
            "formatter": "default",
        },
    },
    "root": {"level": LOG_LEVEL, "handlers": ["console", "file"]},
    "loggers": {
        "uvicorn": {"level": LOG_LEVEL, "handlers": ["console", "file"], "propagate": False},
        "uvicorn.error": {"level": LOG_LEVEL, "handlers": ["console", "file"], "propagate": False},
        "uvicorn.access": {"level": LOG_LEVEL, "handlers": ["console", "file"], "propagate": False},
        "sqlalchemy.engine": {"level": "INFO", "handlers": ["console", "file"], "propagate": False},
    },
}

logging.config.dictConfig(LOGGING)
logging.getLogger(__name__).info("Logging configured. LOG_DIR=%s", LOG_DIR)
return LOGGING

