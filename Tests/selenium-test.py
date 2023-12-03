from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
#from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

TEST_URL = "http://bpcalcqa.ntcyber.net"

options = webdriver.ChromeOptions()
options.headless = True

# options.add_experimental_option("detach", True)

with webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options) as driver:
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


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
#driver = webdriver.Chrome()

#driver.get(TEST_URL)



# if 'Ideal blood pressurre' in result:
#     print("OK")

# links = driver.find_element(By.ID, 'systolic')
# for link in links:
#      print(link.get_attribute('min'))
    