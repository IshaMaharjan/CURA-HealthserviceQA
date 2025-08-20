import pytest
from pages.homepage import HomePage
from pages.base_page import BasePage


def test_homepage_headings(init_driver):
    homepage = HomePage(init_driver)
    assert homepage.validate_main_heading(), "Heading does not match"
    assert homepage.validate_sub_heading(), "Sub-heading does not match"

def test_button_texts(init_driver):
    homepage = HomePage(init_driver)
    actual_text = homepage.get_make_appointment_button_text()
    expected_text = "Make Appointment"
    assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"

def test_menu_button(init_driver):
        homepage = HomePage(init_driver)
        assert homepage.is_menu_dropdown_visible(), "Menu button is not visible"
        homepage.click_menu_dropdown()

def test_menu_option_home_is_working(init_driver):
    homepage = HomePage(init_driver)
    assert homepage.is_menu_dropdown_visible(), "Menu button is not visible"
    homepage.click_menu_dropdown()
    homepage.click_home_option()


