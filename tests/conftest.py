import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("")
    print("Start test")

    driver = webdriver.Chrome()
    url = 'https://www.saucedemo.com'
    driver.get(url)
    driver.maximize_window()

    yield driver

    print("")
    print("Finish test")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")
