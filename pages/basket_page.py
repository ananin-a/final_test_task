from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Методы страницы корзины."""

    def should_be_a_message_about_an_empty_basket(self):
        """Должно быть сообщение об успешном добавлении товара в корзину."""
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY), \
            ">>> No empty basket message."

    def should_not_be_proceed_to_checkout_button(self):
        """Не должно быть кнопки продолжения оформления товара."""
        assert self.is_not_element_present(*BasketPageLocators.PROCEED_TO_CHECKOUT_BUTTON), \
            ">>> There should not be a checkout button in an empty basket."
