import time

import pytest

from pages.main_page import MainPage
from tests.test_login_page import test_go_to_login


@pytest.mark.smoke()
def test_go_to_main_page(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(5)


@pytest.mark.smoke()
def test_go_to_logo_dropdown_filter(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_dropdown_filter_by_type()
    time.sleep(3)


@pytest.mark.smoke()
def test_go_to_filter_by_pet_name(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_pet_name()
    time.sleep(3)


@pytest.mark.smoke()
@pytest.mark.regression()
def test_put_like(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_page2()
    page.go_to_like()
    time.sleep(3)


@pytest.mark.smoke()
def test_open_details_pet(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_page2()
    page.open_details_pet()
    time.sleep(3)


@pytest.mark.smoke()
@pytest.mark.regression()
def test_create_comment(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_page2()
    page.open_details_pet()
    page.go_to_comment_field()
    page.go_to_save_comment_button()
    time.sleep(5)
