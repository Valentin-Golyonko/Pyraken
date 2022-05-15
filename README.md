# All in one web project skeleton: Docker + Django + PostgreSQL + Celery + RabbitMQ + Django REST.

### start:

- open terminals in current directory
- <code>docker-compose build</code>
- <code>docker-compose up -d</code>

### work with Postrges:

- <code>docker exec -it pyraken-db psql -U postgres</code>

### check if it's working:

- <code>docker images</code> # see what images you have
- <code>docker ps</code> # see what containers is up
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

### some commands:

- <code>docker-compose stop</code>
- <code>docker-compose restart</code>
- <code>docker-compose down</code>

### Dependencies update

- <code>pip install --upgrade setuptools pip wheel pip-tools</code>
- empty requirements.txt file (delete everything inside it)
- <code>pip-compile</code>
- <code>pip-sync</code>

### if you need to run it as local dev
- go to config/settings and rename local_dev.py to local.py
- watch for __init__.py in settings dir - IDE can rename import!
