import pytest
from drivers.edge_driver import get_driver
from pages.register_page import register_values
from pages.base_page import register_url

driver = get_driver()


@pytest.fixture(scope='module')
def test_valid_data():
    register_url()
    register_values("test6777@gmail.com", "user6777", "Admin@123", "Admin@123")


def test_run_test(test_valid_data):
    assert 'https://np.chimpvine.com/login/index.php' == driver.current_url
