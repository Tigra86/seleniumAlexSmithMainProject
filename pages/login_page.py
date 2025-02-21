from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    user_name = ("id", "user-name")
    password = ("id", "password")
    login_button = ("id", "login-button")
    page_title = ("xpath", "//span[@class='title']")

    # Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.user_name))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.password))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.login_button))

    def get_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.page_title)).text

    # Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Enter user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Enter password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")

    # Methods
    def authorization(self):
        self.get_current_url()
        self.input_user_name("standard_user")
        self.input_password("secret_sauce")
        self.click_login_button()
        self.assert_page_title_text(self.get_page_title(), "Products")
