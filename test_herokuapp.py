import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from add_remove_elements_and_broken_images import add_remove_element_broken_images
from checkboxes import checkbox
from disappearing_elements import (open_disappear_elements, click_link_by_text, choice_of_elements, gallery_click)
from dropdown import dropdown
from dynamic_loading import dynamic_load
from file_upload import upload_file
from forgot_password import forgot_password
from inputs import inputs_and_expected
from status_codes import statuscodes
from valid_login import valid_login
from invalid_login import invalid_login
from key_presses import key_presses

@pytest.fixture(scope="session")
def driver():
    service = Service(ChromeDriverManager().install())
    # set Chrome to run headless and CI-friendly execution
    options = Options()
    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait

def test_add_remove_element_broken_images(driver, wait):
    add_remove_element_broken_images(driver, wait)
   
def test_checkboxes(driver, wait):
    checkbox(driver, wait)

def test_disappearing_elements(driver, wait):
    open_disappear_elements(driver, wait)
    click_link_by_text(wait, "Home")
    open_disappear_elements(driver, wait)
    click_link_by_text(wait, "About")
    choice_of_elements(driver, wait)
    click_link_by_text(wait, "Contact Us")
    choice_of_elements(driver, wait)
    click_link_by_text(wait, "Portfolio")
    choice_of_elements(driver, wait)
    gallery_click(driver, wait)

def test_dropdown(driver, wait):
    dropdown(driver, wait)

def test_key_presses(driver, wait):
    key_presses(driver, wait)

def test_dynamic_loading(driver, wait):
    dynamic_load(driver, wait)

def test_file_upload(driver, wait):
    upload_file(driver, wait)

def test_forgot_password(driver, wait):
    forgot_password(driver, wait)

@pytest.mark.parametrize("inputs, expected", [
    ("123", "123"),
    ("456", "456"),
    ("abc", ""),
    ("-789", "-789"),
    ("@!/", ""),
    ("", ""),
    ("-159*589", "-159589"),
])
def test_inputs_and_expected(inputs, expected, driver, wait):
    inputs_and_expected(inputs, expected, driver, wait)
    
def test_status_codes(driver, wait):
    statuscodes(driver, wait)

def test_invalid_login(driver, wait):
    invalid_login(driver, wait)

def test_valid_login(driver, wait):
    valid_login(driver, wait)