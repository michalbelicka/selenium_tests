from pages.file_upload_page import FileUploadPage
from pathlib import Path

def test_file_upload(driver, wait):

    BASE_DIR = Path(__file__).resolve().parents[1]
    file_path = BASE_DIR / "files" / "test_upload_file.txt"
    assert file_path.exists()

    page = FileUploadPage(driver, wait)

    page.open()

    page.go_to_file_upload()

    page.set_file(file_path)

    page.click_upload()

    success_message = page.get_success_message()
    assert success_message == "File Uploaded!"