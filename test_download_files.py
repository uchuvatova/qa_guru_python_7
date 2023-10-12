import os.path
import time

import requests
from selene import query
from selene.support.shared import browser

from conftest import options


def test_download_file_with_selene_by_href():
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")

    href = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    content = requests.get(href).content
    with open("pytest_readme.rst", 'wb') as f:
        f.write(content)

    with open("pytest_readme.rst") as f:
        text = f.read()
        assert "framework makes it easy to write" in text


def test_download_file_with_selene_by_button():
    os.makedirs('tmp', exist_ok=True)
    prefs = {"download.default_directory": 'tmp'}
    options.add_experimental_option("prefs", prefs)

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.element("[data-testid='download-raw-button']").click()

    time.sleep(5)  # слип здесь только для демонстрации

    with open('tmp/README.rst') as f:
        text = f.read()
        assert "framework makes it easy to write" in text
