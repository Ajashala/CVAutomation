import time
from selenium.webdriver.common.by import By
from utils.elements import click_element
from utils.elements import type_element
from drivers.edge_driver import get_driver

driver = get_driver()


def navigate_dropdown(page):
    try:
        if page == "dashboard":
            click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[1]/ul/li[4]/div "))
            time.sleep(5)
        elif page == "profile":
            click_element(driver, (By.XPATH, "/html/body/div[2]/div[1]/header/div/nav/ul[2]/li[4]/div"))
            time.sleep(5)
        elif page == "grades":
            click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[1]/ul/li[4]/div"))
            time.sleep(5)
        elif page == "logout":
            click_element(driver,
                          (By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[1]/ul/li[4]/div"))
            time.sleep(5)

    except Exception as e:
        print(f"An exception occurred: {e}")


def dashboard():
    try:
        click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[1]/ul/li[4]/div/div/div[2]/a[1]"))
        time.sleep(5)

    except Exception as e:
        print(f"An exception occurred: {e}")


def profile():
    try:
        click_element(driver, (By.XPATH, "/ html / body / div[2] / div[1] / header / div / nav / ul[2] / li[4] / div "
                                         "/ div / div[2] / a[2]"))
        time.sleep(5)

    except Exception as e:
        print(f"An exception occurred: {e}")


def grades():
    try:
        click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[1]/ul/li[4]/div/div/div[2]/a[3]"))
        time.sleep(5)

    except Exception as e:
        print(f"An exception occurred: {e}")


def logout():
    try:
        click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[1]/ul/li[4]/div/div/div[2]/a[4]"))
        time.sleep(5)

    except Exception as e:
        print(f"An exception occurred: {e}")


# def navigate_dropdown2():
#     try:
#         click_element(driver, (By.XPATH, "/html/body/div[2]/div[1]/header/div/nav/ul[2]/li[4]/div"))
#         time.sleep(5)
#
#     except Exception as e:
#         print(f"An exception occurred: {e}")


# def profile():
#     try:
#         click_element(driver, (By.XPATH, "/ html / body / div[2] / div[1] / header / div / nav / ul[2] / li[4] / div "
#                                          "/ div / div[2] / a[2]"))
#         time.sleep(5)
#
#     except Exception as e:
#         print(f"An exception occurred: {e}")


# def navigate_dropdown3():
#     try:
#         click_element(driver, (By.XPATH, "/html/body/div[1]/div[1]/header/div/nav/ul[1]/ul/li[4]/div"))
#         time.sleep(5)
#
#     except Exception as e:
#         print(f"An exception occurred: {e}")
