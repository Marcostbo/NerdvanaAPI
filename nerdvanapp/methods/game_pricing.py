import urllib.parse as parse
import requests
from nerdvanapp.models.user import User
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from notification.methods import SendNotification

# import asyncio
# import aiohttp
# import async_timeout


class GamePricing:
    def __init__(self):
        self.google = 'https://www.google.com.br'
        self.search = 'https://www.google.com.br/search?q='
        self.class_name = 'T4OwTb'
        # self.end = '" data-agdh="arwt" id="vplap0"'
        self.end = '"'

    # def get_smaller_price_and_url_for_multiple_stores_async(self, game: str, console: str, stores_list: list):
    #
    #     async def fetch(session, url):
    #         with async_timeout.timeout(10):
    #             async with session.get(url) as response:
    #                 return await response.text()
    #
    #     async def main(urls):
    #         async with aiohttp.ClientSession() as session:
    #             tasks = [fetch(session, url) for url in urls]
    #             results = await asyncio.gather(*tasks)
    #             return results
    #
    #     search_urls = []
    #     for store in stores_list:
    #         store_name = store[0]
    #
    #         query = f'{game} {console} {store_name} jogo midia fisica'
    #         search_url = self.search + parse.quote_plus(query)
    #         search_urls.append(search_url)
    #
    #     details_async = asyncio.run(main(search_urls))
    #
    #     store_prices = []
    #     store_result = {}
    #     for html in details_async:
    #         try:
    #             smaller_price = self.treate_price_string_v2(self.find_between(str(html), "R$", "</"))
    #             full_link = self.find_between(str(html), 'href="/url?q=', "&")
    #             store_result = {
    #                 'store_name': 'teste',
    #                 'price': smaller_price,
    #                 'url': full_link
    #             }
    #         except Exception as e:
    #             smaller_price = None
    #             full_link = None
    #         store_prices.append(store_result)
    #     return None

    def get_smaller_price_and_url_for_multiple_stores_v2(self, game: str, console: str, stores_list: list):
        store_prices = []
        for store in stores_list:
            store_name = store[0]

            query = f'{game} {console} {store_name} mais barato'
            search_url = self.search + parse.quote_plus(query)

            result = requests.get(search_url)
            html = result.content
            try:
                smaller_price = self.treate_price_string_v2(self.find_between(str(html), "R$", "</"))
                full_link = self.find_between(str(html), 'href="/url?q=', "&")
                store_result = {
                    'store_name': store[2],
                    'price': smaller_price,
                    'url': full_link
                }
                store_prices.append(store_result)
            except Exception as e:
                pass
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

    @staticmethod
    def evaluate_price(price_limit: float, current_price: float):
        if current_price < price_limit:
            return True
        return False

    @staticmethod
    def send_email_price_alert_resolved(user: User, game_name: str, price: float, link: str, store: str):
        client_name = user.first_name
        text = f'Olá, {client_name} \n' \
               f'\n'\
               f'O seu alerta para o jogo {game_name} foi ativado!. \n' \
               f'\n' \
               f'Jogo: {game_name} \n' \
               f'Loja: {store} \n' \
               f'Preço: {price} \n' \
               f'Link: {link} \n' \
               f'\n' \
               f'Obrigado'

        SendNotification().send_email(
            to_email=user.email,
            subject=f'Encontramos um resultado para seu alerta de preço pra o jogo {game_name}',
            message=text,
            user=user,
            reason="Game Price Alert"
        )
