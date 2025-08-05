from selenium_setup import *

def click_link_by_text(wait, text):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{text}']")))
    assert element.is_displayed()
    element.click()

def statuscodes(driver, wait):
    
    driver.get("https://the-internet.herokuapp.com/")

    status_codes = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Status Codes']")))
    assert status_codes.is_displayed()
    status_codes.click()

    for code in [200, 301, 404, 500]:
        click_the_code = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[text()='{code}']")))
        click_the_code.click()
        text_present = wait.until(EC.text_to_be_present_in_element((By.XPATH, f"//p[contains(text(), '{code}')]"), f"{code}"))
        assert text_present
        click_link_by_text(wait, "here")
       
   
 
        





    # code_200 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='200']")))
    # code_200.click()

    # code_200_here = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='here']")))
    # code_200_here.click()

    # code_301 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='301']")))
    # code_301.click()

    # c_301_here = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='here']")))
    # c_301_here.click()

    # code_404 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='404']")))
    # code_404.click()

    # c_404_here = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='here']")))
    # c_404_here.click()

    # code_500 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='500']")))
    # code_500.click()
    
    # c_500_here = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='here']")))
    # c_500_here.click()

    
    