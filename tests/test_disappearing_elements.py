from pages.disappearing_elements_page import DisappearingElementsPage

def test_disappearing_elements(driver, wait):

    page = DisappearingElementsPage(driver, wait)

    page.open()

    page.go_to_disappearing_elements()

    page.click_link_by_text("Home")

    assert page.welcome_heading_text() == "Welcome to the-internet"

    page.go_to_disappearing_elements()

    broken_links = ["About", "Contact Us", "Portfolio"]
    for link in broken_links:
        page.click_link_by_text(link)
        assert page.not_found_heading_text() == "Not Found"
        driver.back()
    
    page.click_gallery_link()

    assert page.not_found_heading_text() == "Not Found"