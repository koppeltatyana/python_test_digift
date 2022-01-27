from locators.locators import Locators
from pages.base_page import BasePage
import allure


class DigiftPageHelper(BasePage):

    def get_all_nominals(self):
        return list(map(lambda x: x.text, self.find_elements(Locators.NOMINAL_VALUE)))

    def scroll_page_down_till_nominal(self):
        with allure.step("Scroll home page till nominal block"):
            # скролл страницы вниз до элемента 'Номинал карты'
            self.wd.execute_script("return arguments[0].scrollIntoView(true);", self.find_element(Locators.CARD_NOMINAL_VALUE_TEXT))

    def click_nominal(self, nominal_value):
        with allure.step("When I click the '{}' nominal value button".format(nominal_value)):
            for element in self.find_elements(Locators.NOMINAL_VALUE):
                if element.text == nominal_value:
                    element.click()

    def get_range_value_text(self):
        return self.find_element(Locators.INPUT_RANGE_VALUE).get_attribute('value')

    def check_identity_nominal(self, nominal_value):
        with allure.step("And then input field has chosen nominal value"):
            assert str(nominal_value) == self.get_range_value_text()

    def check_enable_nominal_button(self, nominal_value):
        with allure.step("Then that button becomes enable"):
            """ Если кнопка активна, то у нее есть класс  'par-options__button--active' - проверяем это """
            for element in self.find_elements(Locators.NOMINAL_VALUE):
                if element.text == nominal_value:
                    assert "par-options__button--active" in element.get_attribute("class")

    def click_all_nominals_and_check(self, nominal_list):
        for nominal in nominal_list:
            self.click_nominal(nominal)
            self.check_enable_nominal_button(nominal)
            self.check_identity_nominal(nominal)
