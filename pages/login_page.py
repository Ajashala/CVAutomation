import time
from selenium.webdriver.common.by import By
from utils.elements import click_element
from utils.elements import type_element
from drivers.edge_driver import get_driver

driver = get_driver()


def login_values(username, password):
    try:
        type_element(driver, (By.ID, "login_username"), username)
        type_element(driver, (By.ID, "login_password"), password)
        click_element(driver, (By.ID, "login-submit"))
        time.sleep(5)

    except Exception as e:
        print(f"An exception occurred: {e}")
