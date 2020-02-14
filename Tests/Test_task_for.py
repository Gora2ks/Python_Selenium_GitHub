from selenium import webdriver
import unittest
from Page_Patterns.loginPage import LoginPage


class Login(unittest.TestCase):

    def test_LoginPage(self):
        driver = webdriver.Chrome()
        driver.get("D:\Develop\Python_source\Python_Selenium_GitHub\Sources\index2 (2) (1) (2) (1).html")

        lp = LoginPage(driver)
        lp.login("Gora", "Wroclaw")
