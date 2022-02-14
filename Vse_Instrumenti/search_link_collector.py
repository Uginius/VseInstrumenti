import time
import requests
from bs4 import BeautifulSoup
from Vse_Instrumenti.search_product import SearchProduct
from config import headers


class SearchLinkCollector:
    def __init__(self, word):
        self.search_url = 'https://www.vseinstrumenti.ru/search_main.php?what=' + word
        self.soup = None
        self.max_pag = None
        self.product_count = None
        self.card_list = []
        self.sp = None
        self.cur_page_number = 0
        self.current_page = None

    def run(self):
        self.go_pages()
        self.parse_searched_pages()

    def go_pages(self):
        self.get_page()
        self.get_max_pagination()

    def get_page(self, page_url=None):
        try:
            url = page_url if page_url else self.search_url
            r = requests.get(url=url, headers=headers)
            self.soup = BeautifulSoup(r.text, 'lxml')
        except Exception as ex:
            pass
        # with open('in1.html', 'w', encoding='utf8') as wr_file:
        #     wr_file.write(r.text)
        # with open('in1.html', 'r', encoding='utf8') as rd_file:
        #     src = rd_file.read()
        # self.soup = BeautifulSoup(src, 'lxml')

    def get_max_pagination(self):
        try:
            self.get_page()
            pagination = self.soup.find('div', class_='pagination')
            self.max_pag = int(pagination.attrs['data-max-page'])
            self.product_count = int(pagination.attrs['data-product-count'])
            self.current_page = int(pagination.attrs['data-current-page'])
        except AttributeError:
            self.max_pag = None
            self.product_count = None
            self.current_page = None

    def get_search_cards(self):
        cards = self.soup.find_all('div', class_='product-tile grid-item')
        for pos, card in enumerate(cards):
            order = pos + 1 + self.cur_page_number * 20
            self.sp = SearchProduct(order)
            self.sp.card_soup = card
            self.sp.parse_data()
            self.sp.data_out()

    def parse_searched_pages(self):
        self.get_search_cards()
        if self.max_pag > 1:
            for cur_page_number in range(2, self.max_pag + 1):
                self.cur_page_number = cur_page_number - 1
                self.get_search_cards()
                time.sleep(3)
