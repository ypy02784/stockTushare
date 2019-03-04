#该文件夹主要用于初始化数据库，创建相关数据库和数据表
#coding = utf-8

import pymysql
import sys
from connectDB import DBname,DAILYBASICTABLE,DAILYTABLE,mysqlCon,mysqlcur,STOCKBAISCTABLE,COMPANYTABLE,stockDB,cursorDB

#返回stockdaily表的sql语句
def SQLstockDailyTable():
    sql = 'CREATE TABLE `daily` ('
    sql = sql + '`ts_code` varchar(10) DEFAULT NULL COMMENT \'股票代码\','
    sql = sql + '`trade_date` varchar(10) DEFAULT NULL COMMENT \'交易日期\','
    sql = sql + '`open` float DEFAULT NULL COMMENT \'开盘价\','
    sql = sql + '`high` float DEFAULT NULL COMMENT \'最高价\','
    sql = sql + '`low` float DEFAULT NULL COMMENT \'最低价\','
    sql = sql + '`close` float DEFAULT NULL COMMENT \'收盘价\','
    sql = sql + '`pre_close` float DEFAULT NULL COMMENT \'昨收价\','
    sql = sql + '`change` float DEFAULT NULL COMMENT \'涨跌额\','
    sql = sql + '`pct_chg` float DEFAULT NULL COMMENT\'	涨跌幅 （未复权，如果是复权请用 通用行情接口 ）\','
    sql = sql + '`vol` float DEFAULT NULL COMMENT \'成交量 （手）\','
    sql = sql + '`amount` float DEFAULT NULL COMMENT \'成交额 （千元）\''
    sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    return sql


#返回stockdailybasic表的sql语句
def SQLstockDailyBasicTable():
    sql = 'CREATE TABLE `daily_basic` ('
    sql = sql + '`ts_code` varchar(10) DEFAULT NULL COMMENT \'TS股票代码\','
    sql = sql + '`trade_date` varchar(10) DEFAULT NULL COMMENT \'交易日期\','
    sql = sql + '`close` float DEFAULT NULL COMMENT \'当日收盘价\','
    sql = sql + '`turnover_rate` float DEFAULT NULL COMMENT \'换手率（%）\','
    sql = sql + '`turnover_rate_f` float DEFAULT NULL COMMENT \'换手率（自由流通股）\','
    sql = sql + '`volume_ratio` float DEFAULT NULL COMMENT \'量比\','
    sql = sql + '`pe` float DEFAULT NULL COMMENT \'	市盈率（总市值/净利润）\','
    sql = sql + '`pe_ttm` float DEFAULT NULL COMMENT \'	市盈率（TTM）\','
    sql = sql + '`pb` float DEFAULT NULL COMMENT \'市净率（总市值/净资产）\','
    sql = sql + '`ps` float DEFAULT NULL COMMENT \'	市销率\','
    sql = sql + '`ps_ttm` float DEFAULT NULL COMMENT \'市销率（TTM）\','
    sql = sql + '`total_share` float DEFAULT NULL COMMENT \'总股本 （万）\','
    sql = sql + '`float_share` float DEFAULT NULL COMMENT \'流通股本 （万）\','
    sql = sql + ' `free_share` float DEFAULT NULL COMMENT \'自由流通股本 （万）\','
    sql = sql + ' `total_mv` float DEFAULT NULL COMMENT \'总市值 （万元）\','
    sql = sql + ' `circ_mv` float DEFAULT NULL COMMENT \'	流通市值（万元）\''
    sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8'
    return sql


def SQLstockBasicTable():
    sql = 'CREATE TABLE `stock_basic` ('
    sql = sql + '`ts_code` varchar(10) DEFAULT NULL COMMENT \'TS代码\','
    sql = sql + '`symbol` varchar(10) DEFAULT NULL COMMENT \'股票代码\','
    sql = sql + '`name` varchar(10) DEFAULT NULL COMMENT \'股票名称\','
    sql = sql + '`area` varchar(10) DEFAULT NULL COMMENT \'所在地域\','
    sql = sql + '`industry` varchar(10) DEFAULT NULL COMMENT \'所属行业\','
    sql = sql + '`fullname` varchar(255) DEFAULT NULL COMMENT \'股票全称\','
    sql = sql + '`enname` varchar(255) DEFAULT NULL COMMENT \'英文全称\','
    sql = sql + '`market` varchar(10) DEFAULT NULL COMMENT \'市场类型 （主板/中小板/创业板）\','
    sql = sql + '`exchange` varchar(10) DEFAULT NULL COMMENT \'交易所代码\','
    sql = sql + '`curr_type` varchar(10) DEFAULT NULL COMMENT \'交易货币\','
    sql = sql + '`list_status` varchar(10) DEFAULT NULL COMMENT \'上市状态： L上市 D退市 P暂停上市\','
    sql = sql + '`list_date` varchar(10) DEFAULT NULL COMMENT \'上市日期\','
    sql = sql + '`delist_date` varchar(10) DEFAULT NULL COMMENT \'退市日期\','
    sql = sql + '`is_hs` varchar(10) DEFAULT NULL COMMENT \'是否沪深港通标的，N否 H沪股通 S深股通\''
    sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    return sql


