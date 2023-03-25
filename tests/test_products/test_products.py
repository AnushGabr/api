from endpoints.products import Products
from json_models import create_product_json
def test_get_products(app_config):
    products = Products()
    product_list = products.get_products(app_config.base_url, "Polo Shirt")
    assert products.check_products_data_by_length(product_list) == 20

def test_product_is_created(app_config):
    products = Products()
    json_schema = {
    "name": "Multi-Vitamin (900 capsules)",
    "description": "A daily dose of our Multi-Vitamins fulfills a day’s nutritional needs for over 12 vitamins and minerals.",
    "price": "50.00000",
    "category_id": 230000,
    "category_name": "Supplements"
    }
    products.create_product(app_config.base_url, json_schema)