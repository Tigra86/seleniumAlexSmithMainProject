from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class ClientInfoPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name = ("id", "first-name")
    last_name = ("id", "last-name")
    postal_code = ("id", "postal-code")
    continue_button = ("id", "continue")

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.first_name))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.last_name))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.postal_code))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.continue_button))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Enter first name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Enter last name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Enter postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click Continue button")

    # Methods
    def enter_client_info(self):
        self.get_current_url()
        self.input_first_name("Tigran")
        self.input_last_name("Azaryan")
        self.input_postal_code("94132")
        self.click_continue_button()
