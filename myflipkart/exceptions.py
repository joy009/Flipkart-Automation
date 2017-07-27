from myflipkart.logging.logger import LOGGER


class NoElementFoundException(Exception):
    """
    This should thrown when no element found for given predicate on particular page.
    """
    def __init__(self, message):
        LOGGER.exception(message)


class ValidationException(Exception):
    """
    This should thrown when some validation error occurred on page
    """
    def __init__(self, message):
        LOGGER.exception(message)



class MissingDataException(Exception):
    """
    This should thrown when value is not present for key in test input file
    """
    def __init__(self, message):
        LOGGER.exception(message)
