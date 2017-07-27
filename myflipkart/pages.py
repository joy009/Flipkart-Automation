from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
import time


def normalize_url(url):
    '''Returns a normalized url that is -
    1. Relative, not absolute
    2. Resolves to the same url in QA vs Production
    3. Is never null or empty
    3. Always has a leading slash
    4. Always has trailing slash'''
    return url


def _wait_for_element(self, element_selector, wait_additional=2):
    timeout = wait_additional
    try:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.visibility_of_element_located(element_selector))
    except TimeoutException:
        raise TimeoutException("Could not find element selector")

def _wait_until_page_load(self, wait_additional=0):
    if wait_additional:
        time.sleep(wait_additional)
    WebDriverWait(self.driver, 30).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "body.pace-done")))


class Page:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def is_current_page(driver):
        '''
        Returns True if this is the current page
        Only 1 page can be the current page
        Typically, implementations check the URL or title of the page
        Some implementations may check existence of DOM elements
        to determine if this is the right page
        '''
        return True

    @property
    def title(self):
        return self.driver.title

    @property
    def url(self):
        return normalize_url(self.driver.current_url)
