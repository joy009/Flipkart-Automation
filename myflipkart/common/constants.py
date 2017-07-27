import os

PROJECT_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
RESOURCES_DIR = os.path.join(os.path.split(PROJECT_DIR)[0], 'resources')
LOG_DIR = os.path.join(PROJECT_DIR, "reports", "logs")
BIN_DIR = os.path.join(PROJECT_DIR, "bin")
REPORT_DIR = "reports"
SCREENSHOT_DIR = REPORT_DIR + "/screenshots"
PAGE_SOURCE_DIR = REPORT_DIR + "/page_sources"
LOG_DIR = REPORT_DIR + "/logs"
FULL_REPORT_NAME = "report.html"
SUMMARY_REPORT_NAME = "summary.html"
XML_REPORT_NAME = "report.xml"
DASHBOARD_LINK_CSS_SELECTOR = "a.dashboard"

MAIN_MODULE = "myflipkart"

ALL_MODULES = ["home_page", "pages"]
ALL_PAGES = ["HomePage", "Page"]

BASE_URL = "https://www.flipkart.com/"

LOGIN_BUTTON_XPATH = "//a[contains(@class, '_2k0gmP')][contains(text(), 'Log In')]"
SIGN_UP_BUTTON_XPATH = "//a[contains(@class, '_2k0gmP')][contains(text(), 'Signup')]"
LOGIN_BUTTON_MODAL_XPATH = "//button[contains(@class, '_2AkmmA _1LctnI _7UHT_c')]/span[contains(text(), 'Login')]"
LOGIN_USERNAME_INPUT_BOX_XPATH = "//input[contains(@class, '_2zrpKA')][not(contains(@class, '_3v41xv'))]"
LOGIN_PASSWORD_INPUT_BOX_XPATH = "//input[contains(@class, '_2zrpKA _3v41xv')]"
MY_ACCOUNT_TEXT_XPATH = "//a[contains(@class, '_1AHrFc _2k0gmP')][contains(text(), 'My Account')]"
LOGIN_ERROR_MESSAGE_XPATH = "//span[contains(@class, 'ZAtlA-')]"
LOGIN_MODAL_CLOSE_BUTTON_XPATH = "//button[contains(@class, '_2AkmmA _29YdH8')]"
SEARCH_BAR_XPATH = "//input[contains(@placeholder, 'Search for Products, Brands and More')]"
SEARCH_BUTTON_XPATH = "//button[contains(@class, 'vh79eN')]"
FIRST_ITEM_XPATH = "(//div[contains(@class, '_3wU53n')])[1]"
ADD_TO_CART_XPATH = "//button[contains(@class,'_2AkmmA _2Npkh4 _2MWPVK')]"
PRODUCT_NAME_ON_DETAIL_PAGE_XPATH = "//h1[contains(@class, '_3eAQiD')]"
RECENTLY_ADDED_ITEM_XPATH = "(//a[contains(@class, '_325-ji _3ROAwx')])[last()]"