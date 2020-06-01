from unittest import mock

from flask import render_template

from tests.base import TestBase


class ApiTest(TestBase):
    API_URL_PREFIX = '/api/v1'

    def get_url(self, limit: int = None):
        url = f'{self.API_URL_PREFIX}/metrics'
        if limit:
            url += f'?limit={limit}'

        return url

    @mock.patch('service.api.get_metrics')
    def test_get_metrics(self, get_metrics_mock):
        get_metrics_mock.return_value = self.data

        url = self.get_url()

        response = self.get(url)

        with self.app.app_context() as _:
            html = render_template('index.html', len=len(self.data), metrics=self.data)

        self.assertEqual(200, response.status_code)
        self.assertEqual(html, response.data.decode('utf-8'))

    @mock.patch('service.api.get_metrics')
    def test_get_metrics_with_limit(self, get_metrics_mock):
        data = self.data[:1]
        get_metrics_mock.return_value = data

        url = self.get_url(1)

        response = self.get(url)

        with self.app.app_context() as _:
            html = render_template('index.html', len=len(data), metrics=data)

        self.assertEqual(200, response.status_code)
        self.assertEqual(html, response.data.decode('utf-8'))
