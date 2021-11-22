# pytest -s test_product_page.py
import time

import pytest

from pages.product_page import ProductPage

# def test_guest_can_add_product_to_basket(browser):
#     #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" #link for lesson4.3 step 3
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.check_message_that_product_was_added_to_basket()
#     page.product_name_in_alert_equal_product_name()
#     page.total_basket_cost_in_alert_equal_product_cost()

@pytest.mark.parametrize('offerNum', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offerNum):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offerNum}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_message_that_product_was_added_to_basket()
    page.product_name_in_alert_equal_product_name()
    page.total_basket_cost_in_alert_equal_product_cost()
    #time.sleep(60)

