# cookRecipe
爬取下厨房菜谱

> 因为下厨房并未提供API，网上一些菜谱接口也都要收费，于是自己动手，写了个爬虫，代码很少，当然功能也很简单，感兴趣请自行添加修改。

目前选择性爬取了下厨房家常菜系列
```
  name = 'xiachufang' #定义爬虫名字
  start_urls = ['http://www.xiachufang.com/category/40076']#爬取下厨房 家常菜系列
  baseUrl = 'http://www.xiachufang.com'
```
如需爬取更多菜系，自行修改url

本爬虫采用scrapy框架，并将数据存入本地mogodb数据库中，数据配置在setting.py中，可根据自行配置
```
# mongodb
HOST = "127.0.0.1"  # 服务器地址
PORT = 27017  # mongo默认端口号
USER = ""
PWD = ""
DB = "xiachufang"
TABLE = "caipu"
```

