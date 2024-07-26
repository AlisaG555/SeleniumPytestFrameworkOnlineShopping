from Pages.basePage import BasePage
from Pages.shopping_cartPagelocators import Shopping_cartPageLocators
from Resources.constants import MAX_WAIT_INTERVAL

class Shopping_cartPage(BasePage):

    def get_backpack_label(self):
        get_backpack_label = self.wait_and_find_element(Shopping_cartPageLocators.BACKPACK_LINK,MAX_WAIT_INTERVAL).text
        return get_backpack_label
