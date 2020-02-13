from selenium.webdriver.common.by import By

from Locators.locators import Locators
from Base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    # Login page objects
    # Positive scenario
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Write_First_Name(self, firstName):
        firstField = self.driver.find_element(By.ID, Locators.lastname_textbox_id)
        firstField.click()
        firstField.is_enabled()
        firstField.clear()
        firstField.send_keys(firstName)

    def Write_Last_Name(self, lastName):
        lastField = self.driver.find_element(By.ID, Locators.lastname_textbox_id)
        lastField.click()
        lastField.is_enabled()
        lastField.clear()
        lastField.send_keys(lastName)

    def Submit_button(self):
        submit = self.driver.find_element(By.ID, Locators.submit_button_id)
        submit.click()

    #
    # def enter_Last_Name(self, username):
    #     ##      self.driver.find_element_by_xpath_selector(self.username_texbox_id).clear()
    #     try:
    #         self.driver.find_element_by_css_selector(self.username_texbox_id).send_keys(username)
    #     except:
    #         return None

    # # def wait_for_login_page(self):
    # #     wait = WebDriverWait(self.driver, 30)
    # # wait.until(EC.title_is("Facebook – log in or sign up"))
