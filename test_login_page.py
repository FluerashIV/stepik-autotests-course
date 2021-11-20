# pytest -v --tb=line --language=en --browser_name=chrome test_login_page.py

from pages.login_page import LoginPage

def test_guest_can_bla_bla(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

