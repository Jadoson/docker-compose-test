FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD sh -c 'uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --log-level debug --access-log'