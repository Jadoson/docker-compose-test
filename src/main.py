import os import logging from fastapi import FastAPI, Request, HTTPException

from logging_setup import setup_logging LOG_FILE = setup_logging() logger = logging.getLogger("app")

from sqlalchemy import text from sqlalchemy.ext.asyncio import create_async_engine

app = FastAPI()

@app.on_event("startup") async def on_startup(): logger.info("App startup event fired. Log file: %s", LOG_FILE)

@app.get("/") async def index(request: Request, error: int | None = None): logger.info("Index hit from %s %s", request.client.host if request.client else "?", request.url.path) if error: logger.error("Forced error for testing logs") raise HTTPException(status_code=500, detail="forced error") return {"ok": True, "log_file": LOG_FILE}

DATABASE_URL = os.getenv("DATABASE_URL") # задайте в окружении SQL_ECHO = os.getenv("SQL_ECHO", "0") == "1" engine = create_async_engine(DATABASE_URL, echo=SQL_ECHO) if DATABASE_URL else None

@app.get("/db-ping") async def db_ping(): if not engine: logger.warning("DATABASE_URL is not set") return {"db": "no DATABASE_URL"} async with engine.begin() as conn: res = await conn.execute(text("SELECT 1")) val = res.scalar_one() logger.info("DB ping result: %s", val) return {"db": val}

if name == " main ": import uvicorn # Важно: не даем Uvicorn перезаписать наш лог-конфиг uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")), log_config=None)