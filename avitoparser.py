from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
from time import sleep
import itertools


class AvitoParser():

    def __init__(self, base_url, search_word, filter='date'):
        self.base_url = base_url
        self.search_word = search_word
        if filter == 'lowcost':
            self.filter = '1'
        elif filter == 'highcost':
            self.filter = '2'
        elif filter == 'date':
            self.filter = '0'
        else:
            self.filter = '0'

    def __grab_page(self, page_num):
        url_filter = '&i=1&s=' + self.filter
        url_search = '&q=' + quote(search_word)
        url_page_num = '&p=' + str(page_num)
        result_url = ''.join([base_url + '?', url_filter, url_search, url_page_num])
        page = BeautifulSoup(urlopen(result_url), "html.parser")
        return page

    def __links(self, page):
        item_links = []
        for item_link in page.findAll('a', {'class': 'item-description-title-link'}):
            item_links.append('https://www.avito.ru' + item_link.get('href'))
        return item_links

    def __images(self, page):
        item_images = []
        for item_image in page.findAll('img', {'class': 'photo-count-show'}):
            item_images.append(item_image.get('src').replace('//', 'https://'))
        return item_images

    def __descriptions(self, page):
        items_desc = []
        for item_desc in page.findAll('a', {'class': 'item-description-title-link'}):
            items_desc.append(item_desc.getText().replace('\n ', ''))
        return items_desc

    def __prices(self, page):
        prices = []
        for price_div in page.findAll('div', {'class': 'about'}):
            # bad way (because last 'div' has class='about c-2')
            if 'Avito' in price_div.getText():
                pass
            else:
                # append to the price-list only numbers;
                # if there is an empty price, let`s add it too
                price = re.sub('[^0-9]', '', price_div.getText())
                prices.append(price)
        return prices

    def __ads_per_page(self, page):
        links = self.__links(page)
        descriptions = self.__descriptions(page)
        images = self.__images(page)
        prices = self.__prices(page)
        ads = []
        for link, description, image, price in zip(links, descriptions, images, prices):
            ads.append({"link": link,
                            "description": description,
                            "image": image,
                            "price": price})
        return ads

    def dump_ads(self, timeout=10):
        page_num = 1
        ads = []
        while page_num:
            try:
                page = self.__grab_page(page_num)
                ads_per_page = self.__ads_per_page(page)
                ads.append(ads_per_page)
                page_num += 1
                sleep(timeout)
            except HTTPError:
                # there is no more ads
                break
        return list(itertools.chain.from_iterable(ads))