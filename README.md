# Learning Docker + Django + Postgres + tba

### start:
- open terminals in current directory
- <code>docker-compose build</code>
- <code>docker-compose up -d</code>
- <code>docker-compose run app python manage.py migrate</code>
- <code>docker-compose run app python manage.py createsuperuser</code>

### check if it's working:
- <code>docker images</code> # see what images you have
- <code>docker ps</code> # see what containers is up
- check addr - http://localhost:8000/admin/ , and login as created superuser.
- <code>docker-compose restart</code> # if localhost does't work

### the end:
- <code>docker-compose stop</code>