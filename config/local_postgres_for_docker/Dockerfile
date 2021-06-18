FROM postgres:12

ARG psql_pass
ARG psql_db

ENV POSTGRES_PASSWORD=$psql_pass
ENV POSTGRES_DB=$psql_db
COPY init.sql /docker-entrypoint-initdb.d/