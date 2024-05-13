from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    product_1 = ("id", "add-to-cart-sauce-labs-backpack")
    product_2 = ("id", "add-to-cart-sauce-labs-bike-light")
    product_3 = ("id", "add-to-cart-sauce-labs-bolt-t-shirt")
    cart_icon = ("id", "shopping_cart_container")
    burger_menu_button = ("id", "react-burger-menu-btn")
    about_link = ("id", "about_sidebar_link")

    # Getters
    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.product_1))

    def get_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.product_2))

    def get_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.product_3))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.cart_icon))

    def get_burger_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.burger_menu_button))

    def get_about_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.about_link))

    # Actions
    def click_select_product_1(self):
        self.get_product_1().click()
        print("Click select product 1")

    def click_select_product_2(self):
        self.get_product_2().click()
        print("Click select product 2")

    def click_select_product_3(self):
        self.get_product_3().click()
        print("Click select product 3")

    def click_cart_icon(self):
        self.get_cart_icon().click()
        print("Click cart icon")

    def click_burger_menu_button(self):
        self.get_burger_menu_button().click()
        print("Click burger menu button")

    def click_about_link(self):
        self.get_about_link().click()
        print("Click about link")

    # Methods
    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart_icon()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart_icon()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart_icon()

    def select_about_link(self):
        self.get_current_url()
        self.click_burger_menu_button()
        self.click_about_link()
        self.assert_url("https://saucelabs.com/")
