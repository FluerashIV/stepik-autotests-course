from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):

    def add_product_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        login_link.click()

    def check_message_that_product_was_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), "message is not present"

    def product_name_in_alert_equal_product_name(self):
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name_in_alert == product_name, "product name is uncorrect"

    def total_basket_cost_in_alert_equal_product_cost(self):
        product_price_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price_in_alert == product_price, "product price is uncorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), \
            "Success message is presented, but should not be" #тут чуток неправильный локатор

    def should_disappeare_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), \
            "Success message is presented, but should not be" #тут чуток неправильный локатор


