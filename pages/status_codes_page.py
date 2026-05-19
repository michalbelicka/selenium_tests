from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class StatusCodesPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    STATUS_CODES_LINK = (By.XPATH, "//a[text()='Status Codes']")
    HERE_LINK = (By.XPATH, "//a[text()='here']")

    def open(self):
        self.driver.get(self.URL)

    def open_status_codes(self):
        status_codes = self.wait.until(
            EC.element_to_be_clickable(self.STATUS_CODES_LINK)
        )
        status_codes.click()

    def click_here_link(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.HERE_LINK)
        )
        element.click()
        
    def open_code(self, code):
        code_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[text()='{code}']")
            )
        )
        code_link.click()
    
    def text_present(self, code):
        text = self.wait.until(
            EC.text_to_be_present_in_element(
                (By.XPATH, f"//p[contains(text(), '{code}')]"), f"{code}"
            )
        )
        return text
