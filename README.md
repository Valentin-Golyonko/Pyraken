# All in one web project skeleton: Docker + Django + PostgreSQL + Celery + RabbitMQ + Django REST.

### start:
- open terminals in current directory
- <code>docker-compose build</code>
- <code>docker-compose up -d</code>

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


### work with Postrges:
- <code>docker exec -it pyraken-db psql -U postgres</code>
- if you have previous DB -> dump it data: 
<code>python manage.py dumpdata -e contenttypes -e auth.Permission -e admin -e sessions > initial_data.json</code>
- load dumped data to postgres through the django container:
- <code>docker exec -it pyraken-django bash</code>
- root@...:/pyraken# <code>python manage.py loaddata initial_data.json</code>


### static files:
- collect all Django static so you can share it with Nginx:
- <code>docker exec -it pyraken-django bash</code>
- root@...:/pyraken# <code>python manage.py collectstatic</code>
