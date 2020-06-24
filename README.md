## Description

Here is a simple metrics uploader `importer.py` (saves test_data.csv to prepared DB) and the service to read the imported data in simple HTML format.

### Requirements 

1. Postgres DB
2. Python 3.7
3. pipenv

## IMPORTER

Its a simple CLI application which allows you to save test_data.csv to a DB.
Be aware, you need to setup DB first, before applying CSV to it.

### How To

1. run ```python -m pipenv install``` to create a virtual environment and install dependencies
2. run ```sh resources/init.sh``` to create DB and all needed tables
3. run ```python importer.py --csv resources/task_data.csv  --url postgresql://<user>:<password>@<host>/<db_name>``` 

NOTE: use your own username and password for DB (in `init.sh` and `--url`), mine are default from Docker Postgres image

To check that data was really imported the DB:

1. run ```psql -h <host> -U <user>``` and type password after to connect to Postgres
2. run ```\c <db_name>``` to connect to DB
3. run ```SELECT * FROM metrics;```

## SERVICE

This is a Flask-RestX simple service to get data from DB and return it as simple HTML.
Each request to this service is logged separately to table logs in DB.

### How to

1. make sure you run ```python -m pipenv install``` to install all dependencies and virtual environment
2. make sure that DB is created (see `resources/init.sh`) and populated (see `Importer` section)
3. make sure your DB credentials are valid in `service/config.py`
4. run ```python service/app.py``` to run an application

To check the output call with CURL or in Browse ```http://127.0.0.1:5000/api/v1/metrics```

Also the service supports query param `limit`, it will return exact amount of rows from DB what was specified.
For example ```http://127.0.0.1:5000/api/v1/metrics?limit=1```
If this parameter is not specified, you will get the full output.

To check that request was logged run SQL query in DB (see `Importer` section): ```SELECT * FROM logs;```

### Testing

To run unit tests use:
```shell
python -m unittest discover -s tests/ -v
```

## Comments

1. Its better to use env variables in init.sh instead of hardcoding them
2. Importer is not ideal, it would nice to have it more flexible, to be able upload different CSVs, and with better validation
3. There is no unit-tests for Importer, I understand it is important to have
4. TODO: get output by timestamp
5. Instead I added `limit` parameter
