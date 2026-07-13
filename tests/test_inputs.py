from pages.inputs_page import InputsPage
import pytest

@pytest.mark.parametrize("inputs, expected", [
    ("123", "123"),
    ("456", "456"),
    ("abc", ""),              # invalid characters, expect empty string
    ("-789", "-789"),
    ("@!/", ""),              # special characters, expect empty string
    ("", ""),
    ("-159*589", "-159589"),  # expect that '*' is ignored or removed
])
def test_inputs(inputs, expected, driver, wait):

    page = InputsPage(driver, wait)

    page.open()

    page.go_to_inputs()

    page.enter_value(inputs)

    assert page.get_input_value() == expected

