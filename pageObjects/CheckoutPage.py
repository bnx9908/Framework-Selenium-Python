from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productsInCheckout = (By.XPATH, "//*[@class='media']")
    productsNamesLinksInCheckout = (By.XPATH, "div/h4/a")
    checkoutButton = (By.CSS_SELECTOR, "[class*='btn-success']")

    def get_products_in_checkout(self):
        return self.driver.find_elements(*CheckoutPage.productsInCheckout)

    def get_product_name_link_in_checkout(self, product_name_link):
        return product_name_link.find_element(*CheckoutPage.productsNamesLinksInCheckout)

    def get_finish_checkout_button(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)