from selenium.webdriver.common.by import By


class Locators:

    CARD_NOMINAL_VALUE_TEXT = (By.CSS_SELECTOR, "h3.par__title.lined-title.lined-title--left")
    NOMINAL_500 = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::nobr[1]")
    NOMINAL_1000 = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::nobr[2]")
    NOMINAL_2000 = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::nobr[3]")
    NOMINAL_3000 = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::nobr[4]")
    NOMINAL_5000 = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::nobr[5]")
    NOMINAL_10000 = (By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Выберите:'])[1]/following::nobr[6]")
    INPUT_RANGE_VALUE = (By.ID, "range-value-input")
