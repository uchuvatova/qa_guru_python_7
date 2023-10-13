import zipfile, os
from utils import RESOURCES_PATH, TMP_PATH, ARCHIVE_PATH


def test_create_zip():
    file_dir = os.listdir(RESOURCES_PATH)
    with zipfile.ZipFile('test_archive.zip', mode='w', \
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(RESOURCES_PATH, file)
            zf.write(add_file)

    os.rename('test_archive.zip', os.path.join(TMP_PATH, "test_archive.zip"))

    with zipfile.ZipFile(os.path.join(TMP_PATH, "test_archive.zip"), mode='a') as zf:
        for file in zf.infolist():
            name = os.path.basename(file.filename) # имя файла в архиве без пути
            print(f"{name}") # печатаем имя


def test_archived_files():
    resources_content = os.listdir(RESOURCES_PATH)
    archive_content = zipfile.ZipFile(ARCHIVE_PATH, "r").namelist()
    assert resources_content == archive_content
