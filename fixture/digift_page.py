from fixture.digift_page_actions import DigiftPageHelper
from selenium import webdriver


class DigiftPage:

    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.base_url = base_url
        self.ui_actions = DigiftPageHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def destroy(self):
        self.wd.quit()
