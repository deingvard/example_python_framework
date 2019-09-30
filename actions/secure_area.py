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
        return self.secure_area_actions.title_area.text

    # Check that text loaded on the Secure area page
    def check_secure_area_text(self, area):
        LOGGER.info("Text on the page is: '%s'", area)
        return self.get_secure_area_title() == area
