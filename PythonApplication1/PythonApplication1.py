import cloudscraper
from bs4 import BeautifulSoup
scraper = cloudscraper.CloudScraper()
print(scraper.get("http://panel.jagoanssh.com/login").text)