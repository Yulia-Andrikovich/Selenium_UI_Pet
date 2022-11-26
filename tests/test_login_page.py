import time

import pytest

from pages.login_page import LoginPage


@pytest.mark.smoke()
@pytest.mark.regression()
def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    time.sleep(5)
