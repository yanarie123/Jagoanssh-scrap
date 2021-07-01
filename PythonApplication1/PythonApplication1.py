import cloudscraper
from bs4 import BeautifulSoup
scraper = cloudscraper.CloudScraper()
hasil = scraper.get("http://panel.jagoanssh.com/login")
print(hasil.headers)
#soup=BeautifulSoup(hasil.text, 'html.parser')
#hasil = soup.find_all('input', {'class': "_token"})
#h=hasil[0]['value']