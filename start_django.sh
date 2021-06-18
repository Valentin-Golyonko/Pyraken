#!/bin/bash
mkdir logs
mkdir media
mkdir static

sleep 5

echo 'migrate:'
docker exec -it pyraken-django bash

#echo 'collectstatic:'
# python manage.py collectstatic --no-input

echo 'loaddata:'
python manage.py loaddata initial_data.json.xz

echo 'runscript:'
# restart/start celery main worker
python manage.py runscript config.queues_scripts.restart_queues

echo 'runserver:'
python manage.py runserver 0.0.0.0:8000

echo 'nothing here'