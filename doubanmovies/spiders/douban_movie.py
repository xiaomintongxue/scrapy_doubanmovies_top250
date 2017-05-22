#coding=utf-8
'''
import sys
import importlib
importlib.reload(sys)###Python3.x使用方法，不然无法加载reload
'''
##sys.setdefaultencoding('utf-8')   Python3.x不再使用

from scrapy.spiders import Spider
from doubanmovies.items import DoubanmoviesItem
import scrapy

class DoubanTop250(Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/50.0.2661.102 Safari/537.36',
        'Referer':'https://movie.douban.com/top250',
              }

    def start_requests(self):
        url='https://movie.douban.com/top250'
        yield scrapy.Request(url, headers=self.headers)

    def parse(self, response):
        item=DoubanmoviesItem()
        movies=response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking']=movie.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['movie_name']=movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score']=movie.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['score_num']=movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            yield item

        next_url=response.xpath('//span[@class="next"]/a/@href').extract()

        if next_url:
            next_url='https://movie.douban.com/top250'+next_url[0]
            yield scrapy.Request(next_url,headers=self.headers)

