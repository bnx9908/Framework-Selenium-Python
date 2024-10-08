import inspect
import logging
import os

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def loggerTool(self):
        loggerName = inspect.stack()[1][3] #printing the correct function name when using logger in a different class
        logger = logging.getLogger(loggerName) #object responsible for printing

        fileHandler = logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../utilitiesReport/logfile.log")) #object responsible for log file location
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") #log formatter

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG) #set the level => only the argument and the following will be printed (rest skipped)
        return logger

    def get_screenshot(self, screenshot_name):
        return self.driver.get_screenshot_as_file(screenshot_name)

    def wait_element_to_be_present(self, locator, wait_time=10):
        explicitWait = WebDriverWait(self.driver, wait_time)
        return explicitWait.until(expected_conditions.presence_of_element_located(locator))

    def wait_all_elements_to_be_present(self, locator, wait_time=10):
        explicitWait = WebDriverWait(self.driver, wait_time)
        return explicitWait.until(expected_conditions.presence_of_all_elements_located(locator))

    def select_option_by_visible_text(self, locator, option_text):
        gender_dropdown = self.wait_element_to_be_present(locator)
        selector = Select(gender_dropdown)
        # selector = Select(locator)
        selector.select_by_visible_text(option_text)
        return selector
