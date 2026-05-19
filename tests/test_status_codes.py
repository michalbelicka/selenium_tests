from pages.status_codes_page import StatusCodesPage

def test_status_codes(driver, wait):

    page = StatusCodesPage(driver, wait)

    page.open()

    page.open_status_codes()

    for code in [200, 301, 404, 500]:

        page.open_code(code)

        assert page.text_present(code)

        page.click_here_link()