import time
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.client_info_page import ClientInfoPage
from pages.payment_page import PaymentPage
from pages.thank_you_page import ThankYouPage


# @pytest.mark.run(order=1)
def test_select_product_1(set_up, set_group):

    driver = set_up

    print("")
    print("Start Test 1")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_1()

    cp = CartPage(driver)
    cp.confirm_product()

    cip = ClientInfoPage(driver)
    cip.enter_client_info()

    pp = PaymentPage(driver)
    pp.complete_payment()

    typ = ThankYouPage(driver)
    typ.thank_yoy_page()

    time.sleep(3)

    print("Finish Test 1")


# @pytest.mark.run(order=3)
def test_select_product_2(set_up):

    driver = set_up

    print("")
    print("Start Test 2")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_2()

    cp = CartPage(driver)
    cp.confirm_product()

    time.sleep(3)

    print("Finish Test 2")


# @pytest.mark.run(order=2)
def test_select_product_3(set_up):

    driver = set_up

    print("")
    print("Start Test 3")

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_product_3()

    cp = CartPage(driver)
    cp.confirm_product()

    time.sleep(3)

    print("Finish Test 3")
