import math

from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    """Базовые методы страниц."""

    def __init__(self, browser, url: str, timeout: int = 3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открыть страницу."""
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str):
        """Поиск элемента на странице (что искать, как искать)."""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def should_be_login_link(self):
        """Должен быть переход на страницу логина."""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            ">>> Login link is not presented."

    def go_to_login_page(self):
        """Переход на страницу логина."""
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()
        assert 'login' in self.browser.current_url, \
            ">>> This is not login page."

    def go_to_the_basket(self):
        """Переход в корзину."""
        self.browser.find_element(*BasePageLocators.VIEW_BASKET).click()
        assert 'basket' in self.browser.current_url, \
            ">>> This is not basket page."

    def solve_quiz_and_get_code(self):
        """Прохождение капчи (Алерта)."""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how: str, what: str, timeout: int =3):
        """
        Элемент не появляется в течение заданного времени.
        Тест упадет, как только увидит искомый элемент.

        Не появился: тест зеленый.
        """
        try:
            WebDriverWait(self.browser, timeout). \
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how: str, what: str, timeout: int =3):
        """
        Элемент исчезает в течение заданного времени.
        Тест упадет как только выйдет время, а элемент все еще виден.

        Исчез: тест зеленый.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def should_be_authorized_user(self):
        """Проверка авторизован ли пользователь."""
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
            ">>> User icon is not presented, probably unauthorised user."
