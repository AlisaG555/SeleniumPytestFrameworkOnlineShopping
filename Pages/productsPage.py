from Pages.basePage import BasePage
from Pages.productsPagelocators import ProductsPageLocators
from Resources.constants import MAX_WAIT_INTERVAL

class ProductsPage(BasePage):
    def get_login_success_label(self):
        lbl_login_success = self.find_element(ProductsPageLocators.PRODUCTS_PAGE_LABEL).text
        return lbl_login_success

    def click_on_backpack_add_button(self):
        self.find_element(ProductsPageLocators.CLICK_ON_BACKPACK_ADD_BUTTON).click()

    def click_on_bikelight_add_button(self):
        self.find_element(ProductsPageLocators.CLICK_ON_BIKELIGHT_ADD_BUTTON).click()

    def click_on_shopping_cart_icon(self):
        self.find_element(ProductsPageLocators.CLICK_ON_SHOPPING_CART_ICON).click()

    def get_number_of_items_label(self):
        lbl_number_of_items = self.find_element(ProductsPageLocators.NUMBER_OF_ITEMS_LABEL).text
        return lbl_number_of_items

    def get_backpack_button_text(self):
        backpack_button_text = self.find_element(ProductsPageLocators.REMOVE_BACK_PACK_BUTTON).text
        return backpack_button_text

    def add_several_items(self, number_of_items):
        for i in range(0,number_of_items):
            locator = ProductsPageLocators.LIST_OF_CLICK_ON_ADD_TO_CART_BUTTONS[i]
            self.find_element(locator).click()