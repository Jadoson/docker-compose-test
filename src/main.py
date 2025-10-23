import os from logging_setup import setup_logging LOGGING = setup_logging()

from fastapi import FastAPI app = FastAPI()

import logging logging.getLogger( name ).info("App module imported")

from sqlalchemy import create_engine DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://...") SQL_ECHO = os.getenv("SQL_ECHO", "0") == "1" engine = create_engine(DATABASE_URL, echo=SQL_ECHO)

if name == " main ": import uvicorn # Не даём Uvicorn перезаписать наш конфиг логирования uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")), log_config=None)
