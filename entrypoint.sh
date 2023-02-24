#!/bin/bash

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

# Start server
echo "Starting server"
gunicorn todo.wsgi:application --bind 0:8000