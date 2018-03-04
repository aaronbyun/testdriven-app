#!/bin/sh

echo "Waiting for postgress..."

while ! nc -z users-db 5432; do
    sleep 0.1
done

echo "PostgresSQL started"

# flask run -h 0.0.0.0
gunicorn -b 0.0.0.0:5000 manage:app