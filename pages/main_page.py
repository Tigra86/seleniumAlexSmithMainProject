from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_1 = ("id", "add-to-cart-sauce-labs-backpack")
    cart_icon = ("id", "shopping_cart_container")

    # Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.product_1))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.cart_icon))

    # Actions
    def select_product_1(self):
        self.get_product_1().click()
        print("Select Sauce Labs backpack")

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print("Click cart icon")

    # Methods
    def select_product(self):
        self.get_current_url()
        self.select_product_1()
        self.click_cart_icon()