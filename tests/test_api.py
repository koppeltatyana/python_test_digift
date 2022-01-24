from model.JsTestTask import JsTestTask


def test_api(api):
    request_result = api.get_js_test_task(search_field="Alcatel", sort_field="name")
    products_names = api.get_names_from_response(request_result)
    assert request_result == sorted(request_result, key=JsTestTask.sort_key)
    assert api.check_Alcatel_in_names(products_names)
