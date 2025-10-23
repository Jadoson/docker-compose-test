import os import logging from logging.handlers import RotatingFileHandler from pathlib import Path

def setup_logging(): # Абсолютный путь в домашнем каталоге пользователя log_dir_env = os.environ.get("LOG_DIR") if log_dir_env: LOG_DIR = Path(log_dir_env).expanduser() else: LOG_DIR = Path.home() / "logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)
log_file = LOG_DIR / "app.log"

fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"

# Переконфигурируем логирование подчистую
file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5, encoding="utf-8")
stream_handler = logging.StreamHandler()

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format=fmt,
    handlers=[stream_handler, file_handler],
    force=True,  # важно: перезапишет любые предыдущие настройки (в т.ч. uvicorn)
)

# Дадим полезным логгерам уровни и пропагирование к root, чтобы они попали в наш файл
for name in ("uvicorn", "uvicorn.error", "uvicorn.access", "sqlalchemy.engine"):
    lg = logging.getLogger(name)
    lg.setLevel(logging.INFO)
    lg.propagate = True  # пусть идут в root, где наш file handler

logging.getLogger(__name__).info("Logging configured. LOG_DIR=%s", str(LOG_DIR))
return str(log_file)
