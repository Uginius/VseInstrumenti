class SearchProduct:
    def __init__(self, order=1):
        self.card_soup = None
        self.id = None
        self.name = None
        self.url = None
        self.price = None
        self.order = order

    def parse_data(self):
        self.id = self.card_soup.find('div', class_='wtis-id').span.string.strip()
        url_a = self.card_soup.find('div', class_='title').a
        self.name = ' '.join(url_a.string.strip().split())
        self.url = 'https://www.vseinstrumenti.ru' + url_a.get('href')
        self.price = self.card_soup.attrs['data-product-price']

    def data_out(self):
        print('\norder:', self.order, '=' * 100)
        print('id:', self.id)
        print('name:', self.name)
        print('url:', self.url)
        print('price:', self.price)
        return self.order, self.id, self.name, self.url, self.price
