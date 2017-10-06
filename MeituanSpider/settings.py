BOT_NAME = 'MeituanSpider'

SPIDER_MODULES = ['MeituanSpider.spiders']
NEWSPIDER_MODULE = 'MeituanSpider.spiders'

ROBOTSTXT_OBEY = False
CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 8
DOWNLOAD_DELAY = 1
DOWNLOAD_TIMEOUT = 20
COOKIES_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
'charset': 'utf-8',
'Accept-Encoding': 'gzip',
'referer': 'https://servicewechat.com/wxde8ac0a21135c07d/19/page-frame.html',
'content-type': 'application/json',
'User-Agent': 'MicroMessenger/6.5.13.1100 NetType/WIFI Language/zh_CN',
'Host': 'i.meituan.com',
}

DOWNLOADER_MIDDLEWARES = {
   # 'MeituanSpider.middlewares.MyCustomDownloaderMiddleware': 543,
   #  'MeituanSpider.middlewares.ProxyPoolMiddleware': 400,
   #  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   #  'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = {
   'MeituanSpider.pipelines.MysqlTwistedPipeline': 300,
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
}

# LOG_LEVEL = 'INFO'

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'meituan'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234566'

SQL_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
SQL_DATE_FORMAT = '%Y-%m-%d'


GAODE_API_KEY = ''
