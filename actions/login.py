from pages.login_page import LoginPageLocators
import allure
import logging

LOGGER = logging.getLogger(__name__)


class LoginActions(LoginPageLocators):

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.login_actions = LoginPageLocators(driver=self.driver)

    # Enter username, string value
    @allure.step("Enter username")
    def enter_username(self, username):
        LOGGER.info("Enter username: '%s'", username)
        self.login_actions.user_name_input.send_keys(username)

    # Enter password, string value
    @allure.step("Enter password")
    def enter_password(self, password):
        LOGGER.info("Enter password: '%s'", password)
        self.login_actions.user_password_input.send_keys(password)

    # Click 'Login' button to Secure area page
    @allure.step("Click 'Login' button")
    def click_submit_button(self):
        LOGGER.info("Click 'Login' button")
        self.login_actions.submit_button.click()

    # Type name and password
    @allure.step("Type name and password")
    def type_name_and_password(self, group):
        self.enter_username(group.username)
        self.enter_password(group.password)

