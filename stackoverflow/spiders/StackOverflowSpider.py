import scrapy

from stackoverflow.items import StackOverflowItem

base_url_pattern = 'http://stackoverflow.com/questions?sort=votes&page=%s'


class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/']

    def parse(self, response):
        for page_index in range(5):
            url = base_url_pattern % str(page_index)
            yield scrapy.Request(url, callback=StackOverflowSpider.parse_item)

    @staticmethod
    def parse_item(response):
        for href in response.xpath('//div[@class="question-summary"]/div[2]/h3/a/@href'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=StackOverflowSpider.parse_question)

    @staticmethod
    def parse_question(response):
        item = StackOverflowItem()
        item['title'] = response.xpath('//h1/a/text()').extract()[0]
        item['votes'] = response.xpath('//div[@class="question"]/div[2]/div[1]/div[1]/div[1]/text()').extract()[0]
        item['body'] = response.xpath('//div[@class="question"]/div[2]/div[2]/div[1]').xpath('string(.)').extract()[0]
        item['tags'] = response.xpath('//div[@class="question"]/div[2]/div[2]/div[2]/div[1]//a/text()').extract()
        item['link'] = response.url
        yield item
