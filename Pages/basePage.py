from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def navigate_to(self,url):
        self.driver.get(url)

    def wait_and_find_element(self, locator_name, interval):
        return WebDriverWait(self.driver, interval).until(ec.presence_of_element_located(locator_name))

    def find_element(self, locator_name):
        return self.driver.find_element(*locator_name)