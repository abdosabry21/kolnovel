import scrapy
import re


class MrSpider(scrapy.Spider):
    name = "mr"
    allowed_domains = ["kolnovel.me"]
    start_urls = [r"https://kolnovel.me/semperor-has-returnedz-128097/"]


    def parse(self, response):
        
        chapter_title=response.xpath('//blockquote/p/text()').get()
        print(chapter_title)
        
        
        
        
        
        
        
        content=response.xpath('//div[@id="kol_content"]/p/text()')
        a=[]
        for i in content:
            a.append(i.get().strip())
        
    
        title=response.xpath('//div[@class="epheader"]/h1/text()').get()
        
        
        try:
            numbers = re.findall(r'[0-9٠١٢٣٤٥٦٧٨٩]+\.?[0-9٠١٢٣٤٥٦٧٨٩]*', title)[-1]
            print(title)
        except:
            pass 
        

        list_as_string = ' '.join(a)
        print(list_as_string)
        # print(a)
        print(type(list_as_string))
        
        
        
        next_page=response.xpath('//div[@id="Bottum_Down"]//a[@rel="next"]/@href').get()
        # chapter=next_page[-7:-1]
        
        print("########################")
        try:
            with open(f'{numbers}.txt', 'a', encoding='utf-8') as f:
                f.write(chapter_title)
        except:
            pass
        try:
            with open(f'{numbers}.txt', 'a', encoding='utf-8') as f:
                f.write(list_as_string)
        except:
            pass
        
        
        
        try:
            print(numbers)
        except:
            pass
        
        
        if next_page is not None :
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            yield response.follow(next_page,callback=self.parse)