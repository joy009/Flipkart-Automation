import os
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from exceptions import *

from myflipkart.common.constants import *
from logging.logger import LOGGER, make_directory
from datetime import datetime, timedelta

def goto_url(self, relative_url):
    self.driver.get("%s%s" % (BASE_URL, relative_url))
    LOGGER.info("Hitting url " + self.driver.current_url)
    pass

def click_login(self):
    '''
    Click on the Login button on the web page
    :param self:
    :return: self
    '''
    self.driver.find_element_by_xpath(LOGIN_BUTTON_XPATH).click()
    LOGGER.info("Clicked On Login Button")
    time.sleep(2)
    return self


def import_class(main_module, module_name, class_name):
    module = getattr(main_module, module_name)
    class_ = getattr(module, class_name)
    return class_


def get_current_page(driver):
    main_module = __import__(MAIN_MODULE)
    for module_name, page in zip(ALL_MODULES, ALL_PAGES):
        module = import_class(main_module, module_name, page)
        if module.is_current_page(driver):
            return module


def wait_until_page_load(self, wait_additional=0):
    if wait_additional:
        time.sleep(wait_additional)

    try:
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".pace-done")))
    except TimeoutException:
        LOGGER.warn("Timeout for wait until page load predicate with css_selector .pace-done")
        pass

def wait_until_for_element_invisibility(self, css_selector, wait_additional=0):
    if wait_additional:
        time.sleep(wait_additional)
    try:
        WebDriverWait(self.driver, 60).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    except TimeoutException:
        LOGGER.warn("Timeout for wait until element invisibility for css_selector " + css_selector)
        pass


def wait_til_for_element_visibility(self, css_selector, wait_additional=0):
    if wait_additional:
        time.sleep(wait_additional)
    try:
        WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    except TimeoutException:
        LOGGER.warn("Timeout for wait until element visibility for css_selector " + css_selector)
        pass


def wait_til_for_element_visibility_by_xpath(self, xpath, wait_additional=0):
    if wait_additional:
        time.sleep(wait_additional)
    try:
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        LOGGER.warn("Timeout for wait until element invisibility for xpath " + xpath)
        pass


def wait_til_for_element_invisibility_by_xpath(self, xpath, wait_additional=0):
    if wait_additional:
        time.sleep(wait_additional)
    try:
        WebDriverWait(self.driver, 60).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, xpath)))
    except:
        LOGGER.warn("Timeout for wait until element invisibility for xpath " + xpath)


def fill_answer_of_textbox_by_xpath(self, xpath, answer):
    if answer is None:
        return
    try:
        LOGGER.debug("Answering question having xpath " + xpath + "with answer " + answer)
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(answer)
        LOGGER.debug("Answered question having xpath " + xpath + "with answer " + answer)
    except:
        raise NoElementFoundException("Could not find element with xpath " + xpath + " for answer " + answer)


def find_attribute_inner_text_of_field_by_xpath(self, xpath):
    try:
        return self.driver.find_element_by_xpath(xpath).get_attribute('innerText')
    except:
        raise NoElementFoundException("Could not find element with xpath " + xpath )



def click_radio_button_by_xpath(self, xpath):
    try:
        LOGGER.debug("Clicking on element with xpath " + xpath)
        self.driver.find_element_by_xpath(xpath).click()
        LOGGER.debug("Clicked on element with xpath " + xpath)
    except:
        raise NoElementFoundException("Could not find element with xpath " + xpath + " for clicking")


def save_screenshot(file_name, driver):
    '''
    Method to take the screenshot of the browser
    :param file_name: name of the screenshot file
    :param driver: current page driver
    :return: screenshot file name
    '''
    path = "%s/%s" % (make_directory(SCREENSHOT_DIR), file_name)
    driver.save_screenshot(path)
    page_source_file_name = remove_file_extension(file_name)
    save_page_source(page_source_file_name + ".html", driver)
    return file_name


def save_page_source(file_name, driver):
    '''
    Method for creating the page source
    :param file_name: name of the page source file
    :param driver: current page driver
    :return: page source file name
    '''
    page_source = driver.page_source
    path = "%s/%s" % (make_directory(PAGE_SOURCE_DIR), file_name)
    page_source = page_source.encode('utf-8')
    try:
        with open(path, 'wb') as f:
            f.write(page_source)
    except IOError:
        return False
    except Exception as e:
        # Some other exception occurred, like UnicodeEncode error etc.
        LOGGER.exception("Error occurred while creating page source file -- " + e.message)
        return False
    return file_name


def remove_file_extension(file_name):
    return os.path.splitext(os.path.basename(file_name))[0]
