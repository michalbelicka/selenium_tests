from selenium_setup import *
from selenium.webdriver.support.ui import Select

def dropdown(driver, wait):
    driver.get("https://the-internet.herokuapp.com/")

    dropdown_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Dropdown']")))
    assert dropdown_link.is_displayed()
    dropdown_link.click()

    select_options = wait.until(EC.presence_of_element_located((By.ID, "dropdown")))
    select = Select(select_options)

    select.select_by_value("1")
    selected_option = select.first_selected_option
    assert selected_option.get_attribute("value") == "1"

    select.select_by_value("2")
    selected_option = select.first_selected_option
    assert selected_option.get_attribute("value") == "2"
   
    