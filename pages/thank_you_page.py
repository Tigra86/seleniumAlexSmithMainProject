from base.base_class import Base


class ThankYouPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def thank_yoy_page(self):
        self.get_current_url()
        self.assert_url("https://www.saucedemo.com/checkout-complete.html")
        # self.take_screenshot()
