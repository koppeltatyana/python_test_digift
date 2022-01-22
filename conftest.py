import pytest
from fixture.digift_page import DigiftPage

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
