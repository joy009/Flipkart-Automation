from unittest import TestCase

from myflipkart.app import MyFlipkart
from myflipkart.commom_methods import save_screenshot
from myflipkart.logging.logger import LOGGER


def get_meetnotes_driver():
    return MyFlipkart(driver_type="chrome")



class BaseTestCase(TestCase):

    def assertPage(self, page, cls):
        self.assertTrue(isinstance(page, cls), "Expected %s" % cls, )

    def assertContainsString(self, string1, string2):
        if string1.find(string2) == -1:
            return False
        return True

    def tally(self):
        return len(self._resultForDoCleanups.errors) + len(self._resultForDoCleanups.failures)

    def setUp(self):
        self.errors_and_failures = self.tally()
        self.flip = get_meetnotes_driver()
        self.flip.__enter__()
        LOGGER.info("Test %s started" % self._testMethodName)

    def tearDown(self):
        if self.tally() > self.errors_and_failures:
            save_screenshot("%s_failure.png" % self._testMethodName, self.flip.driver)
            LOGGER.info("Test %s failed" % self._testMethodName)
        else:
            LOGGER.info("Test %s completed successfully" % self._testMethodName)
        self.flip.__exit__()
