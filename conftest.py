import pytest
from fixture.digift_page import DigiftPage

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = DigiftPage(base_url="http://qa.digift.ru/")

    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
