from lib2to3.pgen2 import driver

from myflipkart.home_page import HomePage
from resources.input import *
from tests.base import BaseTestCase
from tests.read_credentials import *

VALID_CREDENTIALS = (VALID_USERNAME, VALID_PASSWORD)
INVALID_CREDENTIALS = (INVALID_USERNAME, INVALID_PASSWORD)


class TestCases(BaseTestCase):
    def test_search_and_add_item_and_verify_in_cart(self):
        current_page = self.flip.login_if_necessary(*VALID_CREDENTIALS)
        self.assertEquals(current_page.get_greet_user_text(GREET_USER_TEXT), YES)
        current_page = current_page.enter_text_on_search_bar(SEARCH_TEXT)\
            .click_search_button()\
            .click_on_first_item()\
            .bring_focus_on_last_tab()
        product_view_page_name = current_page.get_product_name_from_detail_page()
        current_page = current_page.click_add_to_cart()
        self.assertEquals(current_page.get_recently_added_item_name_on_cart_page(), product_view_page_name)