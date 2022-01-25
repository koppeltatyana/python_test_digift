from model.JsTestTask import JsTestTask


def test_api(api):
    request_result = api.get_js_test_task(search_field="Alcatel", sort_field="name")
    assert request_result == sorted(request_result, key=JsTestTask.sort_key)
    assert api.check_substr_in_names(api.get_names_from_response(request_result), 'Alcatel')
