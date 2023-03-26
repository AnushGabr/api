from endpoints.products import Products
from json_models import create_product_json


def test_get_products(app_config):
    products = Products()
    product_list = products.get_products(app_config.base_url, "Polo Shirt")
    assert products.check_products_data_by_length(product_list) == 18


def test_product_is_created(app_config):
    products = Products()

    json_schema = create_product_json.create_product_json('Apple', 'this is fruit', 19, 500)
    assert products.create_product(app_config.base_url, json_schema).status_code == 201


def test_is_latest_product_created(app_config):
    product = Products()
    product_id = product.getting_products_in_list_in_object_type(app_config.base_url)
    latest_product = product.get_latest_created_product(app_config.base_url, f'id={product_id}')

    assert product.check_json_value_by_key(latest_product, '$.id') == [f'{product_id}']


def test_product_update(app_config):
    product = Products()
    product_id = product.getting_products_in_list_in_object_type(app_config.base_url)
    json_schema = create_product_json.json_for_product_update(f'{product_id}', 'berry')
    assert product.editing_latest_added_product(app_config.base_url, json_schema).status_code == 200


def test_is_product_deleted(app_config):
    product = Products()
    product_id = product.getting_products_in_list_in_object_type(app_config.base_url)
    json_schema = create_product_json.json_for_product_update(f'{product_id}', 'berry')

    product.deleting_added_product(app_config.base_url, json_schema)
