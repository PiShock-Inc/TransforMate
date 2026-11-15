# Use an official, lightweight Python runtime
FROM python:3.12-slim

# Prevent Python from writing .pyc files and ensure logs output immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies first (caches this layer for faster rebuilds)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code into the container
COPY src/ ./src/

# Create the cache directory and mark it as a volume
RUN mkdir -p /app/cache/people
VOLUME /app/cache

# Run the application
CMD ["python", "src/main.py"]

