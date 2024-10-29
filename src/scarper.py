import time
import pandas as pd
from utils import WebScraperUtils
from selenium.webdriver.common.by import By


class ApartmentLinkScraper:
    def __init__(self, product, num_pages=9):
        self.product = product
        self.num_pages = num_pages
        self.links = []
        self.utils = WebScraperUtils()

    def scrape_links(self):
        """Scrape apartment links across multiple pages."""
        base_url = f"https://www.avito.ma/fr/maroc/{self.product}"

        for page in range(1, self.num_pages + 1):
            url = base_url if page == 1 else f"{base_url}?o={page}"
            self.utils.driver.get(url)
            time.sleep(2)

            apartment_elements = self.utils.driver.find_elements(By.XPATH, "//a[@class='sc-1jge648-0 eTbzNs']")
            for element in apartment_elements:
                link = element.get_attribute('href')
                if link:
                    self.links.append(link)

        self.utils.close_driver()
        return self.links

    def save_links_to_file(self, path):
        """Save scraped links to a file."""
        with open(path, 'w', encoding='utf-8') as file:
            for link in self.links:
                file.write(link + '\n')
        print('Links saved to file.')


class ApartmentDataScraper:
    def __init__(self, links_path):
        self.links_path = links_path
        self.utils = WebScraperUtils()
        self.appartements_data = []

    def scrape_data(self):
        """Scrape data from each apartment link and store in a list of dictionaries."""
        with open(self.links_path, 'r') as f:
            links = f.readlines()

        for link in links:
            self.utils.driver.get(link.strip())
            time.sleep(2)
            data = {
                "title": self.utils.get_text_or_nan("//div[@class='sc-1g3sn3w-9 kvOteU']"),
                "price": self.utils.get_text_or_nan("//p[@class='sc-1x0vz2r-0 lnEFFR sc-1g3sn3w-13 czygWQ']"),
                "location": self.utils.get_text_or_nan("//span[@class='sc-1x0vz2r-0 iotEHk']"),
                "type_de_vente": self.utils.get_text_or_nan("//li[@class='sc-qmn92k-1 jJjeGO']/span[@class='sc-1x0vz2r-0 gSLYtF' and contains(text(),'Appartements, à vendre')]"),
                "salon": self.utils.get_text_or_nan("//li[.//span[text()='Salons']]/span[@class='sc-1x0vz2r-0 gSLYtF']"),
                "chamber":self.utils.get_text_or_nan("//*[@id='__next']/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div/span"),
                "toilete":self.utils.get_text_or_nan("//*[@id='__next']/div/main/div/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div/span"),
                "area": self.utils.get_text_or_nan("//li[.//span[text()='Surface habitable']]/span[@class='sc-1x0vz2r-0 gSLYtF']"),
                "link": link.strip()
            }
            self.appartements_data.append(data)
        self.utils.close_driver()
        return self.appartements_data

    def save_data_to_csv(self, path):
        """Save scraped apartment data to a CSV file."""
        df = pd.DataFrame(self.appartements_data)
        df.to_csv(path, index=False)
        print('Data saved to CSV.')
