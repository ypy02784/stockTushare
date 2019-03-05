#V3版，所有当天交易数据存在daily表中，所有交易指标存在dailybasic表中,不在更新单条股票信息，daily表和daily_basic表都按天更新全部信息
#该文件只提供各种股票信息的获取，数据库维护将另建一个文件
#coding=utf-8
import pymysql
import tushare as ts
import time
import datetime

from sqlalchemy import create_engine
import sys

import connectDB 

STARTTIME = '20190101'
NOWTIME = time.strftime('%Y%m%d', time.localtime(time.time()))  #默认系统当前日期

try:
    tspro = ts.pro_api(
        'b5495988a3294331dda2b5c4a9bb7b9766f179863118c097e5296f60'
    )  #tushare pro 需要在初始化时加上token代码，网址https://tushare.pro
except:
    print('请检查计算机是否正常联网，无法连接tushare平台,程序将终止！！！')
    sys.exit()


#TODO:更新股票基本信息并存入数据库
def updateStockbasicToDB():
    stock_basic = tspro.stock_basic(
        list_status='L'
    )  #默认获取上市股票基本信息，包含七个内容 ts_code，symbol,name,area,industry,market,list_date
    if len(stock_basic.values) == 0: return  #无数据则推出函数
    try:
        if not (deleteTableInfo(connectDB.STOCKBAISCTABLE)):
            return  #删除表中数据失败则退出函数，避免重复数据
        stock_basic.to_sql(
            connectDB.STOCKBAISCTABLE, connectDB.cn, index=False, if_exists='append')
        print('更新股票基本信息表成功，目前上市股票有%s个股' % (len(stock_basic.values)))
    except:
        print('更新股票基本信息表失败，请检查数据库后重新更新')


#删除指定表中数据
def deleteTableInfo(tablename):
    sql = 'delete from ' + tablename
    try:
        count= connectDB.cursorDB.execute(sql)
        print('删除原数据表'+tablename+'%s条数据'%(count))
        connectDB.stockDB.commit()
        return True
    except:
        print('删除'+tablename+'表数据失败')  #出错的话就返回false
        return False


#TODO: 更新公司信息表
def updateCompanyInfoToDB():
    sse = tspro.stock_company(exchange='SSE')  #获取上证公司信息
    szse = tspro.stock_company(exchange='SZSE')  #获取深证公司信息
    if len(sse.values) == 0: return  #无数据则推出函数
    try:
        if not (deleteTableInfo(connectDB.COMPANYTABLE)): return
        sse.to_sql(connectDB.COMPANYTABLE, connectDB.cn, index=False, if_exists='append')
        szse.to_sql(connectDB.COMPANYTABLE, connectDB.cn, index=False, if_exists='append')
        print('更新上市公司信息表成功，目前上市公司有%s家' % (len(sse.values) + len(szse.values)))
    except:
        print('更新上市公司信息表失败，请检查数据库后重新更新')

def strTimeToTime(strTime=''):#将20190101格式的字符串转换成日期%Y-%m-%d返回,默认返回当前日期
    nowtmp = time.localtime(time.time())
    nowtmp =datetime.date(nowtmp.tm_year,nowtmp.tm_mon,nowtmp.tm_mday)
    if strTime=='':  return nowtmp
    tmp = time.strptime(strTime,'%Y%m%d')
    tmp = datetime.date(tmp.tm_year,tmp.tm_mon,tmp.tm_mday)
    return tmp


# TODO: 获取所有股票的指定日期交易信息
def getOneDayStockDailyInfo(endtimetmp):
    df = tspro.daily(trade_date=endtimetmp)
    if len(df.values) == 0: return  #无数据则推出函数
    try:
        df.to_sql(connectDB.DAILYTABLE, connectDB.cn, index=False, if_exists='append')
        print('插入' + str(endtimetmp) + '股票交易信息共%s条' % (len(df.values)))
    except:
        print('插入' + str(endtimetmp) + '股票交易信息失败,请检查数据库是否开启！')
        return

#TODO:更新所有股票交易信息,默认获取到当前日期，也可指定更新到某天
def getAllStockDailyInfo():
    starttime = getMaxdateFromTable(connectDB.DAILYTABLE)
    if starttime >= NOWTIME:
        print('当前信息已是最新')
        return
    #需要将20190101格式字符串转换为时间格式，便于循环
    begin = strTimeToTime(starttime)#转换成日期格式%Y-%m-%d
    end = strTimeToTime(NOWTIME)
    for i in range(1,(end - begin).days+1):#按日期循环
        day = begin + datetime.timedelta(days=i)
        day = str(day).replace('-','')
        getOneDayStockDailyInfo(day)

#TODO:获取指定日期龙虎榜信息
def getOneDayTopListInfo(daytime):
    df = tspro.top_list(trade_date=daytime)
    if len(df.values) == 0: return  #无数据则推出函数
    try:
        df.to_sql(connectDB.TOPLISTTABLE, connectDB.cn, index=False, if_exists='append')
        print('插入' + str(daytime) + '龙虎榜信息共%s条' % (len(df.values)))
    except:
        print('插入' + str(daytime) + '龙虎榜信息失败,请检查数据库是否开启！')
        return
    
