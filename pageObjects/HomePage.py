from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    shopButton = (By.CSS_SELECTOR, "a[href*='shop']")
    nameField = (By.CSS_SELECTOR, "input[name='name']")
    emailField = (By.NAME, "email")
    passwordField = (By.XPATH, "//input[@type='password']")
    iceCreamCheckbox = (By.ID, "exampleCheck1")
    genderDropdown = (By.ID, "exampleFormControlSelect1")
    submitButton = (By.XPATH, "//input[@type='submit']")
    alertSuccess = (By.XPATH, "//*[contains(@class,'alert-success')]")


    def get_shop_button(self):
        return self.driver.find_element(*HomePage.shopButton)

    def get_name_field(self):
        return self.driver.find_element(*HomePage.nameField)

    def get_email_field(self):
        return self.driver.find_element(*HomePage.emailField)

    def get_password_field(self):
        return  self.driver.find_element(*HomePage.passwordField)

    def get_ice_cream_checkbox(self):
        return self.driver.find_element(*HomePage.iceCreamCheckbox)

    def get_gender_dropdown(self):
        return self.driver.find_element(*HomePage.genderDropdown)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submitButton)

    def get_alert_success(self):
        return self.driver.find_element(*HomePage.alertSuccess)