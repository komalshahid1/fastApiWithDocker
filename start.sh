#!/bin/bash

echo "⏳ Waiting for MySQL..."
until nc -z db 3306; do
  sleep 1
done

echo "✅ MySQL is ready. Running migrations..."
alembic upgrade head

echo "🚀 Starting FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
