from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from bs4 import BeautifulSoup
from scrapingproject.items import WikipediaItem

class PagesSpider(CrawlSpider):
    """
    the Page Spider for wikipedia
    """

    name = "wikibot"
    allowed_domains = ["wikipedia.org"]

    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_environmental_and_conservation_organizations_in_the_United_States"
    ]

    rules = (
        Rule(LinkExtractor(allow=".+", restrict_css=('mw-headline'), deny=('body/@spanid =Government agencies')),
             callback='parse_wikipedia_page'),
    )

    def parse_wikipedia_page(self, response):
        print("Found a page")
        print(response.url)

        yield {'url':response.url}
