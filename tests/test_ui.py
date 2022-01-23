import allure


def test_ui(app):
    nominal_value_list = [500, 1000, 2000, 3000, 5000, 10000]
    with allure.step("Open home page"):
        app.open_home_page()
    with allure.step("Scroll home page till nominal block"):
        app.ui_actions.scroll_page_down_till_nominal()
    for nominal_value in nominal_value_list:
        with allure.step("When I click the {} nominal value button".format(nominal_value)):
            app.ui_actions.click_nominal(nominal_value)
        with allure.step("Then that button becomes enable"):
            assert app.ui_actions.check_enable_nominal_button(nominal_value)
        with allure.step("And then input field has chosen nominal value"):
            assert app.ui_actions.check_identity_nominal(nominal_value)
