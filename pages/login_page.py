from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # проверка страници логина/регистрации
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка на той ли мы странице
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Invalid Page'

    # должна быть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_IN_EMAIL), \
            'Missing field Login_in_Email'
        assert self.is_element_present(*LoginPageLocators.LOGIN_IN_PASSWORD), \
            'Missing field Login_in_Password'
        assert self.is_element_present(*LoginPageLocators.LOGIN_IN_BUTTON), \
            'Missing Login_in_Button'

    # должна быть форма регистрации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), \
            'Missing field Register_in_Email'
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), \
            'Missing field Register_Password'
        assert self.is_element_present(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), \
            'Missing field Register_Confirm_Password'
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), \
            'Missing field Register_Button'

    # регистрация нового пользователя
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
