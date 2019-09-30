import allure

from pages.secure_area_page import SecureAreaPageLocators
import pytest
import logging

LOGGER = logging.getLogger(__name__)


class SecureAreaActions(SecureAreaPageLocators):

    # Get an instance driver, app, SecureAreaPageLocators
    def __init__(self, app):
        self.app = app
        self.driver = app.driver
        self.secure_area_actions = SecureAreaPageLocators(driver=self.driver)

    # Get text on the Secure area page
    def get_secure_area_title(self):
        LOGGER.info("Get text on the Secure area page")
        return self.secure_area_actions.title_area.text

    # Verify sub-header text for Secure area page
    @allure.step("Verify sub-header text for Secure area page")
    def check_secure_area_text(self, area):
        LOGGER.info("Text on the page is: '%s'", area)
        return self.get_secure_area_title() == area

    # Click 'Login' button to Secure area page
    @allure.step("Click 'Logout' button")
    def click_logout_button(self):
        LOGGER.info("Click 'Logout' button")
        self.secure_area_actions.logout_button.click()
