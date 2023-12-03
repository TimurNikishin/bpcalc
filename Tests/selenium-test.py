from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TEST_URL = "http://bpcalcqa.ntcyber.net"

driver = webdriver.Chrome()

driver.get(TEST_URL)

systolic = driver.find_element(By.ID, "systolic")
systolic.send_keys("110")

diastolic = driver.find_element(By.ID, "diastolic")
diastolic.send_keys("60")

diastolic.send_keys(Keys.RETURN)

result = driver.find_element(By.CLASS_NAME, "alert").get_attribute('innerHTML')

try:
    assert 'Ideal blood pressure' in result
    print('E2E test passed')
except AssertionError:
    print('E2E test failed')
