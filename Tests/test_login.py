from Pages.loginPage import LoginPage
from Pages.productsPage import ProductsPage
from Resources.constants import URL

from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.productsPagelocators import ProductsPageLocators

class TestLogin:

    def test_login(self, driver, login_password):
        login_Page = LoginPage(driver)
        login_Page.navigate_to(URL)
        login_Page.wait_and_type_credentials(login_password)
        login_Page.click_on_login_button()
        products_page = ProductsPage(driver)
        products_page.find_element(ProductsPageLocators.CLICK_ON_BACKPACK_ADD_BUTTON).click()


        products_Page = ProductsPage(driver)
        login_success_lbl = products_Page.get_login_success_label()
        assert login_success_lbl == "Products","Loggining process failed"

    def test_new(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        #lbl1 = driver.find_element(By.XPATH,"//*[@id='header_container']/div[2]/span").text
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        #lbl2 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text
        lbl3 = driver.find_element(By.ID,"remove-sauce-labs-backpack").text
        print("*************",lbl3)

