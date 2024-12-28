import pathlib
import zipfile

def make_archive(filepaths,destination):
    dest_path = pathlib.Path(destination,"compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath,arcname=filepath.name)