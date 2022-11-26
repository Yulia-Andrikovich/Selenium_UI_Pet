from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    LOGO = (By.CLASS_NAME, 'p-menubar-start')
    DROPDOWN_FILTER_BY_TYPE = (By.XPATH, "//div[@id='pv_id_2']/div/span")
    DOG_ELEMENT = (By.XPATH, '//*[@id="pv_id_4_0"]')
    CAT_ELEMENT = (By.XPATH, '//*[@id="pv_id_4_1"]')
    REPTILE_ELEMENT = (By.XPATH, '//*[@id="pv_id_4_2"]')
    HAMSTER_ELEMENT = (By.XPATH, '//*[@id="pv_id_4_3"]')
    PARROT_ELEMENT = (By.XPATH, '//*[@id="pv_id_4_4"]')
    FILTER_BY_PET_NAME = (By.XPATH, '//*[@id="petName"]')
    PAGE2 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[3]/span[1]/button[2]')
    LIKE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]/span[1]/i[1]')
    DETAILS_BUTTON = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[8]/div[1]/div[3]/div[1]/button[1]')
    COMMENT_FIELD = (By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[1]')
    SAVE_COMMENT_BUTTON = (By.XPATH, '//*[@id="app"]/main[1]/div[2]/div[1]/div[1]/div[3]/form[1]/div[1]/button[1]')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class ProfilePageLocators:
    LOGO = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/div[1]/img[1]')
    BUTTON_QUIT = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[2]/a[1]')
    BUTTON_PROFILE = (By.XPATH, '//*[@id="app"]/header[1]/div[1]/ul[1]/li[1]/a[1]')
    BUTTON_ADD = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]')
    NAME_FIELD = (By.ID, 'name')

    TYPE_DROPDOWN = (By.CSS_SELECTOR, '#pv_id_2 .p-dropdown-trigger-icon')
    CAT_ELEMENT = (By.ID, 'pv_id_2_1')
    AGE_FIELD = (By.XPATH, "//span[@id='age']/input")
    GENDER_DROPDOWN = (By.CSS_SELECTOR, '#pv_id_3 .p-dropdown-trigger-icon')
    FEMALE_GENDER = (By.ID, 'pv_id_3_1')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '.p-button-success > .p-button-label')
    BUTTON_CANCEL = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/button[2]')
    BUTTON_DELETE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]')
    BUTTON_EDIT1 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]')
    NAME1_FIELD = (By.XPATH, '//*[@id="name"]')
    BUTTON_EDIT2 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[1]')
    BUTTON_EDIT3 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/button[1]')
    BUTTON_EDIT4 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/button[1]')
    CHOOSE_BUTTON = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/button[1]')
    BUTTON_DELETE1 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[2]')
    BUTTON_DELETE2 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/button[2]')
    BUTTON_DELETE3 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/button[2]')
    BUTTON_DELETE4 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/button[2]')
    BUTTON_YES = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')
    IMAGE1 = (By.CSS_SELECTOR, 'div#app > main > div > div > div:nth-of-type(2) > div > div > div > img')
    IMAGE2 = (By.CSS_SELECTOR, 'div#app > main > div > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div > img')
    IMAGE3 = (By.CSS_SELECTOR, 'div#app > main > div > div > div:nth-of-type(2) > div > div:nth-of-type(3) > div > img')
    PET_NAME1 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]')
    PET_NAME2 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]')
    PET_NAME3 = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]')
