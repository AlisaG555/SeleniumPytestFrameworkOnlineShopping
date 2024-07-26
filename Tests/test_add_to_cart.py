from Pages.loginPage import LoginPage
from Pages.productsPage import ProductsPage
from Pages.shopping_cartPage import Shopping_cartPage
from Pages.productsPagelocators import ProductsPageLocators

class TestAddToCart:

    def test_adding_to_items_list(self, driver, login_password):
        login_page = LoginPage(driver)
        login_page.login(login_password)
        products_page = ProductsPage(driver)
        products_page.click_on_backpack_add_button()
        products_page.click_on_shopping_cart_icon()
        shopping_cart_page = Shopping_cartPage(driver)
        item_label = shopping_cart_page.get_backpack_label()
        assert item_label == "Sauce Labs Backpack", "Test failed, there's no such an item"

    def test_number_in_cart(self,driver,login_password):
        login_page = LoginPage(driver)
        login_page.login(login_password)
        products_page = ProductsPage(driver)
        products_page.add_several_items(4)
        number_of_items = products_page.get_number_of_items_label()
        assert number_of_items == "4", "Test failed, there are " + number_of_items + " items in this cart"

    def test_replacing_add_with_remove_button(self,driver,login_password):
        login_page = LoginPage(driver)
        login_page.login(login_password)
        products_page = ProductsPage(driver)
        products_page.click_on_backpack_add_button()
        item_text = products_page.get_backpack_button_text()
        assert item_text == "Remove", "Test failed there is no remove button available"







