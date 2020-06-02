import sys
from argparse import ArgumentParser
from logging import getLogger, INFO
from urllib.parse import urlparse

import psycopg2

logger = getLogger(__name__)
logger.setLevel(INFO)

ap = ArgumentParser(
    description='Transfers data in CSV format to a specific DB',
)
ap.add_argument('--csv', type=str, help='Path to CSV file', required=True)
ap.add_argument('--url', type=str, help='Postgres connection string', required=True)

ALLOWED_COLUMNS = ['id', 'timestamp', 'temperature', 'duration']


def run():
    try:
        args = ap.parse_args()

        path_to_csv = args.csv
        url = urlparse(args.url)

        _populate_db(url, path_to_csv)

    except Exception as e:
        logger.error(f'Something went wrong: {str(e)}')
        sys.exit(1)


def _populate_db(url, path_to_csv):
    connection = _get_connection(url)

    with connection.cursor() as cursor:
        with open(path_to_csv, 'r') as f:
            # skip header
            _validate_columns(next(f))

            cursor.copy_from(f, 'metrics', sep=',', columns=ALLOWED_COLUMNS)
            connection.commit()

            logger.info('Metrics were populated')


def _get_connection(url):
    try:
        logger.info(f'Get connection to: {url}')
        return psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
        )

    except psycopg2.OperationalError as e:
        logger.error(e)
        raise Exception(e)


def _validate_columns(header):
    if set(header.rstrip().split(',')) - set(ALLOWED_COLUMNS):
        raise ValueError('Not allowed columns in the header')


if __name__ == '__main__':
    run()
