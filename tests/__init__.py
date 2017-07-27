import unittest

from tests.test_add_item_and_verify import TestCases


def all_tests():
    suite = unittest.TestSuite()

    suite.addTest(TestCases("test_search_and_add_item_and_verify_in_cart"))

    return suite