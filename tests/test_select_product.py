import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.payment_page import PaymentPage
from pages.thank_you_page import ThankYouPage


def test_select_product():
    driver = webdriver.Chrome()

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product()

    cp = CartPage(driver)
    cp.confirm_product()

    cip = ClientInfoPage(driver)
    cip.enter_client_info()

    pp = PaymentPage(driver)
    pp.complete_payment()

    typ = ThankYouPage(driver)
    typ.thank_yoy_page()

    time.sleep(3)
