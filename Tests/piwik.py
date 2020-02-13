import selenium
from selenium import webdriver
from Locators.locators import Locators
import pytest


def piwik_test():
    driver = webdriver.Chrome()
    driver.get(Locators.url_source)
    driver.find_element_by_id(Locators.username_textbox_id).click()
    driver.find_element_by_id(Locators.username_textbox_id).is_displayed()
    driver.find_element_by_id(Locators.username_textbox_id).is_enabled()
    driver.find_element_by_id(Locators.username_textbox_id).clear()
    driver.find_element_by_id(Locators.username_textbox_id).send_keys("Gora")
    driver.find_element_by_id(Locators.password_textbox_id).screenshot(self, "firstname-input")


piwik_test()
