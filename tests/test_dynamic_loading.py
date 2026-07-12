from pages.dynamic_loading_page import DynamicLoadingPage

def test_dynamic_loading(driver, wait):

    page = DynamicLoadingPage(driver, wait)

    page.open()

    page.go_to_dynamic_loading()

    page.open_example_1()

    page.click_start()

    assert page.get_heading() == "Hello World!"

    driver.back()

    page.open_example_2()

    page.click_start()

    assert page.get_heading() == "Hello World!"

