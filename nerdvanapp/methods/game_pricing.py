# Step 1: Define stores
# 1.1 - Americanas
# 1.2 - Submarino
# 1.3 - Ponto Frio (search as pontofrio)
# 1.4 - Kabum
# 1.5 - Casas Bahia
# 1.6 - Magalu
# Step 2: Search for game in Google via Webscraping
# 2.1: Selenium?
# Step 3: Get game price

import urllib.parse as parse
from selenium import webdriver
from selenium.webdriver.common.by import By

query = 'God of War PS4 Magalu'
query = parse.quote_plus(query)

google = 'https://www.google.com.br'
url = 'https://www.google.com.br/search?q='
search_url = url + query

print(search_url)

CLASS_NAME = 'T4OwTb'

driver = webdriver.Chrome(executable_path=r'C:\Users\Marcos Oliveira\PycharmProjects\NerdvanaAPI\chromedriver.exe')
driver.get(search_url)

results = driver.find_elements(By.CLASS_NAME, CLASS_NAME)
