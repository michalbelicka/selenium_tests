from selenium_setup import *
from selenium.webdriver.common.action_chains import ActionChains

def key_presses(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")

    key_presses_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Key Presses']")))
    assert key_presses_link.is_displayed()
    key_presses_link.click()

    keys_list = [Keys.ENTER, Keys.TAB, Keys.SHIFT, Keys.CONTROL, "a", "b", "c", Keys.ALT]
    expected_text = ["ENTER", "TAB", "SHIFT", "CONTROL", "A", "B", "C", "ALT"]

    actions = ActionChains(driver)
    for key, expected in zip(keys_list, expected_text):
        actions.send_keys(key)
        actions.perform()
        result = wait.until(EC.visibility_of_element_located((By.ID, "result")))
        assert expected in result.text
    
