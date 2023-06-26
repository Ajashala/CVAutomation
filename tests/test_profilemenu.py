import pytest
from drivers.edge_driver import get_driver
from pages.login_page import login_values
from pages.base_page import url_open
from pages.profile_menu import navigate_dropdown, grades, profile
from pages.profile_menu import dashboard
from pages.profile_menu import logout

driver = get_driver()


@pytest.fixture(scope='module')
def test_open():
    driver.maximize_window()
    url_open()
    login_values("pramod", "Pramod12!@")
    yield driver
    # navigate_dropdown()


def test_dashboard(test_open):
    navigate_dropdown("dashboard")
    dashboard()
    print("Dropdown opened")
    assert 'Dashboard' == driver.title
    print("Navigated to the dashboard")


def test_profile(test_open):
    navigate_dropdown("profile")
    profile()
    print("Dropdown opened")
    assert 'Pramod Yadav: Public profile' == driver.title


def test_grades(test_open):
    navigate_dropdown("grades")
    grades()
    print("Dropdown opened")
    assert 'Grades - Pramod Yadav' == driver.title


def test_logout(test_open):
    navigate_dropdown("logout")
    logout()
    print("Dropdown opened")
    assert 'ChimpVine: Log in to the site' == driver.title

# def test_invalid_data():
#     url_open()
#     login_values("pramod2", "Pramod12!@")


# invalid function how to do


# def test_run_test(test_open):
#     assert 'ChimpVine' == driver.title
