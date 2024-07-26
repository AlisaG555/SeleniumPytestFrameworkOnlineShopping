from selenium.webdriver.common.by import By

class ProductsPageLocators:
    PRODUCTS_PAGE_LABEL = (By.XPATH,"//*[@id='header_container']/div[2]/span")
    CLICK_ON_BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACK_PACK_BUTTON = (By.ID,"remove-sauce-labs-backpack")
    CLICK_ON_BIKELIGHT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CLICK_ON_SHOPPING_CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    NUMBER_OF_ITEMS_LABEL = (By.XPATH,"//a[@class='shopping_cart_link']/span")

    LIST_OF_CLICK_ON_ADD_TO_CART_BUTTONS = [
        (By.ID, "add-to-cart-sauce-labs-backpack"),
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        (By.ID,"add-to-cart-sauce-labs-onesie"),
        (By.ID,"add-to-cart-sauce-labs-bike-light"),
        (By.ID,"remove-sauce-labs-fleece-jacket"),
        (By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")]
