import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from abstract.selenium_listener import Listener


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximazed')
    options.add_argument('--window-size=1800,900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
# scope='session' - все тесты в одном браузере
def setup(request, get_webdriver):
    driver = get_webdriver
    driver = EventFiringWebDriver(driver, Listener())
    url = 'https://www.macys.com/'

    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)

    yield driver
    # Закрывает вкладку
    # driver.close()
    # Закрывает все вкладки
    driver.quit()
