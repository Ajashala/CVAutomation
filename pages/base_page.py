import time

from drivers.edge_driver import get_driver

driver = get_driver()


def url_open():
    driver.get("https://np.chimpvine.com/login/index.php")
    time.sleep(5)


def register_url():
    driver.get("https://np.chimpvine.com/login/signup.php")
    time.sleep(5)
