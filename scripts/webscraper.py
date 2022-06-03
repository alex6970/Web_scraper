import os
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import re
import time

df = pd.DataFrame(columns=['Brand', 'Model', 'Description', 'Color', 'Price'])


DRIVER_PATH = './resources/chromedriver.exe'
browser = webdriver.Chrome(executable_path=DRIVER_PATH)

url = 'https://www.zalando.fr/t-shirts-polos-homme/' # Can change the url
browser.get(url)
# time.sleep(60)
soup = BeautifulSoup(browser.page_source, 'html.parser')



# get the nb of pages of the url's category
pages = soup.select('nav.VKvyEj._0xLoFW._7ckuOK.mROyo1.uEg2FS span.RYghuO._7Cm1F9.ka2E9k.uMhVZi.FxZV-M.pVrzNP.JCuRr_._0xLoFW.uEg2FS.FCIprz')
nb_pages_text = pages[0].get_text(strip=True).split(' ')
nb_pages = int(nb_pages_text[3])

brands_list = []
model_list = []
descript_list = []
color_list = []
price_list = []


page = 1

while page != 10: # Chosen number of pages to  scrap for the category (n+1)
    url = f'https://www.zalando.fr/t-shirts-polos-homme/?p={page}' # Can change the url
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    ## Scraping part
    product = soup.find_all('div', attrs={'class':'DT5BTM w8MdNG cYylcv QylWsg _75qWlu iOzucJ JT3_zV DvypSJ'}) # finds each html box containing a product

    for item in product:
        brand = item.find('span', attrs={'class':'SZKKsK u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})

        if brand is not None : # in case the article is not a product (can be an ad)
            description = item.find('h3', attrs={'class':'RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2'})
            price = item.select('header div._0xLoFW._78xIQ- span.RYghuO.u-6V88.ka2E9k.uMhVZi')

            # Cleaning price
            if 'à partir de' in price[0].get_text(strip=True) :
                price_list.append(float(price[0].get_text(strip=True).replace('à partir de', '').replace(',', '.').replace('€', '').encode('ascii', 'ignore'))) # removes js spaces inside price

            else :
                price_list.append(float(price[0].get_text(strip=True).replace(',', '.').replace('€', '').encode('ascii', 'ignore')))

            # Cleaning description (spliting)
            desc_words = description.get_text(strip=True).split(' - ')

            if len(desc_words) == 3:
                model_list.append(desc_words[0])
                descript_list.append(desc_words[1])
                color_list.append(desc_words[2])

            elif len(desc_words) == 2 :
                model_list.append("None")
                descript_list.append(desc_words[0])
                color_list.append(desc_words[1])

            # Brand
            brands_list.append(brand.get_text(strip=True))

    page = page + 1


df['Brand'] = brands_list
df['Model'] = model_list
df['Description'] = descript_list
df['Color'] = color_list
df['Price'] = price_list
#
#
print(df.iloc[235:550])
print(len(df), "items have been scraped from this category.")
print(df.shape)

df.to_csv('products.csv', index=False, encoding='utf-8')
