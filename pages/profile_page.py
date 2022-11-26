from .locators import ProfilePageLocators
from .base_page import BasePage


class ProfilePage(BasePage):
    def go_to_profile(self):
        profile_btn = self.browser.find_element(*ProfilePageLocators.BUTTON_PROFILE)
        profile_btn.submit()

    def go_to_add_button(self):
        add_pet = self.browser.find_element(*ProfilePageLocators.BUTTON_ADD)
        add_pet.click()

    def go_to_name(self):
        name_field = self.browser.find_element(*ProfilePageLocators.NAME_FIELD)
        name_field.send_keys('Bella')

    def go_to_type(self):
        dropdown_icon = self.browser.find_element(*ProfilePageLocators.TYPE_DROPDOWN)
        dropdown_icon.click()

    def go_to_list(self):
        cat_element = self.browser.find_element(*ProfilePageLocators.CAT_ELEMENT)
        cat_element.click()

    def go_to_age(self):
        age_field = self.browser.find_element(*ProfilePageLocators.AGE_FIELD)
        age_field.send_keys('5')

    def go_to_gender(self):
        dropdown_icon = self.browser.find_element(*ProfilePageLocators.GENDER_DROPDOWN)
        dropdown_icon.click()

    def go_to_element(self):
        female = self.browser.find_element(*ProfilePageLocators.FEMALE_GENDER)
        female.click()

    def go_to_submit(self):
        submit_button = self.browser.find_element(*ProfilePageLocators.BUTTON_SUBMIT)
        submit_button.click()

    def go_to_cancel(self):
        submit_button = self.browser.find_element(*ProfilePageLocators.BUTTON_CANCEL)
        submit_button.click()

    def go_to_edit1(self):
        button_edit1 = self.browser.find_element(*ProfilePageLocators.BUTTON_EDIT1)
        button_edit1.click()

    def go_to_name1(self):
        name1_field = self.browser.find_element(*ProfilePageLocators.NAME1_FIELD)
        name1_field.clear()
        name1_field.send_keys('Sam')

    def go_to_delete_button(self):
        button_delete4 = self.browser.find_element(*ProfilePageLocators.BUTTON_DELETE4)
        button_delete4.click()

    def go_to_button_yes(self):
        button_yes = self.browser.find_element(*ProfilePageLocators.BUTTON_YES)
        button_yes.click()

    def go_to_quit_button(self):
        button_yes = self.browser.find_element(*ProfilePageLocators.BUTTON_QUIT)
        button_yes.click()
