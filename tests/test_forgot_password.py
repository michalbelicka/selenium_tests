from pages.forgot_password_page import ForgotPasswordPage

def test_forgot_password(driver, wait):

    page = ForgotPasswordPage(driver, wait)

    page.open()

    page.go_to_forgot_password()

    page.input_email("tester@mail.com")

    assert page.heading() == "Internal Server Error"

    # The page shows "Internal Server Error" after submitting email on Forgot Password — this is the expected behavior


