from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    # User Login in '''Поля логина пользавателя'''
    LOGIN_IN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_IN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_IN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')

    # User Register '''Поля регистрации нового пользавателя'''
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
