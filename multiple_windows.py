from selenium_setup import *

def multiple_windows(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")

    multiple_windows_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Multiple Windows']")))
    assert multiple_windows_link.is_displayed()
    multiple_windows_link.click()

    original_window = driver.current_window_handle

    click_here = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Click Here']")))
    assert click_here.is_displayed()
    click_here.click()
    assert len(driver.window_handles) == 2

    for window in driver.window_handles:
        if window != original_window:
            driver.switch_to.window(window)
            break

    h3_new_window = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    assert h3_new_window.text == "New Window"

    driver.close()
    driver.switch_to.window(original_window)

    h3_opening_a_new_window = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    assert h3_opening_a_new_window.text == "Opening a new window"
    