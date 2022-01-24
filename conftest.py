import pytest
from fixture.digift_page import DigiftPage
from fixture.api import ApiHelper


fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = DigiftPage(base_url="http://HR:test@qa.digift.ru/")  # 'HR:test@' для прохождения базовой аутентификации на странице

    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def api():
    api_fixture = ApiHelper(api_url='https://www.lenvendo.ru/api/')
    return api_fixture
