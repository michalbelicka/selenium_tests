from pages.hovers_page import HoversPage

def test_hovers(driver, wait):

    page = HoversPage(driver, wait)

    page.open()

    page.go_to_hovers()

    for name in ["user1", "user2", "user3"]:
        user_element = page.hover_over_user(name)

        page.click_view_profile(user_element)

        assert page.get_heading() == "Not Found"
        
        driver.back()