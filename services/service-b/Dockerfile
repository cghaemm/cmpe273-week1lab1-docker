FROM python:3.11-slim

# Prevent Python from buffering stdout/stderr (helps logs appear immediately in Docker)
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Document the port (doesn't publish it by itself)
EXPOSE 8081

# Run the service
CMD ["python", "app.py"]