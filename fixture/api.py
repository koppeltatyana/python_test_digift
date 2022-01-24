import requests
from model.JsTestTask import JsTestTask


class ApiHelper:

    def __init__(self, api_url):
        self.api_url = api_url

    def convert_json_to_model(self, json):
        def convert(json):
            return JsTestTask(name=str(json['name']), price=json['price'], image=json['image'])
        return list(map(convert, json))

    def get_names_from_response(self, products_list):
        names_list = []
        for product in products_list:
            names_list += [product.name]
        return names_list

    def check_Alcatel_in_names(self, names_list):
        flag = True
        for name in names_list:
            if 'Alcatel' not in name:
                flag = False
        return flag

    def get_js_test_task(self, search_field=None, sort_field=None):
        request_parameters = {'search_field': search_field, 'sort_field': sort_field}
        try:
            response = requests.get(self.api_url + 'js-test-task', request_parameters)
            json_response_products = response.json()['products']
            return self.convert_json_to_model(json_response_products)
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
