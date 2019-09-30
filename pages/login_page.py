from selenium.webdriver.common.by import By
from webium import BasePage, Finds, Find


class LoginPageLocators(BasePage):
    user_name_input = Find(by=By.NAME, value="username")
    user_password_input = Find(by=By.NAME, value="password")
    submit_button = Find(by=By.CSS_SELECTOR, value='button[type="submit"]')
