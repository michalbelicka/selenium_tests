# Selenium Test Project

## Overview

This is a demo project for learning and practicing Selenium.
This project tests different parts of the website https://the-internet.herokuapp.com using Selenium WebDriver in Python.

## Tests included

- Clicking links and buttons
- Filling forms and input fields
- Uploading files
- Login tests with valid and invalid data
- Checking status code pages
- Parametrized tests for inputs

## Important

- Uses waits to find elements before actions
- Checks element visibility and clickability before interaction
- Uses ActionChains for hover and move_by_offset interactions
- Uses GitHub Actions CI workflow to automatically run tests on schedule, push, or pull request

## How to run tests

To run tests, follow these steps:

Clone the repository:
git clone https://github.com/michalbelicka/selenium_tests.git

Change into the project directory:
cd Selenium_tests

Install dependencies:
pip install -r requirements.txt

Run the tests:
pytest -v
