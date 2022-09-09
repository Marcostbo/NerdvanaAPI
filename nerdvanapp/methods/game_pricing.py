# Step 1: Define stores
# 1.1 - Americanas
# 1.2 - Submarino
# 1.3 - Ponto Frio (search as pontofrio)
# 1.4 - Kabum
# 1.5 - Casas Bahia
# 1.6 - Magalu
# 1.7 - Shoptime
# Step 2: Search for game in Google via Webscraping
# 2.1: Selenium?
# Step 3: Get game price

import urllib.parse as parse
from selenium import webdriver
from selenium.webdriver.common.by import By

# store = "https://www.magazineluiza.com.br"
# store = "https://www.americanas.com.br"
# store = "https://www.shoptime.com.br"
store = "https://www.kabum.com.br"
# query = 'Elden Ring PS4 Magalu'
# query = 'Elden Ring PS4 Americanas'
# query = 'Elden Ring XBOX ONE Shoptime'
query = 'Elden Ring PS4 Kabum'
query = parse.quote_plus(query)

google = 'https://www.google.com.br'
url = 'https://www.google.com.br/search?q='
search_url = url + query

print(search_url)

CLASS_NAME = 'T4OwTb'

driver = webdriver.Chrome(executable_path=r'C:\Users\Marcos Oliveira\PycharmProjects\NerdvanaAPI\chromedriver.exe')
driver.get(search_url)

results = driver.find_elements(By.CLASS_NAME, CLASS_NAME)
smaller_price = results[0].text

page_source = results[0].parent.page_source

start = f'href="{store}'
end = '" data-agdh="arwt" id="vplap0"'


def find_between(s, first, last):
    try:
        link_start = s.index(first) + len(first)
        link_end = s.index(last, link_start)
        return s[link_start:link_end]
    except ValueError:
        return ""


link = find_between(page_source, start, end)
full_link = store + link
print(smaller_price)
print(full_link)
