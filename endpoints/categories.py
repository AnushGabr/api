from base.base_api import BaseApi


class Categories(BaseApi):
    get_category_endpoint = '/api_testing/category/read.php'
    put_category_endpoint = '/api_testing/category/update.php'

    def get_categories(self, url, expected_status_code, expected_category):
        response = self.get_request(url + self.get_category_endpoint)
        self.check_status_code(response, expected_status_code)
        list = self.check_json_value_by_key(response, '$.records..name')
        exp_value = self.get_value_from_list(list, expected_category)
        print(exp_value)

    def post_categories(self, url, json_schema):
        response = self.post_request(url + self.get_category_endpoint, json_schema)

    def put_categories(self, url, json_schema):
        response = self.post_request(url + self.put_category_endpoint, json_schema)

    def delete_categories(self):
        pass
