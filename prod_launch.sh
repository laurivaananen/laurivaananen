#!/bin/bash
docker-compose down
docker-compose -f prod-docker-compose.yml build
docker-compose -f prod-docker-compose.yml up -d
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

