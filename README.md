# Selenium Test Project

## Overview

This is a demo project for learning and practicing Selenium test automation.

The project tests different functionalities of the website [The Internet](https://the-internet.herokuapp.com) using Selenium WebDriver with Python and pytest.

The tests are structured using the Page Object Model (POM) design pattern to separate test logic from page-specific actions and improve maintainability.

## Technologies

- Python
- Selenium WebDriver
- pytest
- pytest-html
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
- Uses pytest hooks to automatically capture screenshots when Selenium tests fail
- Generates HTML test reports using pytest-html
- Uses GitHub Actions CI workflow to automatically run tests on push, pull request and scheduled runs
- Configures Chrome policies in CI to prevent password leak warnings from blocking automated tests

## Test Reports and Screenshots

HTML test reports are generated using pytest-html.

The report is created in:

```text
reports/report.html
```

When a Selenium test fails, an automatic screenshot is saved in:

```text
reports/screenshots/
```

Screenshots help with debugging failed tests by capturing the browser state at the moment of failure.

## Future Improvements

- Add more test scenarios and edge cases
- Add support for additional browsers
- Improve test organization and maintainability

## How to run tests

1. Clone the repository:  
   `git clone https://github.com/michalbelicka/selenium_tests.git`

2. Change into the project directory:  
   `cd Selenium_tests`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Run the tests:  
   `pytest --html=reports/report.html --self-contained-html`
