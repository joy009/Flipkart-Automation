import logging
import shutil
import os

from myflipkart.common.constants import *


def make_directory(dir):
    '''
    Method for creating directory
    :param dir: directory name
    :return: current directory path
    '''
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


LOGGER = logging.getLogger("meetnotes_logger")
LOGGER.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s - %(message)s')

log_path = make_directory(LOG_DIR)
fileHandler = logging.FileHandler("{0}/debug.log".format(log_path), mode='w+')

fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)
LOGGER.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(formatter)
LOGGER.addHandler(consoleHandler)