from selenium_setup import *

def checkbox(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")

    checkboxes = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Checkboxes']")))
    assert checkboxes.is_displayed()
    checkboxes.click()

    boxes_located = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']")))

    if not boxes_located[0].is_selected():
        boxes_located[0].click()
    assert boxes_located[0].is_selected()
    
    if boxes_located[1].is_selected():
        boxes_located[1].click()
    assert not boxes_located[1].is_selected()
