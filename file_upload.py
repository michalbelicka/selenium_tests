import os
from selenium_setup import *

def upload_file(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")

    file_upload = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='File Upload']")))
    assert file_upload.is_displayed()
    file_upload.click()

    choose_file = wait.until(EC.element_to_be_clickable((By.ID, "file-upload")))
    assert choose_file.is_displayed()
    file_path = os.path.abspath("files/test_upload_file.txt")
    assert os.path.exists(file_path)
    choose_file.send_keys(file_path)


    upload_button = wait.until(EC.element_to_be_clickable((By.ID, "file-submit")))
    assert upload_button.is_displayed()
    upload_button.click()

    file_uploaded = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='File Uploaded!']")))
    assert file_uploaded.is_displayed()
    assert file_uploaded.text == "File Uploaded!"

