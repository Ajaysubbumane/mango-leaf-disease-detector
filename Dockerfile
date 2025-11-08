# Stage 1: Base image with Python
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements-server.txt .
RUN pip install --no-cache-dir -r requirements-server.txt

# Copy application code (NOT model files)
COPY app.py /app/
COPY class_names.json /app/ 2>/dev/null || true

# Model directory (volumes or download at runtime)
RUN mkdir -p /app/saved_models/7

# Try to download model from GitHub Release (optional, for cloud deployment)
# Falls back gracefully if not available
RUN apt-get update && apt-get install -y --no-install-recommends wget && rm -rf /var/lib/apt/lists/* ; \
    wget -O /app/saved_models/7/model_weights.weights.h5 \
    https://github.com/Ajaysubbumane/mango-leaf-disease-detector/releases/download/v7/model_weights.weights.h5 2>/dev/null || echo "Model download optional - will use local volume if available"

# Expose port
ENV PORT=8080
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8080/health', timeout=5)"

# Run with gunicorn (production server)
CMD exec gunicorn --bind 0.0.0.0:${PORT} --workers 2 --threads 2 --worker-class gthread --timeout 120 app:app
