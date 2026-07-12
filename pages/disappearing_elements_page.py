from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class DisappearingElementsPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    DISAPPEARING_ELEMENTS_LINK = (By.XPATH, "//a[text()='Disappearing Elements']")
    WELCOME_HEADING = (By.TAG_NAME, "h1")
    NOT_FOUND_HEADING = (By.TAG_NAME, "h1")
    GALLERY_LINK = (By.XPATH, "//a[text()='Gallery']")

    def open(self):
        self.driver.get(self.URL)

    def go_to_disappearing_elements(self):
        elements_link = self.wait.until(
            EC.element_to_be_clickable(self.DISAPPEARING_ELEMENTS_LINK)
        )
        elements_link.click()

    def not_found_heading_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.NOT_FOUND_HEADING)
        ).text

    def click_link_by_text(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//a[text()='{text}']"))
        )
        element.click()
    
    def welcome_heading_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.WELCOME_HEADING)
        ).text

    def click_gallery_link(self):
        short_wait = WebDriverWait(self.driver, 1)

        for _ in range(15):
            self.driver.refresh()
            try:
                gallery = short_wait.until(
                    EC.element_to_be_clickable(self.GALLERY_LINK)
                )
                gallery.click()
                return
            except TimeoutException:
                continue

        raise TimeoutException("Gallery link was not found after 15 attempts")


    