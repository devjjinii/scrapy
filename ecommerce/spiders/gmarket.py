import scrapy


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['www.gmarket.co.kr']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/','http://www.gmarket.co.kr/']

    def parse(self, response):
        # pass
        print(response.url)
