# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies that might be needed by WeasyPrint
# This is a common set; adjust if specific errors arise during build or runtime
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     libffi-dev     libpango1.0-0     libharfbuzz0b     libfontconfig1     libjpeg-dev     zlib1g-dev     && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code from the current directory to the working directory
COPY . .

# Create directories for reports and uploads
# These directories will be created within the /app directory
RUN mkdir -p reports uploads

# Expose the port the app runs on
EXPOSE 8080

# Define the command to run the application
# Ensure webapp:app correctly points to your Flask app instance in webapp.py
# The user running Gunicorn inside the container should have write access to /app/reports and /app/uploads
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "webapp:app"]
