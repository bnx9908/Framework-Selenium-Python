from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    productsNamesLinks = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    addToCartButton = (By.XPATH, "ancestor::div[@class='card h-100']//div[@class='card-footer']//button")
    goToCheckoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def get_products_names_links(self):
        return self.driver.find_elements(*ShopPage.productsNamesLinks)

    def get_add_to_cart_button(self, product_name_link):
        return product_name_link.find_element(*ShopPage.addToCartButton)

    def get_go_to_checkout_button(self):
        return self.driver.find_element(*ShopPage.goToCheckoutButton)