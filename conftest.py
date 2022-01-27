import pytest
from selenium import webdriver
from api.api_helper import ApiHelper


@pytest.fixture(scope="session")
def app():
    wd = webdriver.Chrome()
    yield wd
    wd.quit()


@pytest.fixture(scope="session")
def api():
    api_fixture = ApiHelper(api_url='https://www.lenvendo.ru/api/')
    return api_fixture
