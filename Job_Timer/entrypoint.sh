#!/bin/sh

echo "Waiting for db"
while ! nc -z db 5432: do sleep 1; done

echo "Connect to db"
python manage.py migrate

exec "$@"
