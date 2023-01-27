import urllib.parse as parse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class GamePricing:
    def __init__(self):
        self.google = 'https://www.google.com.br'
        self.search = 'https://www.google.com.br/search?q='
        self.class_name = 'T4OwTb'
        # self.end = '" data-agdh="arwt" id="vplap0"'
        self.end = '"'

    def get_smaller_price_and_url_for_multiple_stores_v2(self, game: str, console: str, stores_list: list):
        store_prices = []
        for store in stores_list:
            store_name = store[0]

            query = game + ' ' + console + ' ' + store_name
            search_url = self.search + parse.quote_plus(query)

            result = requests.get(search_url)
            html = result.content

            smaller_price = self.treate_price_string_v2(self.find_between(str(html), "R$", "</"))
            full_link = self.find_between(str(html), 'href="/url?q=', "&")

            store_result = {
                'store_name': store[2],
                'price': smaller_price,
                'url': full_link
            }
            store_prices.append(store_result)
        return store_prices

    def get_smaller_price_and_url_for_multiple_stores(self, game: str, console: str, stores_list: list):
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
        store_prices = []
        for store in stores_list:
            store_name = store[0]
            store_url = store[1]
            query = game + ' ' + console + ' ' + store_name
            search_url = self.search + parse.quote_plus(query)
            driver.get(search_url)

            results = driver.find_elements(By.CLASS_NAME, self.class_name)
            if results:
                smaller_price = results[0].text
                smaller_price = self.treate_price_string(smaller_price=smaller_price)

                page_source = results[0].parent.page_source
                start = f'href="{store_url}'
                link = self.find_between(page_source, start, self.end)
                full_link = store_url + link
                store_result = {
                    'store_name': store[2],
                    'price': smaller_price,
                    'url': full_link
                }
                store_prices.append(store_result)

        return store_prices

    @staticmethod
    def find_between(s, first, last):
        try:
            link_start = s.index(first) + len(first)
            link_end = s.index(last, link_start)
            return s[link_start:link_end]
        except ValueError:
            return ""

    @staticmethod
    def treate_price_string_v2(smaller_price):
        price = smaller_price
        price = price.replace(',', '.')
        price = price.replace('\\xa0', '')

        return float(price)

    @staticmethod
    def treate_price_string(smaller_price):
        price = smaller_price
        price = price.replace(',', '.')
        price = price.replace('R$', '')

        return float(price)
