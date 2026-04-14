FROM ghcr.io/astral-sh/uv:0.6.14-python3.10-bookworm

WORKDIR /app

# Install additional system dependencies for lxml and other packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libavif-dev pkg-config \
    libjpeg-dev \
    gcc unzip zip \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    curl \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-fra \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

COPY SRC/requirements.txt .

RUN uv pip install --system --no-cache -r requirements.txt
COPY SRC/ . 
ENV PYTHONPATH=/app

# Create directory structure for Alembic
RUN mkdir -p /app/Models/db_schemes/minirag/

COPY docker/minirag/alembic.ini /app/Models/db_schemes/minirag/alembic.ini

COPY docker/minirag/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

