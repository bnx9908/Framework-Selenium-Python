from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestEnd2End(BaseClass):

    def test_end2end(self):
        log = self.loggerTool()

        homePage = HomePage(self.driver)
        shopPage = ShopPage(self.driver)
        checkoutPage = CheckoutPage(self.driver)
        confirmPage = ConfirmPage(self.driver)

        homePage.get_shop_button().click()

        log.info("Getting all products names links...") #LOGGING

        products_links = shopPage.get_products_names_links()
        for product in products_links:
            product_name = product.text
            log.info(product_name) #LOGGING
            if product_name == "Blackberry":
                shopPage.get_add_to_cart_button(product).click()
                break

        shopPage.get_go_to_checkout_button().click()
        checkoutPage.get_finish_checkout_button().click()

        autoSuggestiveField = confirmPage.get_autosuggestion_field()
        autoSuggestiveField.send_keys("r")

        expectedCountry = "Romania"

        for suggestionFromList in confirmPage.get_suggestions_list():
            suggestionName = confirmPage.get_suggestion_option(suggestionFromList).text
            if suggestionName == expectedCountry:
                log.info(expectedCountry + " exists in the autosuggestions list -> " + "\n" + suggestionName) #LOGGING
                suggestionFromList.click()
                break

        self.get_screenshot("screenshot_End2End.png")

        assert autoSuggestiveField.get_attribute("value") == expectedCountry, f"{expectedCountry} could not be found in the list!"