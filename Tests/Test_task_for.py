import unittest.mock
from selenium import webdriver
import pytest
import unittest
from Page_Patterns.loginPage import LoginPage
from Locators.locators import Locators


class Login(unittest.TestCase):

    def test_Registration_form(self):
        driver = webdriver.Chrome()
        driver.get(Locators.url_source)
        lg = LoginPage(driver)
        lg.Write_First_Name("Gora")
        lg.Write_Last_Name("Wroclaw")
        lg.Submit_button()
        # self.driver.quit()s
