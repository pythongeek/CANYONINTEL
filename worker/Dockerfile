FROM mcr.microsoft.com/playwright:v1.41.0-jammy

WORKDIR /app

# Copy the entire project
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r worker/requirements.txt

# Create a non-root user (optional but good practice, though Playwright docker often runs as root or pwuser)
# For simplicity in this phase, we'll run as default.

# Set Python path to include root
ENV PYTHONPATH=/app

# Run the worker
CMD ["python", "worker/main.py"]
