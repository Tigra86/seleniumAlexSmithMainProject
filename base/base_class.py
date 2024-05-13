import datetime
import os


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Method get current URL
    def get_current_url(self):
        get_url = self.driver.current_url
        print("")
        print(f"Current URL is {get_url}")

    # Method assert page title text
    @staticmethod
    def assert_page_title_text(actual_page_title_text, expected_page_title_text):
        assert actual_page_title_text == expected_page_title_text, (f"Wrong page title text is displaying: "
                                                                    f"{actual_page_title_text}")
        print(f"Correct page title text is displaying")

    # Method take screenshot
    def take_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f"screenshot-{now_date}.png"
        self.driver.save_screenshot(f"/{os.getcwd()}/../screen/{name_screenshot}")
        print("Screenshot is taken")

    # Method assert URL
    def assert_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Wrong page is displaying: {actual_url}"
        print(f"Correct page is displaying")
