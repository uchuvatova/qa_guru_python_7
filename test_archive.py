import zipfile, os
from utils import ARCHIVE_PATH, TXT_PATH, PDF_PATH, XLS_PATH, XLSX_PATH

def test_pdf(download_pdf):
    pdf_size_real = os.path.getsize(PDF_PATH)
    pdf_name_real = os.path.basename(PDF_PATH)
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='a') as z:
        z.write(filename=PDF_PATH, arcname='sample.pdf')
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='r') as z:
        pdf_info = z.getinfo('sample.pdf')
        pdf_name = pdf_info.filename
        pdf_size = pdf_info.file_size
        assert pdf_name == pdf_name_real
        assert pdf_size == pdf_size_real

def test_txt(download_txt):
    txt_size_real = os.path.getsize(TXT_PATH)
    txt_name_real = os.path.basename(TXT_PATH)
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='a') as z:
        z.write(filename=TXT_PATH, arcname='sample.txt')
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='r') as z:
        txt_info = z.getinfo('sample.txt')
        txt_name = txt_info.filename
        txt_size = txt_info.file_size
        with z.open('sample.txt') as txt:
            assert 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' in txt.read().decode('utf-8')
    assert txt_name == txt_name_real
    assert txt_size == txt_size_real

def test_xls(download_xls):
    xls_size_real = os.path.getsize(XLS_PATH)
    xls_name_real = os.path.basename(XLS_PATH)
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='a') as z:
        z.write(filename=XLS_PATH, arcname='sample.xls')
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='r') as z:
        xls_info = z.getinfo('sample.xls')
        xls_name = xls_info.filename
        xls_size = xls_info.file_size
    assert xls_name == xls_name_real
    assert xls_size == xls_size_real

def test_xlsx(download_xlsx):
    xlsx_size_real = os.path.getsize(XLSX_PATH)
    xlsx_name_real = os.path.basename(XLSX_PATH)
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='a') as z:
        z.write(filename=XLSX_PATH, arcname='sample.xlsx')
    with zipfile.ZipFile(file=ARCHIVE_PATH, mode='r') as z:
        xlsx_info = z.getinfo('sample.xlsx')
        xlsx_name = xlsx_info.filename
        xlsx_size = xlsx_info.file_size
    assert xlsx_name == xlsx_name_real
    assert xlsx_size == xlsx_size_real

