# underland

## what's inside.
* python3
* Django 1.11

## main commands

### development
* `docker-compose build`
* `docker-compose run django python ./manage.py migrate`
* `docker-compose run -p 8000:8000 django python ./manage.py runserver 0.0.0.0:8000`

* `docker-compose run django python ./manage.py sqlflush`
* `psql -U username -h postgres`

### production
* `docker-compose -f docker-compose.yml -f docker-compose-production.yml up -d`

### test
`docker-compose run django py.test -s .`

## TODO
* [  ] graphene config
