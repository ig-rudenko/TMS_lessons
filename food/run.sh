#!/bin/sh
poetry run python manage.py migrate;
poetry run python manage.py createsuperuser --noinput;
poetry run gunicorn -w 2 -b 0.0.0.0:8000 food.wsgi:application;