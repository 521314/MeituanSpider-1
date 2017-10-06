import datetime
import scrapy
from MeituanSpider.settings import SQL_DATETIME_FORMAT


class SellerItem(scrapy.Item):
    poiid = scrapy.Field()
    sellername = scrapy.Field()
    addr = scrapy.Field()
    phone = scrapy.Field()
    avgPrice = scrapy.Field()
    avgScore = scrapy.Field()
    historyCouponCount = scrapy.Field()
    coordinate = scrapy.Field()


    def get_insert_sql(self):
        insert_sql = '''
            insert into meishi_guangzhou(poiid,sellername,addr,phone,avgPrice,avgScore,historyCouponCount,coordinate,crawl_time)
        VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE historyCouponCount=VALUES(historyCouponCount),avgScore=VALUES(avgScore)
        '''
        poiid = self['poiid']
        sellername = self['sellername']
        addr = self['addr']
        phone = self['phone']
        avgPrice = self['avgPrice']
        avgScore = self['avgScore']
        historyCouponCount = self['historyCouponCount']
        coordinate = str(self['coordinate'])
        crawl_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)

        params = (poiid,sellername,addr,phone,avgPrice,avgScore,historyCouponCount,coordinate,crawl_time)

        return insert_sql, params