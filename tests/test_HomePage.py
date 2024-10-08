import time

import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_submissionForm(self, get_data):
        log = self.loggerTool()

        homePage = HomePage(self.driver)

        nameField = homePage.get_name_field()
        nameField.send_keys(get_data["firstname"])
        log.info("NAME: " + get_data["firstname"])
        # nameField.send_keys(get_data[0])

        emailField = homePage.get_email_field()
        emailField.send_keys(get_data["email"])

        passwordField = homePage.get_password_field()
        passwordField.send_keys(get_data["password"])

        iceCreamCheckbox = homePage.get_ice_cream_checkbox()
        iceCreamCheckbox.click()

        self.select_option_by_visible_text(HomePage.genderDropdown, get_data["gender"])
        # self.select_option_by_visible_text(homePage.get_gender_dropdown(), get_data[3])

        submitButton = homePage.get_submit_button()
        submitButton.click()

        alertSuccessText = homePage.get_alert_success().text
        log.info("Text received from application: " + alertSuccessText) #LOGGING

        expectedText = "Success! The Form has been submitted successfully!."

        assert expectedText in alertSuccessText

        self.get_screenshot("screenshot_HomePage.png")

        self.driver.refresh()

    # DICTIONARY DATA TYPE (key - value pair)
    @pytest.fixture(params= HomePageData.test_HomePage_data)
    # TOUPLE
    # @pytest.fixture(params=[("Joana", "Joana@email.com", "Pass123", "Female"),
    #                         ("Alex", "Alex@email.com", "123pass", "Male")])
    def get_data(self, request):
        return request.param
        

