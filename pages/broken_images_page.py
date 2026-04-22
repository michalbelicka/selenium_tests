from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BrokenImagesPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    BROKEN_IMAGES_LINK = (By.XPATH, "//a[text()='Broken Images']")
    IMAGES = (By.XPATH, "//div[@id='content']//div[@class='example']//img")
    HEADER = (By.TAG_NAME, "h3")

    def open(self):
        self.driver.get(self.URL)
    
    def go_to_broken_images_link(self):
        link = self.wait.until(
            EC.element_to_be_clickable(self.BROKEN_IMAGES_LINK)
        )
        link.click()

    def get_images(self):
        images = self.wait.until(
            lambda d: d.find_elements(*self.IMAGES)
        )
        return images
    
    def get_header_text(self):
        header = self.wait.until(
            EC.visibility_of_element_located(self.HEADER)
        )
        return header.text



    
    
