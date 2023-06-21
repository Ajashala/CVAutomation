import pytest
from drivers.edge_driver import get_driver
from pages.login_page import login_values
from pages.base_page import url_open

driver = get_driver()


@pytest.fixture(scope='module')
def test_valid_data():
    url_open()
    login_values("pramod", "Pramod12!@")

#
# def test_invalid_data():
#     url_open()
#     login_values("pramod2", "Pramod12!@")


# invalid function how to do


def test_run_test(test_valid_data):
    assert 'ChimpVine' == driver.title
