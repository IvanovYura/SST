import os


class BaseConfig:
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = int(os.environ.get('DB_PORT', 5432))
    DB_NAME = os.environ.get('DB_NAME', 'metrics')
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')

    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))


class TestConfig(BaseConfig):
    DB_HOST = ''
    DB_PORT = ''
    DB_NAME = ''
    DB_USER = ''
    DB_PASSWORD = ''
