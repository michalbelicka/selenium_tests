from pages.checkboxes_page import CheckboxesPage

def test_checkboxes(driver, wait):

    page = CheckboxesPage(driver, wait)

    # open main page and go to checkboxes
    page.open()
    page.go_to_checkboxes_page()

    # check the first checkbox
    page.check(0)
    assert page.is_checked(0)

    # uncheck the first checkbox
    page.uncheck(0)
    assert not page.is_checked(0)

    # uncheck the second checkbox
    page.uncheck(1)
    assert not page.is_checked(1)

    # check the second checkbox
    page.check(1)
    assert page.is_checked(1)
    