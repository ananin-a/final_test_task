import pytest

from .pages.basket_page import BasketPage
from .pages.locators import BasePageLocators
from .pages.locators import LoginPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        """Гостю видна ссылка прехода на страницу регистрации/авторизации."""
        main_page = MainPage(browser, BasePageLocators.LINK_MAIN_PAGE)
        main_page.open()
        main_page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        """
        Пользователь гость может перейти на страницу регистрации/авторизации с главной страницы.
        Все поля регистрации/авторизации видны.
        """
        main_page = MainPage(browser, BasePageLocators.LINK_MAIN_PAGE)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_login_page(browser):
    """Пользователь гость видит поля регистрации/аворизации."""
    login_page = LoginPage(browser, LoginPageLocators.LINK_LOGIN_PAGE)
    login_page.open()
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Переход под пользователем гость в пустую карзину. Проверка на то что корзина пуста,
    сообщение о том что корзина пуста присутствует.
    """
    main_page = MainPage(browser, BasePageLocators.LINK_MAIN_PAGE)
    main_page.open()
    main_page.go_to_the_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_proceed_to_checkout_button()
    basket_page.should_be_a_message_about_an_empty_basket()
