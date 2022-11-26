from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_dropdown_filter_by_type(self):
        dropdown_icon = self.browser.find_element(*MainPageLocators.DROPDOWN_FILTER_BY_TYPE)
        dropdown_icon.click()

    def go_to_dog_element(self):
        dog_element = self.browser.find_element(*MainPageLocators.DOG_ELEMENT)
        dog_element.click()

    def go_to_filter_by_pet_name(self):
        pet_name = self.browser.find_element(*MainPageLocators.FILTER_BY_PET_NAME)
        pet_name.send_keys('Denny')

    def go_to_page2(self):
        page2 = self.browser.find_element(*MainPageLocators.PAGE2)
        page2.click()

    def go_to_like(self):
        like = self.browser.find_element(*MainPageLocators.LIKE)
        like.click()

    def open_details_pet(self):
        details_pet = self.browser.find_element(*MainPageLocators.DETAILS_BUTTON)
        details_pet.click()

    def go_to_comment_field(self):
        comment = self.browser.find_element(*MainPageLocators.COMMENT_FIELD)
        comment.send_keys("You're so cute))))")

    def go_to_save_comment_button(self):
        save_comment = self.browser.find_element(*MainPageLocators.SAVE_COMMENT_BUTTON)
        save_comment.click()





