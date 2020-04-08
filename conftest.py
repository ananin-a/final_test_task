import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """
    Надстройка принимающая значение "parser", переданные через терминал пользователем.

    --browser=chrome or firefox: default="chrome"

    --language=en or ru: default="en"
    """
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en", help="Choose browser: language")


@pytest.fixture(scope="function")
# Функция принимает на вход request, то есть то, что мы ввели в консоли через addoption: browser, language
def browser(request):
    """
    Принимает на вход то, что мы ввели в консоли через addoption: browser, language
    """
    browser_name = request.config.getoption("browser")
    # Получаем название браузера из параметров в терминале или берем дефолтное значение, если параметр не бы передан
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # Забираем название локали из параметров в терминале или берем дефолтное значение, если параметр не бы передан
        user_language = request.config.getoption("language")
        # используем класс Options и метод add_experimental_option, чтобы указать язык бразуера
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        # Используем значение указанных опций локали при запуске бразуера
        browser: webdriver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        # Забираем название локали из параметров в терминале или берем дефолтное значение, если параметр не бы передан
        user_language = request.config.getoption("language")
        # Объявляем язык бразуера
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        # Используем значение указанных опций локали при запуске бразуера
        browser: webdriver = webdriver.Firefox(firefox_profile=fp)
    else:
        print(f"Browser {browser_name} still is not implemented")
    # По завершении всех функций в бразуере
    yield browser
    print("\nquit browser...")
    browser.quit()
