import time
import pytest
from selenium.webdriver.common.by import By
from utils.driver_manager import edge_driver
from pages.login_page import click_element
from pages.login_page import type_element


@pytest.fixture(scope='module')
def driver():
    yield edge_driver


def test_url(driver):
    driver.get("https://np.chimpvine.com/login/index.php")
    assert 'ChimpVine: Log in to the site' == driver.title
    time.sleep(5)


def test_login(driver, username, password, success=True):
    try:
        type_element(driver, (By.ID, "login_username"), username)
        type_element(driver, (By.ID, "login_password"), password)
        click_element(driver, (By.ID, "login-submit"))
        time.sleep(5)
        if success:
            assert 'https://np.chimpvine.com/' == driver.current_url
        else:
            assert driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/form/div[3]").is_displayed()
        time.sleep(5)
    except Exception as e:
        print(f"An exception occurred: {e}")


def test_login_scenarios(driver):
    test_login(driver, "pramod", "Pramod12!@", success=True)
    test_login(driver, "parmod", "Pramod12!@", success=False)

# def test_failed_login(driver):
#     type_element(driver, (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/form/div[1]/input"), "parmod")
#     type_element(driver, (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/form/div[2]/input"), "Pra")
#     click_element(driver, (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/form/button"))
#     time.sleep(5)
#     assert driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/form/div[3]").is_displayed()
#     time.sleep(5)

# def test_login(driver):
#     type_element(driver,(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[1]/div/label/input"),"asajala")
#     type_element(driver,(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/label/input"),"s@r@ngh@j@")
#     click_element(driver,(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[3]/button/div"))
#     time.sleep(4)
#     assert driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[2]/p").is_displayed()
#     time.sleep(4)
