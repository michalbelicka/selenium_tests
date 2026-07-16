# Selenium Test Project

## Overview

This is a demo project for learning and practicing Selenium test automation.

The project tests different functionalities of the website [The Internet](https://the-internet.herokuapp.com) using Selenium WebDriver with Python and pytest.

The tests are structured using the Page Object Model (POM) design pattern to separate test logic from page-specific actions and improve maintainability.

## Technologies

- Python
- Selenium WebDriver
- pytest
- GitHub Actions (CI)
- Page Object Model (POM)

## Tests included

- Clicking links and buttons
- Filling forms and input fields
- Uploading files
- Login tests with valid and invalid credentials
- Checking status code pages
- Parametrized tests for different input values
- Handling multiple browser windows
- Hover interactions using ActionChains
- Dynamic content testing

## Important

- Uses explicit waits with appropriate expected conditions depending on the element state
- Checks element visibility and clickability before interaction
- Uses Page Object Model to keep tests clean and reusable
- Uses ActionChains for advanced interactions such as hover and mouse movements
- Uses GitHub Actions CI workflow to automatically run tests on push, pull request and scheduled runs
- Configures Chrome policies in CI to prevent password leak warnings from blocking automated tests

## Future Improvements

- Add automated test reports
- Capture screenshots automatically when tests fail
- Add more test scenarios and edge cases

## How to run tests

1. Clone the repository:  
   `git clone https://github.com/michalbelicka/selenium_tests.git`

2. Change into the project directory:  
   `cd Selenium_tests`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Run the tests:  
   `pytest -v`
