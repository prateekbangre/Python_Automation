from selenium import webdriver


def create_chrome_profile():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path="drivers/chromedriver", chrome_options=chrome_options)
    driver.maximize_window()

    return driver


def create_firefox_profile():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--ignore-certificate-errors')
    firefox_options.add_argument("--test-type")
    firefox_options.add_argument("--start-maximized")
    firefox_options.add_argument("--disable-extensions")
    driver = webdriver.Firefox(executable_path="drivers/geckodriver", firefox_options=firefox_options)
    driver.maximize_window()

    return driver


def get_driver(driver_name):

    if driver_name == "CHROME":
        return create_chrome_profile()
    elif driver_name == "FIREFOX":
        return create_firefox_profile()
    else:
        return ""
