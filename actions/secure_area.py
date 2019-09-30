import allure
from pages.secure_area_page import SecureAreaPage
import logging

LOGGER = logging.getLogger(__name__)


class SecureAreaActions:

    # Get an instance driver, app, SecureAreaPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.secure_area_actions = SecureAreaPage(driver=self.driver)

    # Verify sub-header text for Secure area page
    @allure.step("Verify sub-header text for Secure area page")
    def get_secure_area_text(self):
        LOGGER.info("Text on the page is: ")
        return self.secure_area_actions.title_area.text

    # Click 'Login' button to Secure area page
    @allure.step("Logout")
    def click_logout_button(self):
        LOGGER.info("Logout")
        self.secure_area_actions.logout_button.click()
