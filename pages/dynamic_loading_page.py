from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class DynamicLoadingPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    DYNAMIC_LOADING_LINK = (By.XPATH, "//a[text()='Dynamic Loading']")
    START_BUTTON = (By.XPATH, "//button[text()='Start']")
    HELLO_WORLD_HEADING = (By.CSS_SELECTOR, "#finish h4")
    EXAMPLE_1_LINK = (By.XPATH, "//a[contains(text(), 'Example 1')]")
    EXAMPLE_2_LINK = (By.XPATH, "//a[contains(text(), 'Example 2')]")

    def open(self):
        self.driver.get(self.URL)

    def go_to_dynamic_loading(self):
        dynamic_loading = self.wait.until(
            EC.element_to_be_clickable(self.DYNAMIC_LOADING_LINK)
        )
        dynamic_loading.click()

    def open_example_1(self):
        example_1 = self.wait.until(
            EC.element_to_be_clickable(self.EXAMPLE_1_LINK)
        )
        example_1.click()
    
    def click_start(self):
        button = self.wait.until(
            EC.element_to_be_clickable(self.START_BUTTON)
        )
        button.click()
    
    def get_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HELLO_WORLD_HEADING)
        ).text

    def open_example_2(self):
        example_2 = self.wait.until(
            EC.element_to_be_clickable(self.EXAMPLE_2_LINK)
        )
        example_2.click()

    
