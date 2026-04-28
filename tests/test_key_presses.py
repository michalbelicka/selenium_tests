from pages.key_presses_page import KeyPressesPage
from selenium.webdriver.common.keys import Keys

def test_key_presses(driver, wait):

    page = KeyPressesPage(driver, wait)

    page.open()

    page.go_to_key_presses()

    data = [
    (Keys.ENTER, "ENTER"),
    (Keys.TAB, "TAB"),
    (Keys.SHIFT, "SHIFT"),
    (Keys.CONTROL, "CONTROL"),
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),
    (Keys.ALT, "ALT"),
    ]
    
    for key, expected in data:
        page.press_key(key)

        actual = page.get_result_text()
        assert expected in actual, f"Expected: {expected}, got {actual}"