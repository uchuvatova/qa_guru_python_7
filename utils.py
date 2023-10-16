import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(PROJECT_ROOT_PATH, 'resources')
PDF_PATH = os.path.join(RESOURCES_PATH, 'sample.pdf')
TXT_PATH = os.path.join(RESOURCES_PATH, 'sample.txt')
XLS_PATH = os.path.join(RESOURCES_PATH, 'sample.xls')
XLSX_PATH = os.path.join(RESOURCES_PATH, 'sample.xlsx')
TMP_PATH = os.path.join(PROJECT_ROOT_PATH, 'tmp')
ARCHIVE_PATH = os.path.join(TMP_PATH, 'test_archive.zip')
