import time
from selenium.webdriver.common.by import By
from utils.elements import click_element
from utils.elements import type_element
from drivers.edge_driver import get_driver

driver = get_driver()


def register_values(email, username, password, cpassword):
    try:
        type_element(driver, (By.XPATH, "//*[@id='id_email']"), email)
        type_element(driver, (By.XPATH, "//*[@id='id_username']"), username)
        type_element(driver, (By.XPATH, "//*[@id='id_password']"), password)
        type_element(driver, (By.XPATH, "//*[@id='id_confirm_password']"), cpassword)
        click_element(driver, (By.XPATH, "//*[@id='Check1']"))
        click_element(driver, (By.XPATH, "//*[@id='register-submit']"))
        time.sleep(5)

    except Exception as e:
        print(f"An exception occurred: {e}")