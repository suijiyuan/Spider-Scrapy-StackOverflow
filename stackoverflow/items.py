import scrapy


class StackOverflowItem(scrapy.Item):
    title = scrapy.Field()
    votes = scrapy.Field()
    body = scrapy.Field()
    tags = scrapy.Field()
    link = scrapy.Field()

    # def __str__(self):
    #     pass
