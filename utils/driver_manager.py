from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as GeckoService

chrome_driver_path = r"C:\drivers\chromedriver_win32\chromedriver.exe"
edge_driver_path = r"C:\drivers\edgedriver_win64\msedgedriver.exe"
gecko_driver_path = r"C:\drivers\geckodriver-v0.33.0-win64\geckodriver.exe"

# chrome_service = ChromeService(executable_path=chrome_driver_path)
edge_service = EdgeService(executable_path=edge_driver_path)
# gecko_service = GeckoService(executable_path=gecko_driver_path)

#
# chrome_options = webdriver.ChromeOptions()
# chrome_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

edge_options = webdriver.EdgeOptions()
edge_driver = webdriver.Edge(service=edge_service, options=edge_options)

# gecko_options = webdriver.FirefoxOptions()
# gecko_driver = webdriver.Firefox(service=gecko_service, options=gecko_options)
