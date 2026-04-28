from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class KeyPressesPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    KEY_PRESSES_LINK = (By.XPATH, "//a[text()='Key Presses']")
    RESULT_TEXT = (By.ID, "result")

    def open(self):
        self.driver.get(self.URL)

    def go_to_key_presses(self):
        link = self.wait.until(
            EC.element_to_be_clickable(self.KEY_PRESSES_LINK)
        )
        link.click()
    
    def press_key(self, key):
        actions = ActionChains(self.driver)
        actions.send_keys(key)
        actions.perform()

    def get_result_text(self):
        result = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_TEXT)
        )
        return result.text
