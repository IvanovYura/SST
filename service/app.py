import os

from flask import Blueprint, Flask, request
from flask_restx import Api

from service import database
from service.config import BaseConfig
from service.api import ns
from service.utils import save_request_log


def create_app(config: BaseConfig) -> Flask:
    path_to_templates = os.path.join(config.PROJECT_ROOT, 'resources', 'templates')

    app = Flask(__name__, template_folder=path_to_templates)
    app.config.from_object(config)

    api_blueprint = Blueprint(__name__, __name__)

    api = Api(api_blueprint)
    api.add_namespace(ns, '/v1')
    app.register_blueprint(api_blueprint, url_prefix='/api')
    # close connection after request
    app.teardown_appcontext(close_connection)

    return app


def close_connection(exception=None):
    database.close_connection()


if __name__ == '__main__':
    config = BaseConfig()
    app = create_app(config)


    @app.after_request
    def log_request(response):
        log_entry = {
            'url': request.base_url,
            'http_method': request.method,
            'status_code': response.status_code,
        }

        save_request_log(log_entry)

        return response


    app.run(debug=True)
