import zipfile

def extract_archive(archive_path, des_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(des_dir)

if __name__ == "__main__":
    extract_archive(
        r"C:\Users\spsp1\PycharmProjects\pythonProject1\filess\compressed (1).zip",
        r"C:\Users\spsp1\PycharmProjects\pythonProject1\filess"  )
