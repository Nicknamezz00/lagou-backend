import scrapy


class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['http://lagou.com/']

    def parse(self, response):
        pass
