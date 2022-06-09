<!---
LABELS

[![alex6970 - PasswordManager](https://img.shields.io/static/v1?label=alex6970&message=PasswordManager&color=blueviolet&logo=github)](https://github.com/alex6970/PasswordManager "Go to GitHub repo")
[![License](https://img.shields.io/badge/License-MIT-blueviolet)](#license)
[![GitHub commits](https://badgen.net/github/commits/alex6970/PasswordManager)]()  
[![GitHub watchers](https://img.shields.io/github/watchers/alex6970/PasswordManager.svg?style=social&label=Watchers&maxAge=2592000)]()

-->


# Webs scraper


## About the project

Simple webscraper script that retrieves all the data (brand, description, colour, ..) of the items of a category in the Zalando website. The data is cleaned, placed in a dataframe and transferred to a csv file.

<br>



## Table of Contents

- [Project Organization](#project-organization)
- [Features and uses](#features-and-uses-)
- [Technologies & packages](#technologies--packages-)
- [Credits](#credits-)

<br>



## Project Organization

    │
    ├── resources    
    │   │
    │   └── chromedriver.exe          <- Google chrome driver (downloaded)
    │    
    ├── scripts
    │   │
    │   └── webscraper.py             <- Webscraper script
    │
    ├── LICENSE                       <- MIT License
    │
    └── README.md                     <- The top-level README

<br>



## Features and uses 💻

The script allows user to connect to the website via submitted url (Zalando).
Extracts brand, colour, product name and category of each item of the current page.
Switches the page (until submitted number) and does the same operations.
Extracted data is placed inside csv file (products.csv)

<br>



## Technologies & packages 🔧

&rarr; BeautifulSoup  
&rarr; Selenium   
&rarr; Pandas   
&rarr; Python  

<br>


## Credits 🤝

- [Stack Overflow](https://stackoverflow.com/)
- [GeeksforGeeks](https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/)
- [ScrapingBee](https://www.scrapingbee.com/blog/web-scraping-101-with-python/)
- ...
