import sqlite3
from sqlalchemy import create_engine
from SQLite import initialSQLite
from SQLite.global_variable import DB_PATH


# 测试数据库文件是否存在，不存在初始化
try:
    f = open(DB_PATH)
    f.close()
except IOError:
    initialSQLite.initial_db()

# 需要提前检查数据库stocktushare是否存在，不存在要执行初始化，否则退出，通过登录information_schema库检查
try:
    DBCon = sqlite3.connect(DB_PATH)  # 打开m数据库连接，用于创建新的数据库，sqlite数据库存在则打开，不存在则新建名为stockTushare.db的数据库
    DBCur = DBCon.cursor()  # TODO:需要确认一下，是否是可以打开一个占用数据库，还是每次都要打开然后关闭
except:
    print('数据库连接失败，请检查数据库是否开启或是否安装了sqlite数据库')

cn = create_engine('sqlite:///'+DB_PATH)#便于同步github，先放d:盘


