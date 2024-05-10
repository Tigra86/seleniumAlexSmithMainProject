import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage


def test_select_product():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)

    login = LoginPage(driver)
    login.authorization()

    enter_shopping_cart = wait.until(EC.element_to_be_clickable(("id", "shopping_cart_container")))
    enter_shopping_cart.click()
    print("Enter shopping cart")
    time.sleep(3)
