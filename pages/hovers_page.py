from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class HoversPage:

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    HOVERS_LINK = (By.XPATH, "//a[text()='Hovers']")
    PROFILE_LINK = (By.XPATH, ".//a[text()='View profile']")
    HEADING = (By.TAG_NAME, "h1")

    def open(self):
        self.driver.get(self.URL)
    
    def go_to_hovers(self):
        hovers = self.wait.until(
            EC.element_to_be_clickable(self.HOVERS_LINK)
        )
        hovers.click()

    def hover_over_user(self, name):
        user_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@class='figure'][.//h5[text()='name: {name}']]"))
        )

        ActionChains(self.driver).move_to_element(user_element).perform()

        return user_element

    def click_view_profile(self, user_element):
        view_profile_link = user_element.find_element(*self.PROFILE_LINK)

        self.wait.until(
            lambda d: view_profile_link.is_displayed() and view_profile_link.is_enabled()
        )
        view_profile_link.click()

    def get_heading(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HEADING)
        ).text


        
