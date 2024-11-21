from selenium.webdriver.common.by import By
from POM_pages.base_page import BasePage

class LoginLocators():
    LOGIN_EMAIL_TEXTBOX = (By.CSS_SELECTOR,'.login-form > form:nth-child(2) > input:nth-child(2)')
    LOGIN_PWD_TEXTBOX = (By.CSS_SELECTOR, '.login-form > form:nth-child(2) > input:nth-child(3)')

    SIGNUP_NAME_TEXTBOX = (By.CSS_SELECTOR,'.signup-form > form:nth-child(2) > input:nth-child(2)')
    SIGNUP_EMAIL_TEXTBOX = (By.CSS_SELECTOR,'.signup-form > form:nth-child(2) > input:nth-child(3)')

    LOGIN_BTN = (By.CSS_SELECTOR,'button.btn:nth-child(4)')
    SIGNUP_BTN = (By.CSS_SELECTOR,'button.btn:nth-child(5)')

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def click_signup(self):
        self.click_on(LoginLocators.SIGNUP_BTN)


    def input_signup_name(self, username):
        self.driver.find_element(*LoginLocators.SIGNUP_NAME_TEXTBOX).send_keys(username)

    def input_signup_email(self, email):
        self.driver.find_element(*LoginLocators.SIGNUP_EMAIL_TEXTBOX).send_keys(email)


    
