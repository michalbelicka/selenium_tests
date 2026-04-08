from pages.dropdown_page import DropdownPage

def test_dropdown(driver, wait):

    page = DropdownPage(driver, wait)

    # open main page and go to dropdown
    page.open()
    page.go_to_dropdown_page()

    # select option by value
    selected_option = page.select_by_value("1")
    assert selected_option.get_attribute("value") == "1", "Value 1 wasn't selected"
    assert selected_option.is_displayed(), "Selected option is not visible"

    # select option by text
    selected_option = page.select_by_text("Option 2")
    assert selected_option.text == "Option 2", "Text of selected option 2 is not 'Option 2'"
    assert selected_option.is_displayed(), "Selected option is not visible"
    
    

