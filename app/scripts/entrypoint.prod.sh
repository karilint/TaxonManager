#!/bin/sh

set -e

python manage.py makemigrations
python manage.py migrate --no-input
# python manage.py makemigrations front
# python manage.py migrate front --no-input
python manage.py collectstatic --no-input

gunicorn taxonmanager.wsgi:application --bind 0.0.0.0:8000
