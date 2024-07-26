from Pages.basePage import BasePage
from Pages.loginPagelocators import loginPagelocators
from Resources.constants import MAX_WAIT_INTERVAL

from Resources.constants import URL
class LoginPage(BasePage):

    def wait_and_type_credentials(self,credentials):
        username = credentials[0]
        password = credentials[1]
        self.wait_and_find_element(loginPagelocators.USER_NAME,MAX_WAIT_INTERVAL).send_keys(username)
        self.wait_and_find_element(loginPagelocators.PASSWORD, MAX_WAIT_INTERVAL).send_keys(password)
    def click_on_login_button(self):
        self.find_element(loginPagelocators.LOGIN_BUTTON).click()

    def login(self, credentials):
        self.navigate_to(URL)
        self.wait_and_type_credentials(credentials)
        self.click_on_login_button()