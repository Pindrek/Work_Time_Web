#!/bin/sh

echo "Makemigrations"
python manage.py makemigrations

echo "Migrate"
python manage.py migrate

exec "$@"
