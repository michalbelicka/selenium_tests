from pages.multiple_windows_page import MultipleWindowsPage

def test_multiple_windows(driver, wait):

    page = MultipleWindowsPage(driver, wait)

    page.open()

    page.go_to_multiple_windows()

    original_window = driver.current_window_handle

    page.click_here()

    assert len(driver.window_handles) == 2

    page.switch_to_new_window(original_window)

    assert page.get_heading() == "New Window"

    driver.close()

    driver.switch_to.window(original_window)

    assert page.get_heading() == "Opening a new window"