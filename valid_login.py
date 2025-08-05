from selenium_setup import *

def valid_login(driver, wait):

    driver.get("https://the-internet.herokuapp.com/login")

    username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    assert username.is_displayed()
    username.send_keys("tomsmith")

    password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']")))
    assert password.is_displayed()
    password.send_keys("SuperSecretPassword!", Keys.ENTER)

    secure_area_h2 = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
    assert secure_area_h2.text == "Secure Area"