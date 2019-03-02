#最原始版本，每个股票都创建一个数据表，太消耗资源
#coding=utf-8
import pymysql
import tushare as ts
import time

DBname = 'stocktushare'
dailyDB = 'daily'
dailybasicDB = 'dailybasic'
starttime = '20180101'
endtime = time.strftime('%Y%m%d', time.localtime(time.time()))  #默认系统当前日期

stockDB = pymysql.connect(
    "localhost", "root", "", DBname, charset='utf8')  # 打开数据库连接
cursorDB = stockDB.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor

try:
    tspro = ts.pro_api(
        'b5495988a3294331dda2b5c4a9bb7b9766f179863118c097e5296f60'
    )  #tushare pro 需要在初始化时加上token代码，网址https://tushare.pro
except:
    print('请检查计算机是否正常联网，无法连接tushare平台')


#查询股票基本信息并存入数据库
def insertStockbasicToDB(tspro):
    stock_basic = tspro.stock_basic(
        list_status='L'
    )  #默认获取上市股票基本信息，包含七个内容 ts_code，symbol,name,area,industry,market,list_date
    i = 0
    for stockbasic in stock_basic.values:
        try:
            if findRepeatRecord('stock_basic', stockbasic[0]):
                sql = 'insert into stock_basic (ts_code,symbol,name,area,industry,market,list_date) values (\'' + stockbasic[
                    0] + '\',\'' + stockbasic[1] + '\',\'' + stockbasic[
                        2] + '\',\'' + stockbasic[3] + '\',\'' + stockbasic[
                            4] + '\',\'' + stockbasic[
                                5] + '\',\'' + stockbasic[6] + '\')'
                cursorDB.execute(sql)
                stockDB.commit()
                i = i + 1

        except:
            stockDB.rollback()

    print('共插入%s条股票列表' % (i))


#查找股票基础表中重复数据
def findRepeatRecord(tablename, ts_code):
    sql = 'select * from ' + tablename + ' where ts_code=\'' + ts_code + '\''
    try:
        count = cursorDB.execute(sql)
        if count > 0:
            return False
        else:
            return True
    except:
        return False  #出错的话就返回false


def insertCompanyInfoToDB(tspro):
    sse = tspro.stock_company(exchange='SSE')  #获取上证公司信息
    szse = tspro.stock_company(exchange='SZSE')  #获取深证公司信息
    i = 0
    for ssetmp in sse.values:
        try:
            if findRepeatRecord('stock_company', ssetmp[0]):
                sql = 'insert into stock_company (ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,website,email,employees) values (\'' + str(
                    ssetmp[0]) + '\',\'' + str(ssetmp[1]) + '\',\'' + str(
                        ssetmp[2]) + '\',\'' + str(ssetmp[3]) + '\',\'' + str(
                            ssetmp[4]) + '\',' + str(ssetmp[5]) + ',\'' + str(
                                ssetmp[6]) + '\',\'' + str(
                                    ssetmp[7]) + '\',\'' + str(
                                        ssetmp[8]) + '\',\'' + str(
                                            ssetmp[9]) + '\',\'' + str(
                                                ssetmp[10]) + '\',' + str(
                                                    ssetmp[11]) + ')'
                # print(sql)
                cursorDB.execute(sql)
                stockDB.commit()
                i = i + 1
        except:
            stockDB.rollback()
    for szsetmp in szse.values:
        try:
            if findRepeatRecord('stock_company', szsetmp[0]):
                sql = 'insert into stock_company (ts_code,exchange,chairman,manager,secretary,reg_capital,setup_date,province,city,website,email,employees) values (\'' + str(
                    szsetmp[0]) + '\',\'' + str(szsetmp[1]) + '\',\'' + str(
                        szsetmp[2]
                    ) + '\',\'' + str(szsetmp[3]) + '\',\'' + str(
                        szsetmp[4]) + '\',' + str(szsetmp[5]) + ',\'' + str(
                            szsetmp[6]) + '\',\'' + str(
                                szsetmp[7]) + '\',\'' + str(
                                    szsetmp[8]) + '\',\'' + str(
                                        szsetmp[9]) + '\',\'' + str(
                                            szsetmp[10]) + '\',' + str(
                                                szsetmp[11]) + ')'
                cursorDB.execute(sql)
                stockDB.commit()
                i = i + 1
        except:
            stockDB.rollback()

    print('共插入%s条公司基本信息' % (i))


#获取所有股票的ts_code 数组
def getTscodeArray():
    sql = 'select distinct(ts_code) from stock_basic '
    try:
        cursorDB.execute(sql)
        df = cursorDB.fetchall()
    except:
        return None

    return df


#初始化时创建新的股票日交易表
def createStockDailyTable():
    i = 0
    sql = 'select distinct(symbol) from stock_basic '
    cursorDB.execute(sql)
    df = cursorDB.fetchall()
    for symbol in df:
        tablename = symbol[0] + 'daily'
        if findRepeatTable(tablename):  #不存在继续
            sql = createStockDailyTableSQL(tablename)
            try:
                cursorDB.execute(sql)
                i = i + 1
            except:
                stockDB.rollback()
                print('创建表%s失败' % (tablename))
    print('共创建股票日交易表%s份' % (i))


