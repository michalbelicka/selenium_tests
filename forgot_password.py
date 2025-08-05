from selenium_setup import *

def forgot_password(driver, wait):

    driver.get("https://the-internet.herokuapp.com/")

    forgot_password = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Forgot Password']")))
    assert forgot_password.is_displayed()
    forgot_password.click()

    input_email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    assert input_email.is_displayed()
    input_email.send_keys("tester@mail.com", Keys.ENTER)

    confirmation = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    assert confirmation.is_displayed()
    assert confirmation.text == "Internal Server Error"
    # The page shows "Internal Server Error" after submitting email on Forgot Password — this is the expected behavior
  