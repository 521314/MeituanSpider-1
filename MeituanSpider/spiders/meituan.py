import json
import re
import scrapy
from MeituanSpider.items import SellerItem
from MeituanSpider.ponits import city_point


class MeituanSpider(scrapy.Spider):
    name = "meituan"
    # allowed_domains = ["i.meituan.com"]
    # start_urls = ['http://i.meituan.com/']
    city_name = '广州市'
    start_url = 'https://i.meituan.com/brunch/applet/index?&tag=food&page=0&firstTime=0&lat={1}&lng={0}'
    seller_url = 'https://i.meituan.com/brunch/applet/poi?id={0}'

    def start_requests(self):
        """
        将符合城市的坐标遍历进url
        """
        for i,j in city_point(self.city_name):
            url = self.start_url.format(i,j)
            yield self.make_requests_from_url(url)

    def parse(self, response):
        """
        获取商家poiid
        """
        items = json.loads(response.text)
        if items['poiList']['20639']:
            for item in items['poiList']['20639']:
                poiid = item['poiid']
                yield scrapy.Request(url=self.seller_url.format(poiid),callback=self.parse_info,meta={'historyCouponCount':item['historyCouponCount']})
        if len(items['poiList']['20639']) == 15:
            page_num = int(re.search('.*?page=(\d+?)&.*',response.url).group(1))
            point = re.search('.*?(lat=.*)', response.url).group(1)
            yield scrapy.Request(url='https://i.meituan.com/brunch/applet/index?&tag=food&page={0}&firstTime=0&{1}'.format(page_num+1,point),callback=self.parse)

    def parse_info(self,response):
        """
        根据poiid获取商家信息
        """
        seller_item = SellerItem()
        items_j = json.loads(response.text)
        seller_item['poiid'] = items_j['poiid']
        seller_item['sellername'] = items_j['name']
        seller_item['addr'] = items_j['addr']
        seller_item['phone'] = items_j['phone']
        seller_item['avgPrice'] = items_j['avgPrice']
        seller_item['avgScore'] = float(items_j['avgScore'])
        seller_item['historyCouponCount'] = response.meta['historyCouponCount']
        seller_item['coordinate'] = (items_j['lat'],items_j['lng'])
        yield seller_item
