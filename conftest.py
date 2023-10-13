import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(options=options)
browser.config.driver = driver

@pytest.fixture(scope='session', autouse=True)
def browser_management():
    browser.config.base_url = 'https://filesamples.com/formats'
    browser.config.timeout = 2.0
    browser.config.window_width = 1900
    browser.config.window_heigth = 1200


    yield

    browser.quit()