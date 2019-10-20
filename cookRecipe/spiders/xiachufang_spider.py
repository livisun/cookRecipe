import scrapy
import json
from cookRecipe.items import CookrecipeItem

class xiachufang(scrapy.Spider): #定义一个爬虫类，继承自scrapy.Spider
    name = 'xiachufang' #定义爬虫名字
    start_urls = ['http://www.xiachufang.com/category/40076']#爬取下厨房 家常菜系列
    baseUrl = 'http://www.xiachufang.com'

    def parse(self,response):
        cplist = response.css('.recipe.recipe-215-horizontal.pure-g.image-link.display-block')
        # nextUrl = self.baseUrl + response.css('.pager .next::attr(href)').extract_first()
        for item in cplist:
            tt = item.css('a::attr(href)').extract_first()
            yield scrapy.Request(url = self.baseUrl + tt, callback = self.parseRecipe)
        # if nextUrl is not None:
        #     yield scrapy.Request(url = nextUrl, callback = self.parse)

    def parseRecipe(self,response):
        # item = CookrecipeItem()
        # item['name'] = response.css('.page-title::text').extract_first()
        # self.writeFile('name.txt',item['name'])
        # item['image'] = response.css('.cover.image.expandable.block-negative-margin img::attr(src)').extract_first()
        # self.writeFile('image.txt',item['image'])

        materials = []
        trList = response.xpath("//div[@class='ings']//table/tr")
        for td in trList:
            item = td.xpath("//td[@class='name']//text()").extract_first().strip().encode("utf-8").decode("utf-8")+':'+td.xpath("//td[@class='unit']//text()").extract_first().strip().encode("utf-8").decode("utf-8")
            print(item)
            materials.append(item)
        self.writeFile('materials2.txt',json.dumps(materials)+'\r\n')
        # for tr in response.css('.ings tr'):
        #     materials.append('name:' + tr.css('.name::text').extract_first() + 'unit:' + tr.css('.unit::text').extract_first())
        # item['materials'] = json.dumps(materials)
        # self.writeFile('materials.txt',item['materials'])

        # steps = []
        # for step in response.css('.steps li'):
        #     step = step.css('.text::text').extract_first()
        #     image = step.css('img::attr(src)').extract_first()
        #     if image is None:
        #         iamge = ''
        #     steps.append('step:' + step + 'image:'+ image )
        # item['steps'] = json.dumps(steps)
        # self.writeFile('steps.txt',item['steps'])
        # self.writeFile('test.txt',item['name'] + '---' + item['image'] + '---' + item['materials'] + '---' + item['steps'] + '\r\n')

    def writeFile(self,fileName,content):
        f = open(fileName, "a+", encoding="utf-8")
        f.write(content)
        f.close()