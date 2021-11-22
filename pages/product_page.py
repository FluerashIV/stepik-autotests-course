from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()

    def check_message_that_product_was_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), "message is not present"

    def product_name_in_alert_equal_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT) == self.is_element_present(*ProductPageLocators.PRODUCT_NAME)

    def total_basket_cost_in_alert_equal_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT) == self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
