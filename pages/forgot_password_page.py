from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ForgotPasswordPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Forgot Password']")
    INPUT_EMAIL = (By.ID, "email")
    HEADING = (By.TAG_NAME, "h1")

    def open(self):
        self.driver.get(self.URL)

    def go_to_forgot_password(self):
        forgot_password = self.wait.until(
            EC.element_to_be_clickable(self.FORGOT_PASSWORD_LINK)
        )
        forgot_password.click()
    
    def input_email(self, email):
        input_email = self.wait.until(
            EC.element_to_be_clickable(self.INPUT_EMAIL)
        )
        input_email.send_keys(email, Keys.ENTER)

    def heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HEADING)
        ).text