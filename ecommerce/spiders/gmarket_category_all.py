import scrapy


class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'
    # allowed_domains = ['http://corners.gmarket.co.kr/Bestsellers']
    # start_urls = ['http://http://corners.gmarket.co.kr/Bestsellers/']
    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse)
        # yield scrapy.Request(url="", callback=self.parse_sub)

    def parse(self, response):
        print('parse')  
        category_links = response.css('div.gbest-cate ul.by-group li > a::attr(href)').getall()
        category_names = response.css('div.gbest-cate ul.by-group li > a::text').getall()
        for index, category_link in enumerate(category_links):
            # print(category_link, category_names[index])
            print('http://corners.gmarket.co.kr' + category_link, category_names[index])

    # def parse_sub(self, response):
    #     pass
