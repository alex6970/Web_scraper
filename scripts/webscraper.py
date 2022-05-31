import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

df = pd.DataFrame(columns=['Brand', 'Description', 'Price'])


DRIVER_PATH = './resources/chromedriver.exe'
browser = webdriver.Chrome(executable_path=DRIVER_PATH)

url = 'https://www.zalando.fr/t-shirts-tops-femme/'
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

# seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")

brands = soup.find_all('span', {'class': 'SZKKsK u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})
description = soup.find_all('h3', {'class': 'RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})
price = soup.find_all('span', {'class': 'RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP'})


brands_list = []
description_list = []
price_list = []

# get the texs inside the tags contained in the results (from div)
for item in brands:
    brands_list.append(item.text.strip())

for item in description:
    description_list.append(item.text.strip())

for item in price:
    price_list.append(item.text.strip())


df['Brand'] = brands_list
df['Description'] = description_list
df['Price'] = price_list

print(df.head())
