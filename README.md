# Learning Docker + Django + Postgres + tba

<code>cd pgs</code>

<code>docker build -t my-postgres-image .</code>

<code>cd ..</code>

<code>docker build -t my-python-image .</code> 

<code>docker images -a</code>

<code>docker-compose build</code>

<code>docker-compose up</code>

in a new terminal for this directory:

<code>docker-compose run app python manage.py migrate</code>

<code>docker-compose run app python manage.py createsuperuser</code>

<code>docker ps</code> # see what containers is up

check addr - http://localhost:8000/admin/ , and login as created superuser.