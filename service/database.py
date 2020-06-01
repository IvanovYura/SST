from flask import current_app, g
from psycopg2 import connect
from psycopg2.extras import DictCursor
from werkzeug.local import LocalProxy


def open_connection():
    c = g.get('connection')
    if c is None:
        config = current_app.config
        c = g.connection = connect(
            host=config['DB_HOST'],
            port=config['DB_PORT'],
            dbname=config['DB_NAME'],
            user=config['DB_USER'],
            password=config['DB_PASSWORD'],
        )

    return c


def close_connection():
    connection = g.get('connection')
    if connection is not None:
        connection.close()


def get_dict_cursor(connection):
    return connection.cursor(cursor_factory=DictCursor)


connection = LocalProxy(open_connection)
