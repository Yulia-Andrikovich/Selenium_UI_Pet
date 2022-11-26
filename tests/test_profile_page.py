import time

import pytest

from pages.profile_page import ProfilePage
from tests.test_login_page import test_go_to_login


@pytest.mark.smoke()
@pytest.mark.regression()
def test_add_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_button()
    page.go_to_name()
    page.go_to_type()
    page.go_to_list()
    page.go_to_age()
    page.go_to_gender()
    page.go_to_element()
    page.go_to_submit()
    time.sleep(3)


@pytest.mark.regression()
def test_add_pet_cancel(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_button()
    page.go_to_name()
    page.go_to_type()
    page.go_to_cancel()
    time.sleep(3)


@pytest.mark.regression()
def test_add_pet_requirement_fields(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_add_button()
    page.go_to_name()
    page.go_to_type()
    page.go_to_list()
    page.go_to_submit()
    time.sleep(3)


@pytest.mark.smoke()
@pytest.mark.regression()
def test_edit_pet_name(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_edit1()
    page.go_to_name1()
    page.go_to_submit()
    time.sleep(3)


@pytest.mark.smoke()
@pytest.mark.regression()
def test_delete_pet(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_delete_button()
    page.go_to_button_yes()
    time.sleep(3)


@pytest.mark.smoke()
def test_quit(browser):
    test_go_to_login(browser)
    link = 'http://34.141.58.52:8080/#/profile'
    page = ProfilePage(browser, link)
    page.open()
    page.go_to_quit_button()
    time.sleep(3)
