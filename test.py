from selenium import webdriver
import drivers.CreateProfile as createProfile
import time

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument("--test-type")
# chrome_options.add_argument("--start-maximized")
# drivers = webdriver.Chrome(executable_path="drivers/chromedriver", options=chrome_options)
driver = createProfile.get_driver("CHROME")
driver.get('http://codepad.org')

text_area = driver.find_element_by_id('textarea')
text_area.send_keys("This text is send using Python code.")

time.sleep(3)
driver.quit()
