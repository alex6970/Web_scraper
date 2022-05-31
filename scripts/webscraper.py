import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


DRIVER_PATH = './resources/chromedriver.exe'
browser = webdriver.Chrome(executable_path=DRIVER_PATH)

url = 'https://www.zalando.fr/t-shirts-tops-femme/'
browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')
# browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div/div[7]/div/div[2]/div[2]/div[2]/div[1]/div/article/a').click()

# results = soup.find_all('span', {'class': 'hPWzFB'})
results = soup.find_all('div', {'class': '_0xLoFW _78xIQ- EJ4MLB f4ql6o JT3_zV'})

# <div class="_0xLoFW _78xIQ- EJ4MLB f4ql6o JT3_zV" tabindex="-1"><a tabindex="-1" class="JT3_zV CKDt_l ONArL- _2dqvZS CKDt_l LyRfpJ" href="https://www.zalando.fr/bershka-mit-patentmuster-debardeur-stone-bej21d12t-a11.html" aria-hidden="true" rel=""><header><div class="hPWzFB"><span class="SZKKsK u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2">Bershka</span><h3 class="RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP ZkIJC- r9BRio qXofat EKabf7 nBq1-s _2MyPg2">SLEEVELESS - Débardeur - stone</h3></div><div class="_0xLoFW _78xIQ-"><span class="RYghuO u-6V88 ka2E9k uMhVZi FxZV-M pVrzNP">7,99&nbsp;€</span></div></header></a></div>

# get the texs inside the tags contained in the results (from div)
for item in results:
    print(item.text.strip())
