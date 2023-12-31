import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


TEST_URL = "http://bpcalcqa.ntcyber.net"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
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
    driver.quit
except AssertionError:
    print('E2E test failed')
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)