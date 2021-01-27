import scrapy
from bs4 import BeautifulSoup
import urllib

class OurfirstbotSpider(scrapy.Spider):
    name = 'ourfirstbot'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_common_misconceptions']

    def parse(self, response):
        headings = response.css('.mw-headline').extract()
        datas = response.css('ul').extract() 
        for item in datas:
            all_items = {
                'datas' : BeautifulSoup(item).text,
            }
            yield all_items