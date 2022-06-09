#!/bin/bash
mkdir logs
mkdir media
mkdir static
touch ./logs/gunicorn.log
. ./venv/bin/activate
echo "--- 1. Preparations done. ---"
sleep 1

python manage.py migrate
echo "--- 2. Migrate done. ---"
sleep 1

python manage.py collectstatic --no-input
echo "--- 3. Collect static files done. ---"
sleep 1

python manage.py loaddata db_backup/initial_data.json.xz  # !!! ONLY FOR TEST !!!
echo "--- 4. Load initial data done. ---"
sleep 1

python manage.py runscript config.queues_scripts.restart_queues
echo "--- 5. Restart  celery worker done. ---"
sleep 1

gunicorn -c ./config/gunicorn/gunicorn_config.py
echo "--- 6. Run django server. ---"
