import csv
import os
from unittest import TestCase

from service.app import create_app
from service.config import TestConfig

config = TestConfig()


class TestBase(TestCase):
    def setUp(self):
        self.app = create_app(config)
        self.client = self.app.test_client()

        self._prepare_test_data(10)

    def _prepare_test_data(self, rows):
        result = []
        with open(os.path.join(config.PROJECT_ROOT, 'resources', 'task_data.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i >= rows:
                    break

                result.append(row)

            self.data = result

    def get(self, url, **kwargs):
        return self.client.get(url, **kwargs)
