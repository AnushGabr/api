import pytest

from config import Config
from endpoints.categories import Categories


def test_get_category(app_config):
    category = Categories()
    category.get_categories(app_config.base_url, 200, 'Suppplements')


def test_post_category(app_config):
    category = Categories()
    schema = {"id": 300, "name": "Change", "description": "testing changes"}
    category.post_categories(app_config.base_url, schema)


def test_put_category(app_config):
    category = Categories()
    schema = {"id": 3, "name": "Change", "description": "testing changes"}
    category.put_categories(app_config.base_url, schema)