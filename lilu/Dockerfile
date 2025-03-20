# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install gosu
RUN apt-get update && apt-get install -y --no-install-recommends gosu

# Create the nobody user and group (if it doesn't exist)
RUN adduser --system --group nobody || true

# Create logs directory and change ownership
RUN mkdir -p /app/logs && chown nobody:nogroup /app/logs

# Copy project files to the container
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Run gunicorn as nobody using gosu
ENTRYPOINT ["gosu", "nobody", "gunicorn", "lilu.wsgi:application", "--bind", "0.0.0.0:8000"]