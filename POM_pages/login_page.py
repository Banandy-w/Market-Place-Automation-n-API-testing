from selenium.webdriver.common.by import By

class LoginLocators():
    LOGIN_EMAIL_TEXTBOX = (By.CSS_SELECTOR,'.login-form > form:nth-child(2) > input:nth-child(2)')
    LOGIN_PWD_TEXTBOX = (By.CSS_SELECTOR, '.login-form > form:nth-child(2) > input:nth-child(3)')

    SIGNUP_NAME_TEXTBOX = (By.CSS_SELECTOR,'.signup-form > form:nth-child(2) > input:nth-child(2)')
    SIGNUP_EMAIL_TEXTBOX = (By.CSS_SELECTOR,'.signup-form > form:nth-child(2) > input:nth-child(3)')

    LOGIN_BTN = (By.CSS_SELECTOR,'button.btn:nth-child(4)')
    SIGNUP_BTN = (By.CSS_SELECTOR,'button.btn:nth-child(5)')

class LoginPage():
    def __init__(self,driver):
        super().__init__(driver)

    
