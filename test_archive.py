import zipfile, os
import shutil
def test_create_zip():
    path = "./resources/"
    file_dir = os.listdir(path)

    with zipfile.ZipFile('test_archive.zip', mode='w', \
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file)
    with zipfile.ZipFile('test_archive.zip', mode='a') as zf:
        for file in zf.infolist():
            name = os.path.basename(file.filename) # имя файла в архиве без пути
            print(f"{name}") # печатаем имя, начальный размер, размер в архиве