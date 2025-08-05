from selenium_setup import *

def dynamic_load(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")

    dynamic_loading = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Dynamic Loading']")))
    assert dynamic_loading.is_displayed()
    dynamic_loading.click()

    example1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Example 1')]")))
    assert example1.is_displayed()
    example1.click()

    start1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']")))
    assert start1.is_displayed()
    start1.click()

    hello_world_h4_example1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
    assert hello_world_h4_example1.text == "Hello World!"
    driver.back()

    example2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Example 2: Element rendered after the fact']")))
    assert example2.is_displayed()
    example2.click()

    start2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']")))
    assert start2.is_displayed()
    start2.click()

    hello_world_h4_example2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4")))
    assert hello_world_h4_example2.text == "Hello World!"
    
