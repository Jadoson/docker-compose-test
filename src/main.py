import os from logging_setup import setup_logging LOGGING = setup_logging()

from fastapi import FastAPI app = FastAPI()

import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)