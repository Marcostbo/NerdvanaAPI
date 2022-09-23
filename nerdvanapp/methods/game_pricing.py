import urllib.parse as parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class GamePricing:
    def __init__(self, store_name, store_url, game, console, stores_list=None):
        self.google = 'https://www.google.com.br'
        self.search = 'https://www.google.com.br/search?q='
        self.class_name = 'T4OwTb'
        self.start = f'href="{store_url}'
        self.end = '" data-agdh="arwt" id="vplap0"'

        query = game + ' ' + console + ' ' + store_name
        self.stores_list = stores_list
        self.store_url = store_url
        self.query = parse.quote_plus(query)
        self.search_url = self.search + self.query

        self.smaller_price = None
        self.full_link = None

    def get_smaller_price_and_url(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-proxy-server')
        options.add_argument("--proxy-server='direct://'")
        options.add_argument("--proxy-bypass-list=*")
        driver = webdriver.Chrome(
            executable_path=r'C:\Users\Marcos Oliveira\PycharmProjects\NerdvanaAPI\chromedriver.exe',
            options=options
        )
        driver.get(self.search_url)

        results = driver.find_elements(By.CLASS_NAME, self.class_name)
        smaller_price = results[0].text
        self.smaller_price = self.treate_price_string(smaller_price=smaller_price)

        page_source = results[0].parent.page_source
        link = self.find_between(page_source, self.start, self.end)
        self.full_link = self.store_url + link

    def get_smaller_price_and_url_for_multiple_stores(self):
        driver = webdriver.Chrome(
            executable_path=r'C:\Users\Marcos Oliveira\PycharmProjects\NerdvanaAPI\chromedriver.exe'
        )
        # tomorrow: call the driver for each store

    @staticmethod
    def find_between(s, first, last):
        try:
            link_start = s.index(first) + len(first)
            link_end = s.index(last, link_start)
            return s[link_start:link_end]
        except ValueError:
            return ""

    @staticmethod
    def treate_price_string(smaller_price):
        price = smaller_price
        price = price.replace(',', '.')
        price = price.replace('R$ ', '')

        return float(price)


game_price = GamePricing(
    store_name="Americanas",
    store_url="https://www.americanas.com.br",
    game="Elden Ring",
    console="PS4"
)

import time
start = time.time()
game_price.get_smaller_price_and_url()
end = time.time()
print(f'-- Total time {end - start}')
print(game_price.smaller_price)
print(game_price.full_link)
