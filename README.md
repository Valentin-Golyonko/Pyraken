# All in one web project skeleton: Docker + Django + PostgreSQL + Celery + RabbitMQ + Redis + Django REST.

### start:
- open terminals in current directory
- <code>docker-compose build</code>
- <code>docker-compose up -d</code>
- <code>docker-compose run app python manage.py createsuperuser</code>

### check if it's working:
- <code>docker images</code> # see what images you have
- <code>docker ps</code> # see what containers is up
- check localhost - http://localhost:8000/
- rum something
- check admin - http://localhost:8000/admin/
- <code>docker-compose restart</code> # if localhost does't work

<details><summary>Docker in PyCharm (CLICK ME)</summary>
<p>
  <img src="https://github.com/Valentin-Golyonko/ForDockerTest/blob/master/docker%20in%20pycharm.png" alt="web_view">
  </p>
</details>

### the end:
- <code>docker-compose stop</code>


### work with Postrges:
- <code>docker exec -it  test_app_db psql -U postgres</code>
- if you have previous DB -> dump it data: 
<code>python manage.py dumpdata --exclude=contenttypes --exclude=auth.Permission > initial_data.json</code>
- load dumped data to Postgres container with Django help:
<code>docker-compose run app python manage.py loaddata initial_data.json</code>


### static files:
- collect all Django static so you can share it with Nginx:
<code>docker-compose run app python manage.py collectstatic</code>