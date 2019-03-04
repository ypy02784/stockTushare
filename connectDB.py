import pymysql
from sqlalchemy import create_engine
import sys
import initialDB

mysqlDB = 'information_schema'  #mysql系统表
DBname = 'stocktushare'  #系统使用的数据库名称
DAILYTABLE = 'daily'  #股票每日交易信息表名称
DAILYBASICTABLE = 'daily_basic'  #股票每日交易信息指标表名称
STOCKBAISCTABLE = 'stock_basic'  #股票基本信息表名称
COMPANYTABLE = 'stock_company'  #公司基本信息表名称

#需要提前检查数据库stocktushare是否存在，不存在要执行初始化，否则退出，通过登录information_schema库检查
try:
    mysqlCon = pymysql.connect(
        "localhost", "root", "", mysqlDB,
        charset='utf8')  # 打开mysql数据库连接，用于创建新的数据库
    mysqlcur = mysqlCon.cursor()
except:
    print('数据库连接失败，请检查数据库是否开启或是否安装了mysql数据库，请使用5.0版本以上的mysql')
    sys.exit()

sqltmp = 'SELECT * FROM information_schema.SCHEMATA where SCHEMA_NAME=\'' + DBname + '\''
mysqlcur.execute(sqltmp)
tmp = mysqlcur.fetchone()

if tmp == None:  #数据库不存在
    a = str.upper(input('数据库不存在，是否执行数据库初始化操作？（Y/N）：'))  #默认只能输入Y或者N
    while a != 'Y' and a != 'N':
        a = str.upper(input('数据库不存在，是否执行数据库初始化操作？（Y/N）：'))  #默认只能输入Y或者N
    try:
        if a == 'Y': initialDB.initialDB()  #是则初始化
        else:
            print('数据库不存在，系统将退出！')
            sys.exit()  #否则退出
    except:
        sys.exit()  #否则退出

try:
    # 打开数据库连接  使用mysql连接数库
    stockDB = pymysql.connect("localhost", "root", "", DBname, charset='utf8')
    cursorDB = stockDB.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
except:
    print('请检查数据库是否正常,stocktushare数据库可能不存在，请执行初始化数据库功能！！！')
    sys.exit()

cn = create_engine('mysql+pymysql://root:@localhost:3306/' + DBname +
                   '?charset=utf8')  #创建数据引擎方便批量插入数据

