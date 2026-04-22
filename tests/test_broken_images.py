from pages.broken_images_page import BrokenImagesPage

def test_broken_images(driver, wait):

    page = BrokenImagesPage(driver, wait)

    page.open()

    page.go_to_broken_images_link()
    
    assert len(page.get_images()) == 3

    assert page.get_header_text() == "Broken Images"