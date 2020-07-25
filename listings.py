# Dependencies

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
from time import sleep
from time import time
from random import randint

# NoneType replacer function

def xstr(s):
    if s is None:
        return ''
    return s.text

# List that store data

id = []
price = []
address = []
size = []
rooms = []
balcony = []
built = []

# Getting number of pages

URL = 'https://ingatlan.com/lista/kiado+lakas+budapest'
page = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(page).read()
soup = BeautifulSoup(webpage, 'html.parser')
pagenumber = int(soup.find('div', class_='pagination__page-number').text.replace(' oldal','').replace('1 / ',''))
pages = [str(i) for i in range(1,pagenumber+1)]


# Extract data from website
for p in pages:
  URL = 'https://ingatlan.com/lista/kiado+lakas+budapest?page='+ p
  page = Request(URL , headers={'User-Agent': 'Mozilla/5.0'})
  sleep(randint(3,10))
  webpage = urlopen(page).read()
  soup = BeautifulSoup(webpage, 'html.parser')
  flat_containers = soup.find_all('div', class_='listing__card')
  for flats in flat_containers:
    id_elem = flats.find('a', class_='listing__thumbnail js-listing-active-area').get('href')[-8:]
    id.append(id_elem)
    price_elem = xstr((flats.find('div', class_='price')))
    price.append(price_elem)
    address_elem = xstr(flats.find('div', class_='listing__address'))
    address.append(address_elem)
    size_elem = xstr(flats.find('div', class_='listing__parameter listing__data--area-size'))
    size.append(size_elem)
    rooms_elem = xstr(flats.find('div', class_='listing__parameter listing__data--room-count'))
    rooms.append(rooms_elem)
    balcony_elem = xstr(flats.find('div', class_='listing__parameter listing__data--balcony-size'))
    balcony.append(balcony_elem)
    if None in (price_elem, address_elem, size_elem, rooms_elem, balcony_elem):
      continue
scraped_data = pd.DataFrame({'id':id,'price':price,'address':address,'size':size,'rooms':rooms,'balcony':balcony})
scraped_data
