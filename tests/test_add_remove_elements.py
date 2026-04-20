from pages.add_remove_elements_page import AddRemovePage

def test_add_element(driver, wait):

    page = AddRemovePage(driver, wait)

    page.open()
    page.go_to_add_remove_elements()
    page.click_add_element()
    count = page.get_delete_buttons_count()
    assert count == 1

def test_remove_added_element(driver, wait):

    page = AddRemovePage(driver, wait)

    page.open()
    page.go_to_add_remove_elements()
    page.click_add_element()
    count = page.get_delete_buttons_count()
    assert count == 1
    page.delete_last_item()
    count = page.get_delete_buttons_count()
    assert count == 0