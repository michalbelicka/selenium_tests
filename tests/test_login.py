from pages.login_page import LoginPage

def test_invalid_login(driver, wait):

    page = LoginPage(driver, wait)

    page.open()

    page.enter_username("username")

    page.enter_password("password")

    page.click_login_button()

    assert page.get_flash_message() == "Your username is invalid!"


def test_valid_login(driver, wait):

    page = LoginPage(driver, wait)

    page.open()

    page.enter_username("tomsmith")

    page.enter_password("SuperSecretPassword!")

    page.click_login_button()

    page.get_flash_message() == "You logged into a secure area!"

    page.click_logout_button()

    assert page.get_flash_message() == "You logged out of the secure area!"