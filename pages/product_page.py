from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_url(self):
        assert '?promo=newYear' in self.browser.current_url, 'Invalid Page.'

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'Missing button "Add to basket"'

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_adding_confirmation(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is not present'

    def name_added_should_be_correct(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE).text
        assert item_name == added_item_name, 'The added item"s name is not corresponding with the item"s name'

    def price_comparison(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_from_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price == price_from_basket, 'The price of the product and the basket does not match'