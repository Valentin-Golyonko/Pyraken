#!/bin/bash
mkdir logs
mkdir media
mkdir static
sleep 5
echo 'activate venv:'
. ./venv/bin/activate

python -V
pip -V
source ./venv/bin/activate

echo 'migrate:'
python manage.py migrate

#echo 'collectstatic:'
# python manage.py collectstatic --no-input

echo 'loaddata:'
python manage.py loaddata initial_data.json

echo 'runscript:'
# restart/start celery main worker
python manage.py runscript config.queues_scripts.restart_queues

echo 'runserver:'
python manage.py runserver 0.0.0.0:8000

echo 'nothing here'