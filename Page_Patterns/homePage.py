
from selenium.webdriver.common.keys import Keys


class HomePage():

    def __init__(self, driver):
        self.driver = driver
        # home page locators defining
        self.ticket_to_one_way = "span[id='lbl-flight-search-type-one-way']"
        self.departure_id = "input[placeholder='Departure airport']"
        self.destination_id = "input[placeholder='Destination airport']"

    def ticket_to_one_way(self):
        self.driver.find_element_by_css_selector(self.departure_id).click()

    def departure(self):
        self.driver.find_element_by_css_selector(self.departure_id).sendKeys("kosiv")
        self.driver.find_element_by_css_selector(self.departure_id).sendKeys(Keys.ENTER)

    def destination(self):
        self.driver.find_element_by_css_selector(self.destination_id).click()


