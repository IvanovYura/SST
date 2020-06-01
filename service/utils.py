from service.database import get_dict_cursor, connection

SQL_GET_METRICS = '''
    SELECT
        id,
        timestamp,
        temperature,
        duration
    
    FROM metrics
    LIMIT %(limit)s;
'''

SQL_INSERT_REQUEST_LOG = '''
    INSERT INTO logs (url, http_method, status_code)
    VALUES (
        %(url)s,
        %(http_method)s,
        %(status_code)s
    );
'''


def get_metrics(limit: int):
    with get_dict_cursor(connection) as cursor:
        cursor.execute(SQL_GET_METRICS, {'limit': limit})
        return cursor.fetchall()


def save_request_log(log_entry: dict):
    with get_dict_cursor(connection) as cursor:
        cursor.execute(SQL_INSERT_REQUEST_LOG, log_entry)
        connection.commit()
