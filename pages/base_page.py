import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, wd):
        self.wd = wd
        self.base_url = "http://HR:test@qa.digift.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.wd, time).until(EC.presence_of_element_located(locator),
                                                  message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.wd, time).until(EC.presence_of_all_elements_located(locator),
                                                  message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        with allure.step("Open home page"):
            return self.wd.get(self.base_url)
