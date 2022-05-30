import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


DRIVER_PATH = './resources/chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')
