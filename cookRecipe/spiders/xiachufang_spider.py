import scrapy
from w3lib.html import remove_tags
import json
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码，什么都不要改，就这样加入。
from cookRecipe.items import CookrecipeItem

class xiachufang(scrapy.Spider): #定义一个爬虫类，继承自scrapy.Spider
    name = 'xiachufang' #定义爬虫名字
    start_urls = ['http://www.xiachufang.com/category/40076']#爬取下厨房 家常菜系列
    baseUrl = 'http://www.xiachufang.com'

    def parse(self,response):
        cplist = response.xpath("//ul[@class='list']/li/div")
        nextUrl = self.baseUrl + response.xpath("//a[@class='next']/@href").extract_first()
        for item in cplist:
            tt = item.xpath("./a/@href").extract_first()
            yield scrapy.Request(url = self.baseUrl + tt, callback = self.parseRecipe)
        if nextUrl is not None:
            yield scrapy.Request(url = nextUrl, callback = self.parse)

    def parseRecipe(self,response):
        item = CookrecipeItem()
        #菜名
        item['name'] = response.xpath("//h1[@class='page-title']/text()").extract_first().strip()

        #效果图
        item['image'] = response.xpath("//div[@class='cover image expandable block-negative-margin']/img/@src").extract_first().strip()

        #用料
        materials = []
        material_selectors  = response.xpath("//div[@class='ings']//tr")
        for selector in material_selectors:
            #材料
            s1 = selector.xpath("./td[1]").extract_first()
            s1 = remove_tags(s1).strip()
            # 用量
            s2 = selector.xpath("./td[2]/text()").extract_first().strip()
            s = s1 + "：" + s2
            materials.append(s)
        item['materials'] = materials

        #做法步骤
        steps = []
        stepList = response.xpath("//div[@class='steps']//li")
        for sl in stepList:
            step = sl.xpath("./p/text()").extract_first().strip()
            image = sl.xpath('./img/@src').extract_first()
            if image is None:
                steps.append('step:' + step)
            else:
                steps.append('step:' + step + '(image:'+ image +')' )
        item['steps'] = steps
        return item

    def writeFile(self,fileName,content):
        f = open(fileName, "a+", encoding="utf-8")
        f.write(content)
        f.close()