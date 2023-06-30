from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# utils ko elements.py
def get_element(driver, by_locator):
    return WebDriverWait(driver, 5).until(EC.visibility_of_element_located(by_locator))


# def click_element(driver, by_locator, locator_element):
#     element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.by_locator, locator_element)))
#     element.click()


def type_element(driver, by_locator, text):
    get_element(driver, by_locator).send_keys(text)


#
# def click_element(driver, by_locator):
#     get_element(driver, by_locator).click()

def click_element(driver, xpath):
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.click()

