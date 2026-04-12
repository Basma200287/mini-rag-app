#!/bin/bash
set -e

echo "Running database migrations..."
cd /app/Models/db_schemes/minirag/
alembic upgrade head

echo "Starting FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port 8000