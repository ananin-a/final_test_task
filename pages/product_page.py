from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Методы страницы товара."""

    def should_be_button_add_basket(self):
        """Должна быть кнопка добавить в карзину."""
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            ">>> Missing button 'Add to basket."

    def should_not_be_success_message(self):
        """Не должно быть сообщения об успешном добавление товара в корзину."""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            ">>> Success message is presented, but should not be."

    def add_product_to_basket(self):
        """Добавить товар в корзину с прохождением капчи(Алерта)."""
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def add_product_to_basket_no_alert(self):
        """Добавить товар в корзину без проходения капчи(Алерта)."""
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_success_message(self):
        """Должно быть сообщение об успешном добавлении товара в корзину."""
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            ">>> Not messages about the successful addition of the item to the cart."

    def should_element_disappearance(self):
        """Сообщение об успешном добавлении товара в корзино не должно исчезать."""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            ">>> The message about the successful addition of the product to the cart disappeared."

    def name_added_should_be_correct(self):
        """Проверка то ли имя у товара который мы добавили в корзину."""
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE).text
        assert item_name == added_item_name, \
            ">>> The product’s name does not match the product added to the cart."

    def price_comparison(self):
        """Проверка на соответствие цены товара, цене в корзине."""
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_from_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price == price_from_basket, \
            ">>> The price of the product and the basket does not match."
