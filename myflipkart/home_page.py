from myflipkart.commom_methods import *
from myflipkart.pages import Page


class HomePage(Page):

    @staticmethod
    def is_current_page(driver):
        return "https://www.flipkart.com/" in driver.current_url

    def login(self, email, password):
        '''
        This function is used to click on the login in the website and login to the web application by sending the username and the passowrd to the respective input fields.
        :param email: email id
        :param password: password
        :return: Returns current page
        '''
        time.sleep(2)
        click_login(self)
        LOGGER.info("Executing login method")
        self.driver.find_element_by_xpath(LOGIN_USERNAME_INPUT_BOX_XPATH).send_keys(email)
        self.driver.find_element_by_xpath(LOGIN_PASSWORD_INPUT_BOX_XPATH).send_keys(password)
        click_radio_button_by_xpath(self, LOGIN_BUTTON_MODAL_XPATH)
        LOGGER.info("Finished login method")
        time.sleep(1)
        return (get_current_page(self.driver))(self.driver)

    def has_error(self):
        '''
        Checks whether any error is generated or not
        :return:
        '''
        return self.get_error_message()

    def get_error_message(self):
        '''
        Fetches the error message
        :return:
        '''
        return self.driver.find_element_by_xpath(LOGIN_ERROR_MESSAGE_XPATH).text

    def get_greet_user_text(self, greet_user_text):
        '''
        Checks that after user is logged in, whether a greeting text is displayed or not.
        :param greet_user_text: This is the text which user expects to be displayed after login.
        :return: No if the text is not present and return yes if the text is present.
        '''
        length = len(self.driver.find_elements_by_xpath("//a[contains(@class, '_1AHrFc _2k0gmP')][contains(text(), '" + str(greet_user_text) + "')]"))
        if length == 0:
            return "No"
        else:
            return "Yes"

    def enter_text_on_search_bar(self, search_text):
        '''
        This function locates the search bar in the application and enters the given text in the search bar
        :param search_text: This is the text which user wants to enter in the search bar and search)
        :return:self
        '''
        self.driver.find_element_by_xpath(SEARCH_BAR_XPATH).send_keys(search_text)
        return self

    def click_search_button(self):
        '''
        This function clicks the search button which is present beside the search bar on the web page
        :return: the driver of the page which opens
        '''
        time.sleep(1)
        self.driver.find_element_by_xpath(SEARCH_BUTTON_XPATH).click()
        time.sleep(2)
        return (get_current_page(self.driver))(self.driver)

    def click_on_first_item(self):
        '''
        This function clicks on the name of the first item displayed on the web page
        :return: self
        '''
        self.driver.find_element_by_xpath(FIRST_ITEM_XPATH).click()
        time.sleep(5)
        return (get_current_page(self.driver))(self.driver)

    def get_product_name_from_detail_page(self):
        text = find_attribute_inner_text_of_field_by_xpath(self, PRODUCT_NAME_ON_DETAIL_PAGE_XPATH)
        LOGGER.info(text)
        return text

    def click_add_to_cart(self):
        '''
        This function clicks on the "Add to Cart" button on a product view page.
        :return: The driver of the new page
        '''
        self.driver.execute_script("window.scrollTo(0, 100)")
        self.driver.find_element_by_xpath(ADD_TO_CART_XPATH).click()
        LOGGER.info("Clicked on Add to Cart")
        time.sleep(2)
        return (get_current_page(self.driver))(self.driver)

    def bring_focus_on_last_tab(self):
        '''
        This function brings the focus of the webdriver to the last tab in a window
        :return:
        '''
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self

    def get_recently_added_item_name_on_cart_page(self):
        '''
        This function fetches the name of the recently added items from the cart page
        :return: The text of the recently added item
        '''
        text = find_attribute_inner_text_of_field_by_xpath(self, RECENTLY_ADDED_ITEM_XPATH)
        return text
