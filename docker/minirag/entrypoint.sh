#!/bin/bash
set -e

echo "Running database migrations..."
cd /app/Models/db_schemes/minirag/
alembic upgrade head
cd /app