def test_ui(app):
    nominal_value_list = [500, 1000, 2000, 3000, 5000, 10000]
    app.open_home_page()
    app.ui_actions.scroll_page_down_till_nominal()
    for nominal_value in nominal_value_list:
        app.ui_actions.click_nominal(nominal_value)
        assert app.ui_actions.check_enable_nominal_button(nominal_value)
        assert app.ui_actions.check_identity_nominal(nominal_value)
