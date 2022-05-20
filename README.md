# All in one web project skeleton
- Docker
- Django / Django REST
- PostgreSQL
- Celery
- RabbitMQ
- WebSockets (Django Channels)
- Redis

### Start:
- open terminals in current directory
- `docker-compose build`
- `docker-compose up -d`

### Work with Postrges:
- `docker exec -it pyraken-db psql -U postgres`
- data backup `python manage.py dumpdata core.Flag _OTHER_APPS_or_APPS_MODELS_ -o db_backup/initial_data.json.xz`

### Check if it's working:
- `docker images` # see what images you have
- `docker ps` # see if containers is up and running
- check out japanese flag builder - http://127.0.0.1:8000/api/core/draw_flag/

<details><summary>Docker in PyCharm (CLICK ME)</summary>
<p>
    <img src="https://github.com/Valentin-Golyonko/Pyraken/blob/master/docker%20in%20pycharm.png" alt="docker_in_pycharm.png">
</p>
</details>

<details><summary>result (CLICK ME)</summary>
<p>
    <img src="https://github.com/Valentin-Golyonko/Pyraken/blob/master/media/result.png" alt="result.png">
</p>
</details>

### Some commands:
- `docker-compose stop`
- `docker-compose restart`
- `docker-compose down`

### Dependencies update
- `pip install --upgrade setuptools pip wheel pip-tools`
- empty requirements.txt file (delete everything inside it)
- `pip-compile`
- `pip-sync`

### If you need to run it as local dev
- go to config/settings and rename local_dev.py to local.py
- watch for __init__.py in settings dir - IDE can rename import!

### Django backups and sharing for apps logs, db backups, media
In `docker-compose.yml` to the `app` container add:
-     volumes:
      - /root/_server_path_/db_backup:/pyraken/db_backup
      - /root/_server_path_/logs_backup:/pyraken/logs
      - /root/_server_path_/media_backup:/pyraken/media

### ...
