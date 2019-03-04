import pymysql
from sqlalchemy import create_engine
import sys

mysqlDB = 'mysql'
DBname = 'stocktushare'
DAILYTABLE = 'daily'
DAILYBASICTABLE = 'daily_basic'
STOCKBAISCTABLE = 'stock_basic'
COMPANYTABLE = 'stock_company'

try:
    stockDB = pymysql.connect(
        "localhost", "root", "", DBname,
        charset='utf8')  # 打开数据库连接  使用mysql连接数库
    cursorDB = stockDB.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
except:
    print('请检查数据库是否正常,程序将终止！！！')
    sys.exit()


try:
    mysqlCon = pymysql.connect(
        "localhost", "root", "", 'mysql',
        charset='utf8')  # 打开mysql数据库连接，用于创建新的数据库
    mysqlcur = mysqlCon.cursor()
except:
    print('数据库连接失败，请检查数据是否开启或是否存在mysql数据库')
    sys.exit()

cn = create_engine('mysql+pymysql://root:@localhost:3306/' + DBname +
                   '?charset=utf8')  #创建数据引擎方便批量插入数据