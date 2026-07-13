from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InputsPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    INPUTS_LINK = (By.XPATH, "//a[text()='Inputs']")
    INPUTS_FIELD = (By.CSS_SELECTOR, "input[type='number']")

    def open(self):
        self.driver.get(self.URL)

    def go_to_inputs(self):
        inputs_link = self.wait.until(
            EC.element_to_be_clickable(self.INPUTS_LINK)
        )
        inputs_link.click()

    def enter_value(self, value):
        input_field = self.wait.until(
            EC.element_to_be_clickable(self.INPUTS_FIELD)
        )
        input_field.clear()
        input_field.send_keys(value)

    def get_input_value(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.INPUTS_FIELD)
        ).get_attribute("value")

    