from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_a_message_about_an_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), \
            'There is no message that the goat is empty'

    def should_not_be_proceed_to_checkout_button(self):
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT_BUTTON), \
            'There was a button that will issue the goods, maybe the basket is not empty'
