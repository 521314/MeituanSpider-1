 MeituanSpider/美团商家信息爬虫
 =============
> - 根据城市遍历经纬度坐标，爬取手机版美团商家信息
> - 城市边界数据来源于高德地图API
> - 使用shapely筛选符合要求的坐标
> - blog：[scrapy爬取美团美食商家信息](http://www.jianshu.com/p/a9a3f72347c1 "My blog")

### 运行环境

Win10<br>
Python3.6<br>
Scrapy 1.3.3<br>
MySQL Server 5.7<br>
<br/>

## 安装
```python
pip install -r requirements.txt
```

## settings配置

- mysql设置
```python
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'meituan'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234566'
```
- KEY设置
```python
GAODE_API_KEY = ''
```

- 爬取城市设置
```python
city_name = '广州市'
```



## 运行
```python
scrapy crawl meituan
```


### 运行效果
```
{'addr': '海珠区上渡路金豪商场二层（麦当劳斜对面）',
 'avgPrice': 65,
 'avgScore': 5.0,
 'coordinate': (23.10128, 113.30798),
 'historyCouponCount': 2547,
 'phone': '020-89621213',
 'poiid': '72758170',
 'sellername': '大舶韩国料理(3号店)'}
2017-10-06 21:00:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://i.meituan.com/brunch/applet/poi?id=103925393> (referer: https://i.meituan.com/brunch/applet/index?&tag=food&page=3&firstTime=0&lat=23.086045&lng=113.290281)
2017-10-06 21:00:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://i.meituan.com/brunch/applet/poi?id=103925393>
{'addr': '海珠区江燕南路68号',
 'avgPrice': 48,
 'avgScore': 5.0,
 'coordinate': (23.073222, 113.275608),
 'historyCouponCount': 489,
 'phone': '020-89115240',
 'poiid': '103925393',
 'sellername': '蜀客酸菜鱼(江燕南路店)'}
2017-10-06 21:00:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://i.meituan.com/brunch/applet/poi?id=50625927> (referer: https://i.meituan.com/brunch/applet/index?&tag=food&page=3&firstTime=0&lat=23.086045&lng=113.290281)
2017-10-06 21:00:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://i.meituan.com/brunch/applet/poi?id=50625927>
{'addr': '海珠区新港西路大江冲60号（愉景雅苑西右侧50米，信孚雅慧幼儿园旁）',
 'avgPrice': 28,
 'avgScore': 5.0,
 'coordinate': (23.09806, 113.31164),
 'historyCouponCount': 2236,
 'phone': '020-84269426',
 'poiid': '50625927',
 'sellername': '林小棠(客村店)'}
2017-10-06 21:00:59 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://i.meituan.com/brunch/applet/poi?id=99132144> (referer: https://i.meituan.com/brunch/applet/index?&tag=food&page=3&firstTime=0&lat=23.047933&lng=113.290281)
2017-10-06 21:00:59 [scrapy.core.scraper] DEBUG: Scraped from <200 https://i.meituan.com/brunch/applet/poi?id=99132144>
{'addr': '海珠区江晓路18号晓港商业城首层B1-103/103A（家福酒家楼下）',
 'avgPrice': 64,
 'avgScore': 5.0,
 'coordinate': (23.067446, 113.293024),
 'historyCouponCount': 11434,
 'phone': '020-89629309',
 'poiid': '99132144',
 'sellername': '木屋烧烤(晓港店)'}
```

### 数据展示
<br><br>
共抓取了广州市范围内6378家商家简单信息：<br><br>
 ![](http://upload-images.jianshu.io/upload_images/6926359-02003ea088f5366e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)<br>
 <br><br><br>
商家散点图：<br><br>
![](http://upload-images.jianshu.io/upload_images/6926359-d9f27d3f5bfe0c32.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) <br><br><br> <br>

商家词频：<br><br>
![](http://upload-images.jianshu.io/upload_images/6926359-e4ed8b302e90cb63.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240) <br><br><br> <br>


### 注意事项
- 程序仅供学习之用，请下载24小时内删除
- 程序已设置适当延迟，请合理使用
