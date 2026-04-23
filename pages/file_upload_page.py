from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class FileUploadPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    FILE_UPLOAD_LINK = (By.XPATH, "//a[text()='File Upload']")
    FILE_INPUT = (By.ID, "file-upload")
    UPLOAD_BUTTON = (By.ID, "file-submit")
    SUCCESS_MESSAGE = (By.XPATH, "//h3[text()='File Uploaded!']")

    def open(self):
        self.driver.get(self.URL)
    
    def go_to_file_upload(self):
        link = self.wait.until(
            EC.element_to_be_clickable(self.FILE_UPLOAD_LINK)
        )
        link.click()

    def set_file(self, file_path):
        file_input = self.wait.until(
            EC.visibility_of_element_located(self.FILE_INPUT)
        )
        file_input.send_keys(str(file_path))

    def click_upload(self):
        upload_button = self.wait.until(
            EC.element_to_be_clickable(self.UPLOAD_BUTTON)
        )
        upload_button.click()

    def get_success_message(self):
        success_message = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
        return success_message.text


        
    
