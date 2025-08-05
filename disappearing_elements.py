from selenium_setup import *

def choice_of_elements(driver, wait):
    driver.get("https://the-internet.herokuapp.com/disappearing_elements")
    heading = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    assert heading.is_displayed()
    assert heading.text == "Disappearing Elements"

def open_disappear_elements(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")
    de = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Disappearing Elements']")))
    assert de.is_displayed()
    de.click()

def click_link_by_text(wait, text):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{text}']")))
    assert element.is_displayed()
    element.click()
    if text in ["About", "Contact Us", "Portfolio"]:
        not_found(wait)

def not_found(wait):
    h1_not_found = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
    assert h1_not_found.is_displayed()
    assert h1_not_found.text == "Not Found"

def gallery_click(driver, wait):  
    for attempt in range(15):
        driver.refresh()
        short_wait = WebDriverWait(driver, 1)
        try:
            gallery = short_wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Gallery']")))
            if gallery.is_displayed():                 
                gallery.click()
                not_found(wait)
                break
        except Exception as e:
            print(f"Attempt: {attempt +1}, Gallery is not found yet. Exception: {e}")
            continue
