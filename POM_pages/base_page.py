from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage():

    def  __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, URL):
        self.driver.get(URL)

    """Clicks on element given locator"""
    def click_on(self, by_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            element.click()
        
        except TimeoutException:
            print('Timedout: Element was not found or clickable')

    """Returns True if an elment is visible"""
    def is_visible(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        return bool(element)