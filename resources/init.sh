#!/bin/bash

set -e

DB_HOST=localhost
DB_NAME=metrics

USER=postgres
PASSWORD=password

export PGPASSWORD=${PASSWORD}

if [[ $(psql -h ${DB_HOST} -U ${USER} -lt | cut -d \| -f 1 | grep -w ${DB_NAME}) ]]
then
    psql -h ${DB_HOST} -U ${USER} -c "drop database ${DB_NAME};"
fi

psql -h ${DB_HOST} -U ${USER} -c "create database ${DB_NAME};"

psql -h ${DB_HOST} -U ${USER} -d ${DB_NAME}  -a -f db.sql
