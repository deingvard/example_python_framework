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

    import allure

    # Enter username, string value
    @allure.step('Click show all available laptops')
    def enter_username(self, group):
        LOGGER.info("Enter username: '%s'", group.username)
        self.login_actions.user_name_input.click()
        self.login_actions.user_name_input.clear()
        self.login_actions.user_name_input.send_keys(group.username)

    # Enter password, string value
    def enter_password(self, group):
        LOGGER.info("Enter password: '%s'", group.password)
        self.login_actions.user_password_input.click()
        self.login_actions.user_password_input.clear()
        self.login_actions.user_password_input.send_keys(group.password)

    # Click 'Submit' button to Secure area page
    def click_submit_button(self):
        LOGGER.info("Click Submit button")
        self.login_actions.submit_button.click()
