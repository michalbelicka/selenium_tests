import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from valid_login import valid_login
from invalid_login import invalid_login

@pytest.fixture(scope="session")
def driver():
    service = Service(ChromeDriverManager().install())
    # set Chrome to run headless and CI-friendly execution
    options = Options()
    if os.getenv("HEADLESS") == "true":
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--incognito")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait

def test_invalid_login(driver, wait):
    invalid_login(driver, wait)

def test_valid_login(driver, wait):
    valid_login(driver, wait)