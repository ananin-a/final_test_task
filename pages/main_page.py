from .base_page import BasePage


class MainPage(BasePage):
    pass
#     def go_to_login_page(self):
#         login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
#         login_link.click()
#         # alert = self.browser.switch_to.alert  # обработка Алертов
#         # alert.accept()
#
#     def should_be_login_link(self):
#         assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
