from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Методы страницы регистрации и входа."""

    def should_be_login_page(self):
        """Проверка всех форм на странице Входа/Регистрации."""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка что мы на странице логина."""
        assert "login" in self.browser.current_url, \
            ">>> This is not a login page."

    def should_be_login_form(self):
        """Должна быть форма логина."""
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), \
            ">>> Not found 'LOGIN_EMAIL' field."
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            ">>> Not found 'LOGIN_PASSWORD' field."
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), \
            ">>> Not found 'LOGIN_BUTTON' field."

    def should_be_register_form(self):
        """Должна быть форма регистрации."""
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), \
            ">>> Not found 'REGISTER_EMAIL' field."
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), \
            ">>> Not found 'REGISTER_PASSWORD' field."
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), \
            ">>> Not found 'REGISTER_CONFIRM_PASSWORD' field."
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), \
            ">>> Not found 'REGISTER_BUTTON' field."

    def register_new_user(self, email: str, password: str):
        """Регистрация нового пользователя."""
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
