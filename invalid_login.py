from selenium_setup import *

def invalid_login(driver, wait):

    driver.get("https://the-internet.herokuapp.com/login")

    username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    assert username.is_displayed()
    username.send_keys("tester")

    password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    assert password.is_displayed()
    password.send_keys("heslo")

    login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "radius")))
    login.click()

    invalid = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert invalid.is_displayed()
    assert "Your username is invalid!" in invalid.text
    
    