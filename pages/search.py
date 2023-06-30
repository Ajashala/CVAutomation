import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.elements import click_element
from utils.elements import type_element
from drivers.edge_driver import get_driver

driver = get_driver()


def search_page():
    try:
        #click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[2]/li/div/a"))
        click_element(driver, "//a[@id='search-button-listener']")
    except Exception as e:
        print(f"An exception occurred: {e}")


def search_values(search):
    try:
        if search == "valid_search":
            type_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/input[1]"),
                         "english")
            #click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/i/input"))
            click_element(driver, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/i/input")
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                             "/html/body/div[1]/div[1]/div[5]/div["
                                                                             "3]/div["
                                                                             "2]/div/div/div/div/div/div/div/div["
                                                                             "1]/div/ul/li[2]")))

        elif search == "interactive_course":

            #click_element(driver, (By.CLASS_NAME,"type-data activehr"))
            click_element(driver, "type-data activehr")
            type_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/input[1]"),
                         "english")
            #click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/i/input"))
            click_element(driver, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/i/input")
            time.sleep(5)

        elif search == "interactive_books":
            type_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/input[1]"),
                         "interactive book")
            #click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/i/input"))
            click_element(driver, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/i/input")
            time.sleep(5)

        elif search == "blogs":
            type_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/input[1]"),
                         "blogs")
            #click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/i/input"))
            click_element(driver, "/html/body/div[1]/div[1]/div[4]/div/div/div/div/fieldset/i/input")
            time.sleep(5)

    except Exception as e:
        print(f"An exception occurred: {e}")
