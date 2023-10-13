import os.path
from utils import RESOURCES_PATH, PROJECT_ROOT_PATH
import requests
from selene import query
from selene.support.shared import browser
from pypdf import PdfReader
from xlrd import open_workbook
from openpyxl import load_workbook
import os


def test_download_pdf_file_with_selene_by_href():
    browser.open("/pdf")
    href = browser.element("[href='/samples/document/pdf/sample2.pdf']").get(query.attribute("href"))
    content = requests.get(href).content
    with open(os.path.join(RESOURCES_PATH, "sample.pdf"), 'wb') as f:
        f.write(content)
    reader = PdfReader(os.path.join(RESOURCES_PATH, "sample.pdf"))
    number_of_pages = len(reader.pages)
    print(number_of_pages)
    page = reader.pages[0]
    text = page.extract_text()
    assert "This is an example of a user fillable PDF form." in text

def test_download_txt_file_with_selene_by_href():
    browser.open("/txt")
    href = browser.element("[href='/samples/document/txt/sample1.txt']").get(query.attribute("href"))
    content = requests.get(href).content
    with open(os.path.join(RESOURCES_PATH, "sample.txt"), 'wb') as f:
        f.write(content)
    with open(os.path.join(RESOURCES_PATH, "sample.txt")) as f:
        text = f.read()
        assert "Lorem ipsum dolor sit amet, consectetur adipiscing elit." in text

def test_download_xls_file_with_selene_by_href():
    browser.open("/xls")
    href = browser.element("[href='/samples/document/xls/sample1.xls']").get(query.attribute("href"))
    content = requests.get(href).content
    with open(os.path.join(RESOURCES_PATH, "sample.xls"), 'wb') as f:
        f.write(content)
    book = open_workbook(os.path.join(RESOURCES_PATH, "sample.xls"))
    count_sheets = f"{book.nsheets}"
    sheet = book.sheet_by_index(0)
    text = sheet.cell_value(1, 1)
    assert book.sheet_names() == ['Example Test', 'Format Abbr.', 'Readme']
    assert count_sheets == "3"
    assert "What C datatypes are 8 bits?" in text

def test_download_xlsx_file_with_selene_by_href():
    browser.open("/xlsx")
    href = browser.element("[href='/samples/document/xlsx/sample1.xlsx']").get(query.attribute("href"))
    content = requests.get(href).content
    with open(os.path.join(RESOURCES_PATH, "sample.xlsx"), 'wb') as f:
        f.write(content)
    workbook = load_workbook(os.path.join(RESOURCES_PATH, "sample.xlsx"))
    sheet = workbook.active
    text = sheet.cell(row=2, column=1).value
    assert "2121" in text