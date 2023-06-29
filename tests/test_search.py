import pytest
from drivers.edge_driver import get_driver
from pages.login_page import login_values
from pages.base_page import url_open
from pages.search import search_page
from pages.search import search_values

driver = get_driver()


@pytest.fixture(scope='module')
def test_open():
    driver.maximize_window()
    url_open()
    login_values("pramod", "Pramod12!@")
    yield driver
    # navigate_dropdown()


def test_search_game(test_open):
    search_page()
    search_values("valid_search")
    assert "https://np.chimpvine.com/filters/filter.php?type=games&query=english" == driver.current_url


def test_search_interactive_course(test_open):
    search_page()
    search_values("interactive_course")


def test_search_books(test_open):
    search_page()
    search_values("interactive_books")


def test_search_blogs(test_open):
    search_page()
    search_values("blogs")
