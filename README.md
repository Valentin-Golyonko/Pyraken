# Learning Docker + Django + Postgres + tba

### start:

open 2 terminals in current directory

terminal 1:
- <code>docker-compose build</code>
- <code>docker-compose up</code>

terminal 2:
- <code>docker-compose run app python manage.py migrate</code>
- <code>docker-compose run app python manage.py createsuperuser</code>

### check if it's working:
- <code>docker images</code> # see what images you have
- <code>docker ps</code> # see what containers is up
- check addr - http://localhost:8000/admin/ , and login as created superuser.

### the end:
terminal 2:
- <code>docker-compose stop</code>