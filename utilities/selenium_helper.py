class Selenium_Helper:
    def __init__(self, driver):
        self.driver = driver

    """set-up driver"""
    def initiate_driver(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(10)

    """quits driver after tests are completed"""
    def finsh_tests(self):
        self.driver.quit()