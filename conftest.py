import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Добавляем парсер, который будет считывать опции, которые пользователь передает через терминал при запуске теста
def pytest_addoption(parser):
    # Браузер: передается через опцию --browser=браузернейм, по умолчанию Хром
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    # Локаль браузера: передается через опцию --language=локаль, по умолчанию английский язык
    parser.addoption('--language', action='store', default="en", help='Choose browser language')


# Фикстуры, которые будут применяться ко всем тестам в сьюте
@pytest.fixture(scope='function')  # Параметр 'function' передается по умолчанию
# Функция принимает на вход request, то есть то, что мы ввели в консоли через addoption: browser, language
def browser(request):
    # Получаем название браузера из параметров в терминале или берем дефолтное значение, если параметр не бы передан
    browser_name = request.config.getoption('browser')
    browser = None
    # Если браузер = Хром, то
    if browser_name == 'chrome':
        print('\nstart chrome browser for test..')
        # Забираем название локали из параметров в терминале или берем дефолтное значение, если параметр не бы передан
        user_language = request.config.getoption('language')
        # используем класс Options и метод add_experimental_option, чтобы указать язык бразуера
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # Используем значение указанных опций локали при запуске бразуера
        browser = webdriver.Chrome(options=options)
    # Если браузер = Firefox
    elif browser_name == 'firefox':
        print('\nstart firefox browser for test..')
        # Забираем название локали из параметров в терминале или берем дефолтное значение, если параметр не бы передан
        user_language = request.config.getoption('language')
        # Объявляем язык бразуера
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        # Используем значение указанных опций локали при запуске бразуера
        browser = webdriver.Firefox(firefox_profile=fp)
    # Если ввели не Хром или ФФ, а несуществующее имя браузера
    else:
        print(f'Browser {browser_name} still is not implemented')
    # По завершении всех функций в бразуере
    yield browser
    print('\nquit browser..')
    # Закрываем само окошко браузера, чтобы не жрать оперативку кучей висячих открытых окон
    browser.quit()
