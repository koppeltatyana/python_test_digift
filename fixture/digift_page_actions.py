from fixture.locators import Locators
import time


class DigiftPageHelper:

    # словарь соответствия порядкового номера кнопки и номинала кнопки
    nominal_dict = {500: 0, 1000: 1, 2000: 2, 3000: 3, 5000: 4, 10000: 5}

    def __init__(self, app):
        self.app = app

    def scroll_page_down_till_nominal(self):
        wd = self.app.wd
        # скролл страницы вниз до элемента 'Номинал карты'
        wd.execute_script("return arguments[0].scrollIntoView(true);", wd.find_element(*Locators.CARD_NOMINAL_VALUE_TEXT))
        time.sleep(2)

    def click_nominal(self, nominal_value):
        wd = self.app.wd
        wd.find_elements(*Locators.NOMINAL_VALUE)[self.nominal_dict[nominal_value]].click()

    def get_range_value_text(self):
        wd = self.app.wd
        return wd.find_element(*Locators.INPUT_RANGE_VALUE).get_attribute('value')

    def check_identity_nominal(self, nominal_value):
        return str(nominal_value) == self.get_range_value_text()

    def check_enable_nominal_button(self, nominal_value):
        """ Если кнопка активна, то у нее есть класс  'par-options__button--active' - проверяем это """
        wd = self.app.wd
        nominal_value_button_classes = wd.find_elements(*Locators.NOMINAL_VALUE)[self.nominal_dict[nominal_value]].get_attribute("class")
        return "par-options__button--active" in nominal_value_button_classes
