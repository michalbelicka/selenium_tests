from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MultipleWindowsPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    MULTIPLE_WINDOWS_LINK = (By.XPATH, "//a[text()='Multiple Windows']")
    HERE_LINK = (By.XPATH, "//a[text()='Click Here']")
    H3_HEADING = (By.TAG_NAME, "h3")

    def open(self):
        self.driver.get(self.URL)

    def go_to_multiple_windows(self):
        multiple_windows_link = self.wait.until(
            EC.element_to_be_clickable(self.MULTIPLE_WINDOWS_LINK)
        )
        multiple_windows_link.click()
    
    def click_here(self):
        click_here = self.wait.until(
            EC.element_to_be_clickable(self.HERE_LINK)
        )
        click_here.click()

    def switch_to_new_window(self, original_window):
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                return
    
    def get_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.H3_HEADING)
        ).text

    
