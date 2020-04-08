import pytest
from faker import Faker

from .pages.basket_page import BasketPage
from .pages.locators import LoginPageLocators
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                      "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link: str):
    """
    Пользователь гость, может добавить товар в корзину
    проверка на страницах с действующей акцией.
    """
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_button_add_basket()
    product_page.should_not_be_success_message()
    product_page.add_product_to_basket()
    product_page.should_be_success_message()
    product_page.name_added_should_be_correct()
    product_page.price_comparison()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Пользователь гость, не может видеть сообщение об успешном добавлении товара в корзину."""
    product_page = ProductPage(browser, ProductPageLocators.LINK_PRODUCT_PAGE)
    product_page.open()
    product_page.add_product_to_basket_no_alert()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """Пользователь гость, не видит сообщение о добавлении товара в корзину, не добавив товарю."""
    product_page = ProductPage(browser, ProductPageLocators.LINK_PRODUCT_PAGE)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Сообщение о добавлении товара в корзину исчезает."""
    product_page = ProductPage(browser, ProductPageLocators.LINK_PRODUCT_PAGE)
    product_page.open()
    product_page.add_product_to_basket_no_alert()
    product_page.should_element_disappearance()


def test_guest_should_see_login_link_on_product_page(browser):
    """Пользоваьель гость, видит ссылку на страницу регистрации/авторизации со страницы товара."""
    product_page = ProductPage(browser, ProductPageLocators.LINK_PRODUCT_PAGE)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Пользователь гость, может перейти на страницу регистрации/авторизации со страницы товара."""
    product_page = ProductPage(browser, ProductPageLocators.LINK_PRODUCT_PAGE)
    product_page.open()
    product_page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Пользователь гость, не видит товар перейдя в корзину со страницы товара."""
    product_page = ProductPage(browser, ProductPageLocators.LINK_PRODUCT_PAGE)
    product_page.open()
    product_page.go_to_the_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_proceed_to_checkout_button()
    basket_page.should_be_a_message_about_an_empty_basket()


class TestUserAddToBasketFromProductPage:
    """Зарегистрированный пользователь, может добавить товары в корзину."""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Регистрация нового пользователя."""
        fake = Faker()
        email = fake.email()
        password = fake.password()
        login_page = LoginPage(browser, LoginPageLocators.LINK_LOGIN_PAGE)
        login_page.open()
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """Зарегистрированный пользователь, по умолчанию нет сообщения об успешном добавлении товара в корзину."""
        product_page = ProductPage(browser, ProductPageLocators.LINK_PRODUCT_PAGE)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Зарегистрированный пользователь, добавление товара в корзину.
        Сравнение названия товара на странице и в корзине.
        Сравнение центы товара, цене товара в корзине.
        """
        product_page = ProductPage(browser, ProductPageLocators.LINK_PRODUCT_PAGE)
        product_page.open()
        product_page.should_be_button_add_basket()
        product_page.should_not_be_success_message()
        product_page.add_product_to_basket_no_alert()
        product_page.should_be_success_message()
        product_page.name_added_should_be_correct()
        product_page.price_comparison()
