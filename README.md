# Base project skeleton with: Docker + Django + Postgres + Celery + RabbitMQ + Redis + tba

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

### the end:
- <code>docker-compose stop</code>
