import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service_obj = Service("C:\\users\112ra\downloads\Chromedrive")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(2)