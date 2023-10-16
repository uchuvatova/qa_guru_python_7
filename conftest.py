import glob
import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from utils import *
import requests
from selene import query
from selene.support.shared import browser
import os

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


@pytest.fixture(scope='session', autouse=True)
def folder_management():
    if not os.path.exists(RESOURCES_PATH):
        os.mkdir('resources')
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')
    yield
    files = glob.glob(os.path.join(RESOURCES_PATH, "*"))
    for f in files:
        os.remove(f)
    os.remove(os.path.join(TMP_PATH, "test_archive.zip"))


@pytest.fixture(scope='session', autouse=True)
def download_pdf(folder_management):
    browser.open("/pdf")
    href = browser.element("[href='/samples/document/pdf/sample2.pdf']").get(query.attribute("href"))
    content = requests.get(href).content
    with open(os.path.join(RESOURCES_PATH, "sample.pdf"), 'wb') as f:
        f.write(content)


@pytest.fixture(scope='session', autouse=True)
def download_txt(folder_management):
    browser.open("/txt")
    href = browser.element("[href='/samples/document/txt/sample1.txt']").get(query.attribute("href"))
    content = requests.get(href).content
    with open(os.path.join(RESOURCES_PATH, "sample.txt"), 'wb') as f:
        f.write(content)


@pytest.fixture(scope='session', autouse=True)
def download_xls(folder_management):
    browser.open("/xls")
    href = browser.element("[href='/samples/document/xls/sample1.xls']").get(query.attribute("href"))
    content = requests.get(href).content
    with open(os.path.join(RESOURCES_PATH, "sample.xls"), 'wb') as f:
        f.write(content)


@pytest.fixture(scope='session', autouse=True)
def download_xlsx(folder_management):
    browser.open("/xlsx")
    href = browser.element("[href='/samples/document/xlsx/sample1.xlsx']").get(query.attribute("href"))
    content = requests.get(href).content
    with open(os.path.join(RESOURCES_PATH, "sample.xlsx"), 'wb') as f:
        f.write(content)
