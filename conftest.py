import glob
import os
import pytest
from selene.support.shared import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import TMP_PATH, RESOURCES_PATH

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
    if not os.path.exists(RESOURCES_PATH):
        os.mkdir('resources')
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')

    yield

    browser.quit()
    os.remove(os.path.join(TMP_PATH, "test_archive.zip"))
    files = glob.glob(os.path.join(RESOURCES_PATH, "*"))
    for f in files:
        os.remove(f)