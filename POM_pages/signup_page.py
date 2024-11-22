from selenium.webdriver.common.by import By
from POM_pages.base_page import BasePage

class SignUp_Locators:
    TITLE_MR = (By.CSS_SELECTOR, '#id_gender1')
    TITLE_MRS = (By.CSS_SELECTOR, '#id_gender2')
    SIGNUP_PW_TEXTBOX = (By.CSS_SELECTOR,'#password')

class SignUpPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def click_title(self,title):
        title = title.lower()
        match title:
            case 'mr':
                self.click_on(SignUp_Locators.TITLE_MR)

            case 'mrs':
                self.click_on(SignUp_Locators.TITLE_MRS)

    def input_signup_password(self, password):
        ...



