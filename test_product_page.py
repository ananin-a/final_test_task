from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_url()
    page.should_be_button_add_basket()
    page.add_product_to_basket()
    page.should_be_adding_confirmation()
    page.name_added_should_be_correct()
    page.price_comparison()