#创建stockdaily表的sql语句
def createStockDailyTableSQL(tablename):
    sql = 'CREATE TABLE `' + tablename + '` ('
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


#创建stockdailybasic表的sql语句
def createStockDailyBasicTableSQL(tablename):
    sql = 'CREATE TABLE `' + tablename + '` ('
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


#初始化时创建新的股票每日具体指标表
def createStockDailyBasicTable():
    i = 0
    sql = 'select distinct(symbol) from stock_basic '
    cursorDB.execute(sql)
    df = cursorDB.fetchall()
    for symbol in df:
        tablename = symbol[0] + 'dailybasic'
        if findRepeatTable(tablename):  #不存在继续
            sql = createStockDailyBasicTableSQL(tablename)
            try:
                cursorDB.execute(sql)
                i = i + 1
            except:
                stockDB.rollback()
                print('创建表%s失败' % (tablename))
    print('共创建股票每日指标表%s份' % (i))


#查找重复的数据表，存在返回false，否则true
def findRepeatTable(tablename):
    sql = 'select count(*) from information_schema.TABLES t where t.TABLE_SCHEMA ="' + DBname + '" and t.TABLE_NAME ="' + tablename + '"'
    try:
        cursorDB.execute(sql)
        result = cursorDB.fetchone()
        if result[0] > 0:
            return False
        else:
            return True

    except:
        return False


#获取指定股票每日交易信息
def getStockDailyInfo(ts_codetmp, starttimetmp, endtimetmp):
    df = tspro.daily(
        ts_code=ts_codetmp, start_date=starttimetmp, end_date=endtimetmp)
    i = 0
    for dailyinfo in df.values:
        sql = 'insert into  ' + ts_codetmp[
            0:6] + dailyDB + ' values ( ' + '\'' + dailyinfo[
                0] + '\',\'' + dailyinfo[1] + '\',' + str(dailyinfo[2]) + ','
        sql = sql + str(dailyinfo[3]) + ',' + str(dailyinfo[4]) + ',' + str(
            dailyinfo[5]) + ',' + str(dailyinfo[6]) + ',' + str(
                dailyinfo[7]) + ',' + str(dailyinfo[8]) + ','
        sql = sql + str(dailyinfo[9]) + ',' + str(dailyinfo[10]) + ')'
        try:
            cursorDB.execute(sql)
            stockDB.commit()
            i = i + 1
        except:
            stockDB.rollback()
            print('插入股票%s%s当天数据失败' % (dailyinfo[0], dailyinfo[1]))

    print('插入股票%s交易记录共%s条' % (ts_codetmp, i))


#获取所有股票的每日交易信息
def getAllstockDailyInfo(endtimetmp):
    tscodeAaary = getTscodeArray()
    for tscode in tscodeAaary:
        ts = tscode[0]
        maxdateinDB = getMaxdateFromTable(ts[0:6] + dailyDB)

        getStockDailyInfo(tscode[0], maxdateinDB, endtime)


#获取表中最大日期,否则返回默认starttime
def getMaxdateFromTable(tablename):
    sql = 'select max(trade_date) from ' + tablename
    try:
        cursorDB.execute(sql)
        result = cursorDB.fetchone()
        if result[0] == None:
            return starttime
    #  elif result[0]<starttime:
    #      return starttime
        else:
            a = int(result[0]) + 1  #最大日期加1
            return a
    except:
        return starttime


#删除指定表数据信息
def deleteTableInfor(tablename):
    tableNotExist = findRepeatTable(tablename)
    if tableNotExist: return None  #返回true表示表不存在直接返回空
    sql = 'delete from ' + tablename
    try:
        cursorDB.execute(sql)
    except:
        stockDB.rollback()


def dropTable(tablename):
    tableNotExist = findRepeatTable(tablename)
    if tableNotExist: return None  #返回true表示表不存在直接返回空
    sql = 'drop table ' + tablename
    try:
        cursorDB.execute(sql)
    except:
        stockDB.rollback()


def deleteAllStockDailyInfor():
    tscodeAaary = getTscodeArray()
    i = 0
    for tscode in tscodeAaary:
        ts = tscode[0]
        deleteTableInfor(ts[0:6] + dailyDB)
        i = i + 1
    print('共删除%s张股票每日交易表信息' % (i))


def deleteAllStockDailyBasicInfor():
    tscodeAaary = getTscodeArray()
    i = 0
    for tscode in tscodeAaary:
        ts = tscode[0]
        deleteTableInfor(ts[0:6] + dailybasicDB)
        i = i + 1
    print('共删除%s张股票每日指标表信息' % (i))


# insertStockbasicToDB(tspro)#获取上市股票列表，并插入数据库

# insertCompanyInfoToDB(tspro)

# createStockDailyBasicTable()

# getStockDailyInfo('000001.SZ','20170101','20190226')

stockDB.close()
