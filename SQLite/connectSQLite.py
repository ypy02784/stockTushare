import sqlite3
from sqlalchemy import create_engine
import sys,os


DBname = 'stocktushare'  #系统使用的数据库名称
DAILYTABLE = 'daily'  #股票每日交易信息表名称
DAILYBASICTABLE = 'daily_basic'  #股票每日交易信息指标表名称
STOCKBAISCTABLE = 'stock_basic'  #股票基本信息表名称
COMPANYTABLE = 'stock_company'  #公司基本信息表名称
TOPLISTTABLE = 'top_list' #龙虎榜
TOPINSTTABLE = 'top_inst' #龙虎榜机构交易
BLOCKTRADETABLE = 'block_trade'#大宗交易


#需要提前检查数据库stocktushare是否存在，不存在要执行初始化，否则退出，通过登录information_schema库检查
try:
    DBCon = sqlite3.connect("D:\stockTushare.db")  # 打开m数据库连接，用于创建新的数据库，sqlite数据库存在则打开，不存在则新建名为stockTushare.db的数据库
    DBCur = DBCon.cursor()#TODO:需要确认一下，是否是可以打开一个占用数据库，还是每次都要打开然后关闭
except:
    print('数据库连接失败，请检查数据库是否开启或是否安装了sqlite数据库')
    sys.exit()

# cn = create_engine('sqlite:///stockTushare.db')  #相对路劲创建数据引擎

cn = create_engine('sqlite:///d:\stockTushare.db')#便于同步github，先放d:盘

# con = cn.connect()
# for row in con.execute('SELECT * FROM table_info'):
#     print (row[0])


