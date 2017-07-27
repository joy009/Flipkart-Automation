import os
import platform
import sys
from selenium import webdriver

from myflipkart.common.constants import *

from myflipkart.commom_methods import *
from logging.logger import LOGGER
from myflipkart.home_page import HomePage
from myflipkart.common.constants import *

PHANTOMJS_POSSIBLE_PATHS = (
    "%s/phantomjs" % BIN_DIR, "/usr/local/bin/phantomjs", "/usr/bin/phantomjs", "%s/phantomjs.exe" % BIN_DIR)


class MyFlipkart(object):
    """
    This is the main class where the current_page, driver_type etc are defined. Also the
    """

    def __init__(self, driver_type=None, base_url=None):
        if not base_url:
            self.base_url = BASE_URL
        else:
            self.base_url = base_url
        self.driver_type = driver_type

    def __enter__(self):
        """ Start PhantomJS/Chrome/Firefox inside a context manager"""
        if self.driver_type == "chrome":
            self.driver = webdriver.Chrome()
        elif self.driver_type == "firefox":
            self.driver = webdriver.Firefox()
        LOGGER.info("Launching session on browser " + self.driver.name + " with version " + self.driver.capabilities[
            'version'] + " on system " + platform.system())
        # self.driver.set_window_size(1120, 550)
        self.driver.maximize_window()

    def __exit__(self):
        """quit driver inside context manager"""
        if self.driver:
            self.driver.quit()
        LOGGER.info("*" * 10 + " Quitting driver " + "*" * 10)
        LOGGER.info("=" * 50)

    @property
    def current_page(self):
        '''
        1. Iterate over all the pages defined in the application
        2. Call the is_current_page function defined on the page
        3. Return the first page that matches
        '''

        return get_current_page(self.driver)

    def is_logged_in(self):
        '''
        Check current page is login page or not
        '''
        login_len = len(self.driver.find_elements_by_xpath(LOGIN_BUTTON_XPATH))
        LOGGER.info("Got the lenth of login")
        singup_len = len(self.driver.find_elements_by_xpath(SIGN_UP_BUTTON_XPATH))
        LOGGER.info("Got the lenth of signup")
        if login_len > 0 and singup_len > 0:
            return False
        return True

    def login_if_necessary(self, email, password):
        '''
        Check already logged in or not
        :param email: email id
        :param password: password
        :return: Returns current page
        '''
        self.driver.get(BASE_URL)
        LOGGER.info("Login if necessary")

        if self.is_logged_in():
            LOGGER.info("Already Logged In")
            return self.current_page
        else:
            LOGGER.info("Needs to Log In.")
            login_modal = len(self.driver.find_elements_by_xpath(LOGIN_MODAL_CLOSE_BUTTON_XPATH))
            if login_modal > 0:
                LOGGER.info("Login Modal Already Exists")
                self.driver.find_element_by_xpath(LOGIN_MODAL_CLOSE_BUTTON_XPATH).click()
                time.sleep(2)
            else:
                LOGGER.info("Login Modal does not exists")
            page = HomePage(self.driver)
            return page.login(email, password)

