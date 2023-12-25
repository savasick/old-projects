#!/bin/sh

echo "Waiting for postgres..."; \

while ! nc -z $DB_HOST $DB_PORT ; do sleep 5 ; done ; \

echo "PostgreSQL started"; \

python manage.py makemigrations --no-input; \

python manage.py migrate --no-input; \

python manage.py collectstatic --no-input; \

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput; \

exec "$@"