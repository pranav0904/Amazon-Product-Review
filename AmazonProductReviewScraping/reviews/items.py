# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_rating = scrapy.Field()
    review_title = scrapy.Field()
    product_review = scrapy.Field()
    
