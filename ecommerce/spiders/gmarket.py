import scrapy
from ecommerce.items import EcommerceItem

class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['www.gmarket.co.kr']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers']

    def parse(self, response):
        # pass
        titles = response.css('div.best-list li > a::text').getall()
        prices = response.css('div.best-list li > div.item_price > div.s-price > strong > span > span::text').getall()

        for num,title in enumerate(titles):
            item = EcommerceItem()
            item['title'] = title
            item['price'] = prices[num].strip().replace("원","").replace(",","")
            yield item


# In contrast to "return", 
# "yield" doesn't exit the function and continues with the your for-loop. 
# If you use "return", your for-loop will finish after the first iteration.