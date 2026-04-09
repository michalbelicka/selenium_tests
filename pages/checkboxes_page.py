from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CheckboxesPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    CHECKBOXES_LINK = (By.XPATH, "//a[text()='Checkboxes']")
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def open(self):
        self.driver.get(self.URL)
    
    def go_to_checkboxes_page(self):
        link = self.wait.until(EC.element_to_be_clickable(self.CHECKBOXES_LINK))
        link.click()
    
    def check(self, index):
        elements = self.wait.until(EC.presence_of_all_elements_located(self.CHECKBOXES))
        checkbox = elements[index]
        self.wait.until(lambda driver: checkbox.is_displayed() and checkbox.is_enabled())
        
        if not checkbox.is_selected():
            checkbox.click()
        
    def uncheck(self, index):
        elements = self.wait.until(EC.presence_of_all_elements_located(self.CHECKBOXES))
        checkbox = elements[index]
        self.wait.until(lambda driver: checkbox.is_displayed() and checkbox.is_enabled())
        
        if checkbox.is_selected():
            checkbox.click()

    def is_checked(self, index):
        checkbox = self.wait.until(EC.visibility_of_all_elements_located(self.CHECKBOXES))[index]
        return checkbox.is_selected()
    


    