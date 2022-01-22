from selenium.webdriver.common.by import By


class Locators:

    CARD_NOMINAL_VALUE_TEXT = (By.CSS_SELECTOR, "h3.par__title.lined-title.lined-title--left")
    NOMINAL_VALUE = (By.CLASS_NAME, "par-options__button")
    # NOMINAL_500 = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::nobr[1]")
    INPUT_RANGE_VALUE = (By.ID, "range-value-input")
