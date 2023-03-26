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


def json_for_product_update(id, name):
    data = {
        'id': id,
        'name': name
    }

    json_data = json.dumps(data)
    return json_data



