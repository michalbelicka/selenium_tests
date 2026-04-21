from pages.add_remove_elements_page import AddRemovePage

def test_add_element(driver, wait):

    page = AddRemovePage(driver, wait)

    page.open()

    page.go_to_add_remove_elements()

    page.add_elements(1)

    count = page.get_delete_buttons_count()

    assert count == 1

def test_remove_added_element(driver, wait):

    page = AddRemovePage(driver, wait)

    page.open()

    page.go_to_add_remove_elements()

    page.add_elements(1)

    count = page.get_delete_buttons_count()

    assert count == 1

    page.delete_last_items(1)

    count = page.get_delete_buttons_count()
    
    assert count == 0

def test_add_and_remove_elements(driver, wait):

    page = AddRemovePage(driver, wait)

    page.open()

    page.go_to_add_remove_elements()

    page.add_elements(4)

    count = page.get_delete_buttons_count()

    assert count == 4

    page.delete_last_items(2)

    count = page.get_delete_buttons_count()

    assert count == 2

def test_add_and_remove_many_elements(driver, wait):

    page = AddRemovePage(driver, wait)

    page.open()

    page.go_to_add_remove_elements()

    page.add_elements(20)

    assert page.get_delete_buttons_count() == 20

    page.delete_last_items(20)
    
    assert page.get_delete_buttons_count() == 0






