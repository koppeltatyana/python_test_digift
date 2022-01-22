def test_ui(app):
    app.open_home_page()
    app.ui_actions.scroll_page_down_till_nominal()
    app.ui_actions.click_nominal_500()
