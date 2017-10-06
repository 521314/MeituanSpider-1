# import MySQLdb
import copy
import MySQLdb.cursors
from twisted.enterprise import adbapi

class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        dbparms = dict(
            host = settings['MYSQL_HOST'],
            db = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWORD'],
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool =adbapi.ConnectionPool('MySQLdb',**dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用深拷贝，避免插入数据库重复问题
        asynItem = copy.deepcopy(item)
        query = self.dbpool.runInteraction(self.do_insert, asynItem)
        query.addErrback(self.handle_error,asynItem,spider)
        return asynItem

    def handle_error(self,failure,item,spider):
        # 处理异步插入异常
        print(failure)

    def do_insert(self,cursor,item):
        insert_sql,params = item.get_insert_sql()
        cursor.execute(insert_sql,params)