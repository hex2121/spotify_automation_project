
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from conftest import *

class CommonFunctions:

    def click(self, element):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element)))
        driver.find_element(by=By.CSS_SELECTOR, value=element).click()

    def fill_fields(self, field, value):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, field)))
        driver.find_element(by=By.CSS_SELECTOR, value=field).send_keys(value)

    def wait_for_element(self, element):
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, element)))

