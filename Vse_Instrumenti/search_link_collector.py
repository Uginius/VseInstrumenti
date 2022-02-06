import time
import requests
from bs4 import BeautifulSoup
from Vse_Instrumenti.search_product import SearchProduct
from config import headers


class SearchLinkCollector:
    def __init__(self, word):
        self.search_url = 'https://www.vseinstrumenti.ru/search_main.php?what=' + word
        self.soup = None
        self.max_pag = 1
        self.card_list = []
        self.sp = None

    def get_page(self):
        # r = requests.get(url=self.search_url, headers=headers)
        # self.soup = BeautifulSoup(r.text, 'lxml')
        # with open('in1.html', 'w', encoding='utf8') as wr_file:
        #     wr_file.write(r.text)
        with open('in1.html', 'r', encoding='utf8') as rd_file:
            src = rd_file.read()
        self.soup = BeautifulSoup(src, 'lxml')

    def get_max_pagination(self):
        self.get_page()
        self.max_pag = self.soup.find('div', class_='pagination').attrs['data-max-page']

    def get_search_cards(self):
        cards = self.soup.find_all('div', class_='product-tile grid-item')
        for pos, card in enumerate(cards):
            order = pos + 1
            self.sp = SearchProduct(order)
            self.sp.card_soup = card
            self.sp.parse_data()
            self.sp.data_out()

    def parse_searched_pages(self):
        self.get_search_cards()
        time.sleep(3)

    def run(self):
        self.get_max_pagination()
        self.parse_searched_pages()
