from fixture.locators import Locators
import time


class DigiftPageHelper:

    def __init__(self, app):
        self.app = app

    def scroll_page_down_till_nominal(self):
        wd = self.app.wd
        wd.execute_script("return arguments[0].scrollIntoView(true);", wd.find_element(*Locators.CARD_NOMINAL_VALUE_TEXT))
        time.sleep(2)

    def click_nominal_500(self):
        wd = self.app.wd
        wd.find_element(*Locators.NOMINAL_500).click()

    def click_nominal_1000(self):
        wd = self.app.wd
        wd.find_element(*Locators.NOMINAL_1000).click()

    def click_nominal_2000(self):
        wd = self.app.wd
        wd.find_element(*Locators.NOMINAL_2000).click()

    def click_nominal_3000(self):
        wd = self.app.wd
        wd.find_element(*Locators.NOMINAL_3000).click()

    def click_nominal_5000(self):
        wd = self.app.wd
        wd.find_element(*Locators.NOMINAL_5000).click()

    def click_nominal_10000(self):
        wd = self.app.wd
        wd.find_element(*Locators.NOMINAL_10000).click()
