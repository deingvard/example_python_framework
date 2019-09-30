from selenium import webdriver
from actions.login import LoginActions
from actions.secure_area import SecureAreaActions
import os
from selenium.common.exceptions import WebDriverException
import webium.settings
import logging

LOGGER = logging.getLogger(__name__)


class Application:
    def __init__(self, browser, base_url, config):
        # Set browser
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=chrome_options,
                                           executable_path=os.getcwd() + os.sep + os.sep + "data/chromedriver")
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # Sets a sticky timeout to implicitly wait for an element to be found
        self.driver.implicitly_wait(30)
        webium.settings.wait_timeout = 15
        # Invokes the window manager-specific 'full screen' operation
        LOGGER.info("Expand browser to full screen")
        self.driver.maximize_window()
        # Delete all cookies in the scope of the session
        self.driver.delete_all_cookies()
        # Initialize pages
        LOGGER.info("Started execution test")
        self.login_page = LoginActions(self)
        self.secure_area_page = SecureAreaActions(self)
        self.base_url = base_url

    def open_home_page(self):
        LOGGER.info("Open url '%s'", self.base_url)
        driver = self.driver
        driver.get(self.base_url)

    # Stop the browser
    def destroy(self):
        LOGGER.info("Quits the driver and closes every associated window.")
        self.driver.quit()

    def is_valid(self):
        try:
            self.current_url()
            LOGGER.info("Browser is valid")
            return True
        except WebDriverException:
            return False

    def current_url(self):
        return self.driver.current_url
