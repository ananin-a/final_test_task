from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default"]')


class BasketPageLocators:
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//a[@class="btn btn-lg btn-primary btn-block"]')
    MESSAGE_BASKET_IS_EMPTY = (By.XPATH, '//div[@id="content_inner"]/p')


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


class ProductPageLocators:
    # ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[@value="Add to basket"]')
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button[@type="submit"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1)')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '.alert-success:nth-child(1) div.alertinner strong')
    PRICE = (By.XPATH, '//p[@class="price_color"]')
    PRICE_BASKET = (By.XPATH, '//div[@class="alertinner "]/p/strong')
