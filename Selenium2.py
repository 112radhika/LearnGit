# https://rahulshettyacademy.com/angularpractice/
# https://rahulshettyacademy.com/client
# https://rahulshettyacademy.com/dropdownsPractise/
# https://rahulshettyacademy.com/seleniumPractise/#/
# https://rahulshettyacademy.com/AutomationPractice/
# https://the-internet.herokuapp.com/windows


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# ID, name, xpath, css selector, link text, class name - locators
#driver.find_element(By.NAME,"name").send_keys("Radz Test")
#driver.find_element(By.NAME,"email").send_keys("test@test.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Pass123")
driver.find_element(By.ID,"exampleCheck1").click()

# STATIC DROPDOWN
# If the HTML has select tag then it is static dropdown.
# Select class is used to identify the static dropdown.
# select by index, value, visible text are different options available
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "#exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Female")
#dropdown.select_by_value("male")

# XPATH - //tagname[@attribute='value']
# XPATH - //parent_tagname/child_tagname - parent to child traversal using tagname
# XPATH - //tagname[text()='value'] - identify element using text
# XPATH - //tagname[contains(@attribute,'value'] - using regular expression

# CSS - tagname[attribute='value']
# CSS - #id
# CSS - .classname
# CSS - parent_tagname child_tagname - parent to child traversal using tagname.
# In CSS space should be used instead of / (/ is used in XPATH)
# CSS - tagname[attribute*='value'] - using regular expression

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("radztest")
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("test123@test.com")
driver.find_element(By.CSS_SELECTOR,"#inlineRadio2").click()
driver.find_element(By.CSS_SELECTOR,".btn-success").click()
message = driver.find_element(By.CSS_SELECTOR,".alert-success").text
print(message)
assert 'Success' in message
time.sleep(2)

