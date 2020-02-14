from selenium.webdriver.common.by import By
from Base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):
    # Login page objects
    # Positive scenario
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _firstNameBox = "firstname-input"
    _lastnameBox = "lastname-input"
    _username_textbox = ""
    _password_textbox = ""
    _submitButton = "submit-button"

    def Write_First_Name(self, firstName):
        self.sendKeys(firstName, self._firstNameBox)
        # return self.driver.find_element(By.ID, self._firstNameBox)

    def Write_Last_Name(self, lastName):
        self.sendKeys(lastName,self._lastnameBox)
        # return self.driver.find_element(By.ID, self._lastnameBox)

    def Submit_button(self):
        self.elementClick(self._submitButton, locatorType="id")
        # return self.driver.find_element(By.ID, self._submitButton)

    def login(self, firstName, lastName):
        self.Write_First_Name(firstName)
        self.Write_Last_Name(lastName)
        self.Submit_button()

