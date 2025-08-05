from selenium_setup import *
import pytest

@pytest.mark.parametrize("inputs, expected", [
    ("123", "123"),
    ("456", "456"),
    ("abc", ""),              # invalid characters, expect empty string
    ("-789", "-789"),
    ("@!/", ""),              # special characters, expect empty string
    ("", ""),
    ("-159*589", "-159589"),  # expect that '*' is ignored or removed
])
def inputs_and_expected(inputs, expected, driver, wait):
    # Tests what happens when different characters are typed into a number input field
    driver.get("https://the-internet.herokuapp.com/")

    inputs_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Inputs']")))
    assert inputs_link.is_displayed()
    inputs_link.click()

    input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='number']")))
    input_field.clear()
    input_field.send_keys(inputs)
    assert input_field.get_attribute("value") == expected
