from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AddRemovePage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    ADD_REMOVE_ELEMENTS_LINK = (By.XPATH, "//a[text()='Add/Remove Elements']")
    ADD_ELEMENT = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTONS = (By.XPATH, "//button[text()='Delete']")


    def open(self):
        self.driver.get(self.URL)
    
    def go_to_add_remove_elements(self):
        link = self.wait.until(EC.element_to_be_clickable(self.ADD_REMOVE_ELEMENTS_LINK))
        link.click()
    
    def add_elements(self, count):
        for _ in range(count):
            add_element_button = self.wait.until(EC.element_to_be_clickable(self.ADD_ELEMENT))
            add_element_button.click()
    
    def get_delete_buttons_count(self):
        return len(self.driver.find_elements(*self.DELETE_BUTTONS))
    
    def delete_last_items(self, count):
        for _ in range(count):
            self.wait.until(
                lambda d: len(d.find_elements(*self.DELETE_BUTTONS)) > 0
                )
            buttons = self.driver.find_elements(*self.DELETE_BUTTONS)
            buttons[-1].click()

        


    