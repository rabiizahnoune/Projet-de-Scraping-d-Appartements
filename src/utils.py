from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class WebScraperUtils:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_text_or_nan(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            return "NaN"

    def close_driver(self):
        self.driver.quit()
