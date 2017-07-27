import os

from myflipkart.common.constants import *
import json

# Read data from credentials.json file
from myflipkart.common.constants import RESOURCES_DIR

data = json.loads(open(os.path.join(RESOURCES_DIR, "credentials.json")).read())

VALID_USERNAME = os.environ.get("FLIPKART_LOGIN_EMAIL", data["valid_credentials"]["email"])
VALID_PASSWORD = os.environ.get("FLIPKART_LOGIN_PASSWORD", data["valid_credentials"]["password"])
INVALID_USERNAME = data["invalid_credentials"]["email"]
INVALID_PASSWORD = data["invalid_credentials"]["password"]
