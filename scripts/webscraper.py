import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

df = pd.DataFrame(columns=['Brand', 'Description', 'Price'])


DRIVER_PATH = './resources/chromedriver.exe'
browser = webdriver.Chrome(executable_path=DRIVER_PATH)

url = 'https://www.zalando.fr/t-shirts-tops-femme/'
browser.get(url)
# time.sleep(60)

soup = BeautifulSoup(browser.page_source, 'html.parser')

# seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")

brands_list = []
description_list = []
price_list = []

sum = 0

product = soup.find_all('div', attrs={'class':'DT5BTM w8MdNG cYylcv QylWsg _75qWlu iOzucJ JT3_zV DvypSJ'}) # finds each html box containing a product

for item in product:
    brand = item.find('span', attrs={'class':'SZKKsK u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})

    if brand is not None : # in case the article is not a product (can be an ad)


        description = item.find('h3', attrs={'class':'RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})
        price = item.select('header div._0xLoFW._78xIQ- span.RYghuO.u-6V88.ka2E9k.uMhVZi')

        brands_list.append(brand.get_text(strip=True))
        description_list.append(description.get_text(strip=True))
        price_list.append(price[0].get_text(strip=True))


df['Brand'] = brands_list
df['Description'] = description_list
df['Price'] = price_list

print(df.head())

    # brand = item.select("")
    # print(brand.get_text(strip=True))
    # brands_list.append(brand)
    # description = item.find('h3', attrs={'class':'RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})
    # price = item.find('span', attrs={'class':'RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP'})

# print(type(product[5].find('span', attrs={'class':'SZKKsK u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})))
# # df['Brand'] = brands_list
# # print(df.head())
#
# # print(brand.prettify())



# for item in product:
#     print(item.get_text(strip=True))


# brand = product.find_all('span', {'class': 'SZKKsK u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})
# description = product.find_all('h3', {'RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})
# price = product.find_all('span', {'class': 'RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP'})

#
# brands_list = []
# description_list = []
# price_list = []
#
# # get the texs inside the tags contained in the results (from div)
# for item in brand:
#     brands_list.append(item.text.strip())
#
# for item in description:
#     description_list.append(item.text.strip())
#
# for item in price:
#     price_list.append(item.text.strip())
#
#
# df['Brand'] = brands_list
# df['Description'] = description_list
# df['Price'] = price_list
#
# print(df.head())
