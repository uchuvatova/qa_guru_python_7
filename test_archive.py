import zipfile
import xlrd
from openpyxl.reader.excel import load_workbook
from pypdf import PdfReader

from utils import *


def test_create_zip():
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='w') as z:
        z.write(filename=PDF_PATH, arcname='sample.pdf')
        z.write(filename=TXT_PATH, arcname='sample.txt')
        z.write(filename=XLS_PATH, arcname='sample.xls')
        z.write(filename=XLSX_PATH, arcname='sample.xlsx')
    assert os.path.isfile(ARCHIVE_PATH)


def test_pdf(download_pdf):
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='r') as z:
        with z.open('sample.pdf') as pdf:
            pdf_file_zip = PdfReader(pdf)
            pdf_pages_zip = len(pdf_file_zip.pages)
            pdf_text_zip = pdf_file_zip.pages[0].extract_text()
            pdf_info = z.getinfo('sample.pdf')
            pdf_name_zip = pdf_info.filename
            pdf_size_zip = pdf_info.file_size
        pdf_size_real = os.path.getsize(PDF_PATH)
        pdf_name_real = os.path.basename(PDF_PATH)
        reader = PdfReader(PDF_PATH)
        pdf_pages_real = len(reader.pages)
        pdf_text_real = reader.pages[0].extract_text()
        assert pdf_name_zip == pdf_name_real
        assert pdf_size_zip == pdf_size_real
        assert pdf_pages_zip == pdf_pages_real
        assert pdf_text_zip == pdf_text_real


def test_txt(download_txt):
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='r') as z:
        txt_info_zip = z.getinfo('sample.txt')
        txt_name_zip = txt_info_zip.filename
        txt_size_zip = txt_info_zip.file_size
        with z.open('sample.txt') as txt_zip:
            txt_text_zip = txt_zip.read().decode('utf-8')
    with open(TXT_PATH) as f:
        txt_text_real = f.read()
    txt_size_real = os.path.getsize(TXT_PATH)
    txt_name_real = os.path.basename(TXT_PATH)
    assert txt_name_zip == txt_name_real
    assert txt_size_zip == txt_size_real
    assert txt_text_zip == txt_text_real


def test_xls(download_xls):
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='r') as z:
        with z.open('sample.xls') as book:
            xls_file_zip = xlrd.open_workbook(file_contents=book.read())
        xls_info_zip = z.getinfo('sample.xls')
        xls_name_zip = xls_info_zip.filename
        xls_size_zip = xls_info_zip.file_size
    xls_file_real = xlrd.open_workbook(XLS_PATH)
    xls_size_real = os.path.getsize(XLS_PATH)
    xls_name_real = os.path.basename(XLS_PATH)
    assert xls_name_zip == xls_name_real
    assert xls_size_zip == xls_size_real
    assert xls_file_zip.sheet_names() == xls_file_real.sheet_names()


def test_xlsx(download_xlsx):
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='r') as z:
        with z.open('sample.xlsx') as book:
            xlsx_text_zip = load_workbook(book).active.cell(row=2, column=1).value
        xlsx_info = z.getinfo('sample.xlsx')
        xlsx_name_zip = xlsx_info.filename
        xlsx_size_zip = xlsx_info.file_size
    xlsx_text_real = load_workbook(XLSX_PATH).active.cell(row=2, column=1).value
    xlsx_size_real = os.path.getsize(XLSX_PATH)
    xlsx_name_real = os.path.basename(XLSX_PATH)
    assert xlsx_name_real == xlsx_name_zip
    assert xlsx_size_real == xlsx_size_zip
    assert xlsx_text_real == xlsx_text_zip
