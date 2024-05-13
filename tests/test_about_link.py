import time
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_about_link(set_up):

    driver = set_up

    login = LoginPage(driver)
    login.authorization()

    mp = MainPage(driver)
    mp.select_about_link()

    time.sleep(3)
