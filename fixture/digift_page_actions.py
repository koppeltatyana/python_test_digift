from fixture.locators import Locators
import time


class DigiftPageHelper:

    def __init__(self, app):
        self.app = app

    def scroll_page_down_till_nominal(self):
        wd = self.app.wd
        wd.execute_script("return arguments[0].scrollIntoView(true);", wd.find_element(*Locators.CARD_NOMINAL_VALUE_TEXT))
        time.sleep(2)


