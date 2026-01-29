# worker/Dockerfile
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Upgrade to Python 3.11 logic
RUN apt-get update && apt-get install -y python3.11 python3.11-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements-worker.txt .
RUN pip install --no-cache-dir -r requirements-worker.txt

# Install Playwright browsers (Specifically Chromium)
RUN playwright install chromium

# Copy the application code
COPY . .

# Command to run the worker
CMD ["python", "worker/main.py"]
