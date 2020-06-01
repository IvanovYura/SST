from flask import render_template, make_response
from flask_restx import Namespace, Resource

from service.utils import get_metrics

ns = Namespace(
    name='Importer',
    path='/',
)

parser = ns.parser()
parser.add_argument(
    'limit',
    type=int,
    required=False,
    help='Number of rows to return',
)


@ns.route('/metrics')
class Api(Resource):
    @ns.hide
    def get(self):
        """
        Returns metrics from DB in HTML format
        """
        args = parser.parse_args()
        limit = args['limit']

        metrics = get_metrics(limit)

        html = render_template('index.html', len=len(metrics), metrics=metrics)

        return make_response(html)
