
from scarper import ApartmentLinkScraper, ApartmentDataScraper


link_scraper = ApartmentLinkScraper(product="appartement")
links = link_scraper.scrape_links()
link_scraper.save_links_to_file("href.txt")


data_scraper = ApartmentDataScraper("href.txt")
appartements_data = data_scraper.scrape_data()
data_scraper.save_data_to_csv("appartements_data.csv")
