from base.base_api import BaseApi


class Products(BaseApi):
    get_products_endpoint = '/api_testing/product/read.php'
    post_products_endpoint = '/api_testing/product/create.php'

    def get_products(self, url, expected_product):
        response = self.get_request(url + self.get_products_endpoint)
        list = self.check_json_value_by_key(response, '$.records..id')
        return list
        #exp_value = self.get_value_from_list(list, expected_product)

    def check_products_data_by_length(self, data):
        return len(data)

    def create_product(self, url, json_schema):
        response = self.post_request(url + self.post_products_endpoint, json_schema)

    def checking_product_was_created(self):
        pass
