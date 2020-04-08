from selenium.webdriver.common.by import By


class BasePageLocators:
    """Локаторы главной страницы."""
    LINK_MAIN_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/"

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    """Локаторы страницы авторизации/регистрации."""
    LINK_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/accounts/login/"

    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')


class ProductPageLocators:
    """Локаторы страницы товара."""
    LINK_PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-work_195/"

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button[@type="submit"]')
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) div.alertinner strong")
    PRICE = (By.XPATH, '//p[@class="price_color"]')
    PRICE_BASKET = (By.XPATH, '//div[@class="alertinner "]/p/strong')


class BasketPageLocators:
    """Локаторы страницы корзины."""
    LINK_BASKET_PAGE = "http://selenium1py.pythonanywhere.com/basket/"

    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, '//a[@class="btn btn-lg btn-primary btn-block"]')
    MESSAGE_BASKET_IS_EMPTY = (By.XPATH, '//div[@id="content_inner"]/p')
