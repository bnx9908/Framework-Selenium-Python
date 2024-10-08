from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    autoSuggestiveField = (By.CSS_SELECTOR, "#country")
    suggestionsList = (By.XPATH, "//div[@class='suggestions']/ul")
    suggestionTextPath = (By.XPATH, "li/a")

    def get_autosuggestion_field(self):
        return self.driver.find_element(*ConfirmPage.autoSuggestiveField)

    def get_suggestions_list(self):
        return self.wait_all_elements_to_be_present(self.suggestionsList)

    def get_suggestion_option(self, suggestionArgument):
        return suggestionArgument.find_element(*ConfirmPage.suggestionTextPath)