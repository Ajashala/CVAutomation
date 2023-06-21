import time
import pytest
from drivers.edge_driver import get_driver
from pages.base_page import url_open

driver = get_driver()


@pytest.fixture(scope='module')
def test_url():
    url_open()
    time.sleep(5)


def test_run_test(test_url):
    assert 'ChimpVine: Log in to the site' == driver.title