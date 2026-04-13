from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
    
    def click_add_element(self):
        add_element_button = self.wait.until(EC.element_to_be_clickable(self.ADD_ELEMENT))
        add_element_button.click()
    
    def get_delete_buttons_count(self):
        delete_buttons = self.wait.until(EC.visibility_of_all_elements_located(self.DELETE_BUTTONS))
        return len(delete_buttons)
    
    def click_delete_button_by_index(self, index):
        delete_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"(//button[text()='Delete'])[{index + 1}]")
            ))
        delete_button.click()

        


    