from pages.digift_page import DigiftPageHelper


def test_click_on_all_nominal_buttons(app):
    digift_page = DigiftPageHelper(app)
    digift_page.go_to_site()
    digift_page.scroll_page_down_till_nominal()
    digift_page.click_all_nominals_and_check(digift_page.get_all_nominals())
