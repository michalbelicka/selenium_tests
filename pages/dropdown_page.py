from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
class DropdownPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    DROPDOWN_LINK = (By.XPATH, "//a[text()='Dropdown']")
    DROPDOWN = (By.ID, "dropdown")

    def open(self):
        self.driver.get(self.URL)
    
    def go_to_dropdown_page(self):
        link = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_LINK))
        link.click()
        
    def select_by_value(self, value):
        select_options = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN))
        select = Select(select_options)
        select.select_by_value(value)
        return select.first_selected_option

    def select_by_text(self, text):
        select_options = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN))
        select = Select(select_options)
        select.select_by_visible_text(text)
        return select.first_selected_option

    