def getAllTopListInfo():
    starttime = getMaxdateFromTable(connectDB.TOPLISTTABLE)
    if starttime >= NOWTIME:
        print('当前信息已是最新')
        return
    #需要将20190101格式字符串转换为时间格式，便于循环
    begin = strTimeToTime(starttime)#转换成日期格式%Y-%m-%d
    end = strTimeToTime(NOWTIME)
    for i in range(1,(end - begin).days+1):#按日期循环
        day = begin + datetime.timedelta(days=i)
        day = str(day).replace('-','')
        getOneDayTopListInfo(day)
  
#TODO:获取指定日期龙虎榜机构交易明细
def getOneDayTopInstInfo(daytime):
    df = tspro.top_inst(trade_date=daytime)
    if len(df.values) == 0: return  #无数据则推出函数
    try:
        df.to_sql(connectDB.TOPINSTTABLE, connectDB.cn, index=False, if_exists='append')
        print('插入' + str(daytime) + '龙虎榜机构交易共%s条' % (len(df.values)))
    except:
        print('插入' + str(daytime) + '龙虎榜机构交易失败,请检查数据库是否开启！')
        return
    
def getAllTopInstInfo():
    starttime = getMaxdateFromTable(connectDB.TOPINSTTABLE)
    if starttime >= NOWTIME:
        print('当前信息已是最新')
        return
    #需要将20190101格式字符串转换为时间格式，便于循环
    begin = strTimeToTime(starttime)#转换成日期格式%Y-%m-%d
    end = strTimeToTime(NOWTIME)
    for i in range(1,(end - begin).days+1):#按日期循环
        day = begin + datetime.timedelta(days=i)
        day = str(day).replace('-','')
        getOneDayTopInstInfo(day)

#TODO:获取指定日期大宗交易交易明细
def getOneDayBlockTradeInfo(daytime):
    df = tspro.block_trade(trade_date=daytime)
    if len(df.values) == 0: return  #无数据则推出函数
    try:
        df.to_sql(connectDB.BLOCKTRADETABLE, connectDB.cn, index=False, if_exists='append')
        print('插入' + str(daytime) + '大宗交易共%s条' % (len(df.values)))
    except:
        print('插入' + str(daytime) + '大宗交易失败,请检查数据库是否开启！')
        return
    
def getAllBlockTradeInfo():
    starttime = getMaxdateFromTable(connectDB.BLOCKTRADETABLE)
    if starttime >= NOWTIME:
        print('当前信息已是最新')
        return
    #需要将20190101格式字符串转换为时间格式，便于循环
    begin = strTimeToTime(starttime)#转换成日期格式%Y-%m-%d
    end = strTimeToTime(NOWTIME)
    for i in range(1,(end - begin).days+1):#按日期循环
        day = begin + datetime.timedelta(days=i)
        day = str(day).replace('-','')
        getOneDayBlockTradeInfo(day)

#TODO:获取所有股票的指定日期每日指标信息
def getOneDayStockDailyBasicInfo(endtimetmp):
    df = tspro.daily_basic(ts_code='', trade_date=endtimetmp)
    if len(df.values) == 0: return #无数据则推出函数
    try:
        df.to_sql(connectDB.DAILYBASICTABLE, connectDB.cn, index=False, if_exists='append')
        print('插入' + str(endtimetmp) + '每日指标信息共%s条' % (len(df.values)))
    except:
        print('插入' + str(endtimetmp) + '每日指标信息失败,请检查数据库是否开启！')
        return


#TODO:更新所有股票每日指标信息,默认获取到当前日期，也可指定更新到某天
def getAllStockDailyBasicInfo():
    starttime = getMaxdateFromTable(connectDB.DAILYBASICTABLE)
    if starttime >= NOWTIME:
        print('当前信息已是最新')
        return

    begin = strTimeToTime(starttime)#转换成日期格式%Y-%m-%d
    end = strTimeToTime(NOWTIME)
    for i in range(1,(end - begin).days+1):#按日期循环
        day = begin + datetime.timedelta(days=i)
        day = str(day).replace('-','')
        getOneDayStockDailyBasicInfo(day)


#获取表中最大日期,否则返回默认starttime
def getMaxdateFromTable(tablename):
    sql = 'select max(trade_date) from ' + tablename
    try:
        connectDB.cursorDB.execute(sql)
        result = connectDB.cursorDB.fetchone()
        if result[0] == None:
            return STARTTIME
    #  elif result[0]<starttime:
    #      return starttime
        else:
            a = int(result[0])
            return str(a)
    except:
        return STARTTIME


#更新所有股票数据
def updateStockInfo():

    updateStockbasicToDB()  #股票基本信息
    updateCompanyInfoToDB()  #公司信息
    getAllStockDailyInfo()  #日交易信息
    getAllStockDailyBasicInfo()  #日交易指标
    getAllTopListInfo()
    getAllTopInstInfo()
    getAllBlockTradeInfo()

getAllTopListInfo()
getAllTopInstInfo()
getAllBlockTradeInfo()
# updateStockInfo()

