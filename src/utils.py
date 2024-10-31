from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from fake_useragent import UserAgent
import random

class WebScraperUtils:
    def __init__(self):
        self.driver = self._create_driver_with_proxy()

    def _create_driver_with_proxy(self):
        # Liste de proxies
        # proxies = [
                  
        #           "143.198.242.86:8080"
    
    
        #         ]
        # Sélectionner un proxy et un User-Agent aléatoires
        # proxy = random.choice(proxies)
        # user_agent = UserAgent().random

        # Configurer les options du navigateur
        # options = webdriver.ChromeOptions()
        # options.add_argument(f'--proxy-server={proxy}')
        # options.add_argument(f'user-agent={user_agent}')
        
        # Initialiser le driver avec les options
        return webdriver.Chrome()

    def get_text_or_nan(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            return "NaN"

    def close_driver(self):
        self.driver.quit()
