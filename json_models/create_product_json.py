import json


def create_product_json(name, description, category_id, price):
    data = {
        'name': name,
        'description': description,
        'price': price,
        'category_id': category_id,
    }

    json_data = json.dumps(data)
    return json_data
