from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
   
    MAKE_APPOINTMENT_BUTTON = (By.XPATH, "//a[@id='btn-make-appointment']")
    MENU_DROPDOWN = (By.ID, "menu-toggle")
    HEADING = (By.XPATH, "//h1[text()='CURA Healthcare Service']")
    SUB_HEADING = (By.XPATH, "//h3[text()='We Care About Your Health']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_appointment(self):
        self.click(self.MAKE_APPOINTMENT_BUTTON)

    def get_make_appointment_button_text(self):
        return self.driver.find_element(*self.MAKE_APPOINTMENT_BUTTON).text

    def validate_main_heading(self):
        return self.validate_text(self.HEADING, "CURA Healthcare Service")

    def validate_sub_heading(self):
        return self.validate_text(self.SUB_HEADING, "We Care About Your Health")

    def is_menu_dropdown_visible(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MENU_DROPDOWN)
        )
        return element.is_displayed()

    def click_menu_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_DROPDOWN)
        )
        element.click()

    def click_home_option(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.HOME_OPTION)
        )
        element.click()