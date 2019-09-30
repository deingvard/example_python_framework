from pages.login_page import LoginPage
import allure
import logging

LOGGER = logging.getLogger(__name__)


class LoginActions:

    # Get an instance driver, app, LoginPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.login_actions = LoginPage(driver=self.driver)

    # Enter username, string value
    @allure.step("Enter username")
    def enter_username(self, group):
        LOGGER.info("Enter username: '%s'", group.username)
        self.login_actions.user_name_input.send_keys(group.username)

    # Enter password, string value
    @allure.step("Enter password")
    def enter_password(self, group):
        LOGGER.info("Enter password: '%s'", group.password)
        self.login_actions.user_password_input.send_keys(group.password)

    # Click 'Login' button to Secure area page
    @allure.step("Click 'Login' button")
    def click_submit_button(self):
        LOGGER.info("Click 'Login' button")
        self.login_actions.submit_button.click()
