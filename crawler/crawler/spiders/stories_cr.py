import scrapy
from crawler.items import CrawlerItem
from datetime import datetime
import re 

class Stories(scrapy.Spider):
    name = "test"

    def __init__(self) -> None:
        super().__init__()
        # self.start_urls = ["https://blog.reedsy.com/short-stories/kids/"]
        self.start_urls = []

        for i in range(10,100):
            self.start_urls.append(f"https://blog.reedsy.com/short-stories/kids/page/{i}/")

    def parse(self, response):
        hrefs = response.xpath("//a[@class = 'btn-blue btn-rounded btn-xxs']/@href").extract()
        
        for i in hrefs:
            url = "https://blog.reedsy.com" + i
            print(url)
            yield scrapy.Request(url,callback = self.parse_dir_contents)
                

    def parse_dir_contents(self, response):
        item =  CrawlerItem()

        # # item['id'] = response.xpath("//*[@id='prod']/div/h4[2]/strong//text()").extract()
        title = response.xpath("//div[@class = 'content-thin']/h1/text()").extract()
        lst_genres = response.xpath("//a[@class = 'btn-grey-dark btn-xxs btn-rounded space-right-xs-sm']/text()").extract()
        lst_text = response.xpath("//article[@class = 'font-alt submission-content space-top-xs-md space-bottom-xs-lg']/p/text()").extract()


        # print(title)
        # print(lst_genres)
        # print(lst_text)
        # exit()
        item['title'] = self.preprocess_title(title)
        item['genre'] = self.preprocess_genre(lst_genres)
        item['text'] = self.preprocess_text(lst_text)

        # item['text'] = 
        # item['']

        # print(item)
        # exit()

        yield item 

    def preprocess_title(self,title):
        return title[0].strip().strip(" ")

    def preprocess_genre(self,genre):
        return ', '.join(genre)

    def preprocess_text(self,text):
        return '\n'.join(text)

    