def SQLstockCompany():
    sql = 'CREATE TABLE `stock_company` ('
    sql = sql + '`ts_code` varchar(10) DEFAULT NULL COMMENT \'股票代码\','
    sql = sql + '`exchange` varchar(10) DEFAULT NULL COMMENT \'交易所代码 ，SSE上交所 SZSE深交所\','
    sql = sql + '`chairman` varchar(255) DEFAULT NULL COMMENT \'法人代表\','
    sql = sql + '`manager` varchar(255) DEFAULT NULL COMMENT \'总经理\','
    sql = sql + ' `secretary` varchar(255) DEFAULT NULL COMMENT \'董秘\','
    sql = sql + '`reg_capital` float DEFAULT NULL COMMENT \'	注册资本\','
    sql = sql + '`setup_date` varchar(10) DEFAULT NULL COMMENT \'注册日期\','
    sql = sql + '`province` varchar(100) DEFAULT NULL COMMENT \'所在省份\','
    sql = sql + '`city` varchar(100) DEFAULT NULL COMMENT \'所在城市\','
    sql = sql + '`introduction` varchar(255) DEFAULT NULL COMMENT \'公司介绍\','
    sql = sql + '`website` varchar(255) DEFAULT NULL COMMENT \'公司主页\','
    sql = sql + '`email` varchar(255) DEFAULT NULL COMMENT \'电子邮件\','
    sql = sql + '`office` varchar(255) DEFAULT NULL COMMENT \'办公室\','
    sql = sql + '`employees` int(11) DEFAULT NULL COMMENT \'员工人数\','
    sql = sql + '`main_business` varchar(255) DEFAULT NULL COMMENT \'主要业务及产品\','
    sql = sql + '`business_scope` varchar(255) DEFAULT NULL COMMENT \'经营范围\''
    sql = sql + ') ENGINE=InnoDB DEFAULT CHARSET=utf8;'
    return sql


def createTable():  #创建数据表
    stockDB = pymysql.connect(
        "localhost", "root", "", DBname, charset='utf8')  # 打开数据库连接
    cursorDB = stockDB.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
    sql1 = SQLstockBasicTable()
    sql2 = SQLstockCompany()
    sql3 = SQLstockDailyTable()
    sql4 = SQLstockDailyBasicTable()
    try:
        cursorDB.execute(sql1)  
        cursorDB.execute(sql2)  
        cursorDB.execute(sql3)  
        cursorDB.execute(sql4) 
    except Exception as e:
        stockDB.rollback()  # 事务回滚
        stockDB.close()
        print('创建数据表失败', e)
    else:
        stockDB.commit()  # 事务提交
        print('数据表创建成功')
        stockDB.close()

#如果原有表则删除表
def dropExistTable():
    stockDB = pymysql.connect(
        "localhost", "root", "", DBname, charset='utf8')  # 打开数据库连接
    cursorDB = stockDB.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
    sql1 = 'DROP TABLE IF EXISTS `stock_company`;'
    sql2 = 'DROP TABLE IF EXISTS `stock_basic`;'
    sql3 = 'DROP TABLE IF EXISTS `daily_basic`;'
    sql4 = 'DROP TABLE IF EXISTS `daily`;'
    
    try:
        cursorDB.execute(sql1)  
        cursorDB.execute(sql2)  
        cursorDB.execute(sql3)  
        cursorDB.execute(sql4)  
    except Exception as e:
        stockDB.close()
        print('删除原有数据表失败，请手动删除', e)
    else:
        stockDB.commit()  # 事务提交
        stockDB.close()
        # print('数据表删除成功', cursorDB.rowcount)
   
def creatStockTushareDB():
    sql = 'CREATE DATABASE IF NOT EXISTS ' + DBname + ' default charset utf8 COLLATE utf8_general_ci'
    try:
        print('正在创建数据库stocktushare......') 
        mysqlcur.execute(sql)
        mysqlCon.commit()
        print('创建数据库stocktushare成功') 
        return True
    except:
        print('创建数据库stocktushare失败')  #出错的话就返回false
        return False

#初始化数据库，
def initialDB():
    if creatStockTushareDB():#创建成功或者数据库已存在的情况下执行后面数据
        dropExistTable()  #创建数据库失败，说明已经已经存在，删除可能存在的数据表
        createTable()  #创建数据表
        print('数据库初始化完成！！！')
    else:
        print('数据库初始化失败，请检查数据库连接！！！')


#只需调用initialDB函数即可完成数据库初始化
initialDB()

mysqlCon.close()