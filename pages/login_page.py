from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class LoginPage:

    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    FLASH = (By.ID, "flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a[href='/logout']")

    def open(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        username_input = self.wait.until(
            EC.element_to_be_clickable(self.USERNAME)
        )
        username_input.send_keys(username)
    
    def enter_password(self, password):
        password_input = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD)
        )
        password_input.send_keys(password)
    
    def click_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()

    def get_flash_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.FLASH)
        ).text.replace("×", "").strip()

    def click_logout_button(self):
        logout_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        logout_button.click()

    
    