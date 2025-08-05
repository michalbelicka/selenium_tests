from selenium_setup import *



def add_remove_element_broken_images(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")

    button_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Add/Remove Elements']")))
    assert button_click.is_displayed()
    button_click.click()


    add_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']")))
    assert add_element.is_displayed()
    add_element.click()

    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Delete']")))
    assert delete_button.is_displayed()
    delete_button.click()

    add_element_again = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']")))
    add_element_again.click()

    add_again = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']")))
    add_again.click()

    last_delete = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Delete'])[last()]")))
    last_delete.click()

    first_delete = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Delete']")))
    first_delete.click()

    driver.back()

    broken_images = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Broken Images']")))
    assert broken_images.is_displayed()
    broken_images.click()
    
    images = wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "img")))
    assert any(img.is_displayed() for img in images)
    assert len(images) > 0

    h3_broken_images = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    assert h3_broken_images.is_displayed()
    assert h3_broken_images.text == "Broken Images"
