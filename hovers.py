from selenium_setup import *
from selenium.webdriver.common.action_chains import ActionChains

def hovers(driver, wait):
    driver.get("https://the-internet.herokuapp.com")

    hovers_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Hovers']")))
    assert hovers_link.is_displayed()
    hovers_link.click()

    actions = ActionChains(driver)

    for name in ["user1", "user2", "user3"]:
        user_element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@class='figure'][.//h5[text()='name: {name}']]")))

        actions.move_to_element(user_element).perform()

        view_profile_link = user_element.find_element(By.XPATH, ".//a[text()='View profile']")
        wait.until(lambda driver: view_profile_link.is_displayed() and view_profile_link.is_enabled())
        view_profile_link.click()

        h1_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        assert h1_element.text == "Not Found"

        driver.back()



