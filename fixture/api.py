import requests
from model.JsTestTask import JsTestTask


class ApiHelper:

    def __init__(self, api_url):
        self.api_url = api_url

    def convert_json_responce_to_model(self, json_products):
        def convert(json_products):
            return JsTestTask(name=str(json_products['name']), price=json_products['price'], image=json_products['image'])
        return list(map(convert, json_products))

    def get_js_test_task(self, search_field=None, sort_field=None):
        request_parameters = {'search_field': search_field, 'sort_field': sort_field}
        try:
            response = requests.get(self.api_url + 'js-test-task', request_parameters)
            json_response_products = response.json()['products']
            return self.convert_json_responce_to_model(json_response_products)

        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
