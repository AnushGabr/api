from base.base_api import BaseApi


class Products(BaseApi):
    get_products_endpoint = '/api_testing/product/read.php'
    post_products_endpoint = '/api_testing/product/create.php'
    get_single_product_endpoint = '/api_testing/product/read_one.php'
    update_product_endpoint = '/api_testing/product/update.php'
    delete_product_endpoint = '/api_testing/product/delete.php'

    def get_products(self, url, name):
        response = self.get_request(url + self.get_products_endpoint)
        list = self.check_json_value_by_key(response, '$.records..name')
        return list

    def getting_products_in_list_in_object_type(self, url):
        response = self.get_request(url + self.get_products_endpoint)
        single_product_id = self.get_json_object(response)

        return single_product_id
    def check_products_data_by_length(self, data):
        return len(data)

    def create_product(self, url, json_schema):
        response = self.post_request(url + self.post_products_endpoint, json_schema)
        return response

    def get_latest_created_product(self, url, id):
        response = self.get_request(url + self.get_single_product_endpoint, params=id)

        return response

    def editing_latest_added_product(self, url, json_schema):
        response = self.post_request(url + self.update_product_endpoint, json_schema)

        return response

    def deleting_added_product(self, url, json_schema):
        response = self.post_request(url + self.delete_product_endpoint, json_schema)

        return response



