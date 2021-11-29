import scrapy
from scrapy import Request
import scraper_helper as sh
from scrapy.selector import Selector


review_url = 'https://www.amazon.com/product-reviews/{}'
asin_list = ['B08CVSL4K5'] #Roborock


class ProductreviewsSpider(scrapy.Spider):
    name = 'productReviews'
    
    def start_requests(self):
        for asin in asin_list:
            url = review_url.format(asin)
            yield scrapy.Request(url)

    def parse(self, response):
        for review in response.css('[data-hook = "review"]'):
            item = {
                'Rating': review.css('[data-hook = "review-star-rating"] ::text').get(),
                'Review_title': review.css('[data-hook = "review-title"] span ::text').get(),
                'Product_review': review.xpath('normalize-space(.//*[@data-hook="review-body"]/span/text())').get(),
            }
            yield item
            
        next_page = review.xpath('//a[text() = "Next page"]/@href').get()    
        if next_page:
            yield scrapy.Request(response.urljoin(next_page))
