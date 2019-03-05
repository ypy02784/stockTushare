#该文件夹主要用于初始化数据库，创建相关数据库和数据表下，此文件为手动创建数据库及数据表，第二版使用sql文档初始化数据库
#coding = utf-8

import pymysql
import sys

mysqlDB = 'information_schema'
DBname = 'stocktushare'


def _createTable():
    if _executeTableSQL('table_info'):  #首先创建table_info表，sql中带数据
        #从table_info中读取数据，自动创建其余表
        try:
            stockCon = pymysql.connect(
                "localhost", "root", "", DBname, charset='utf8')
            stockCur = stockCon.cursor()
        except:
            print('数据库连接失败，请检查数据库stocktushare是否存在')
            sys.exit()
        try:
            sql = 'select distinct(tablename) from table_info where tablename <>\'table_info\''
            stockCur.execute(sql)
            stockCon.commit()
            df = stockCur.fetchall()
            for i in df:
                _executeTableSQL(i[0])
        except:
            print('数据库连接失败，无法自动初始化数据表！！！')


def _executeTableSQL(fileName):  #通过sql文件创建数据表,所有的sql文件通过navicat生成

    try:
        stockCon = pymysql.connect(
            "localhost", "root", "", DBname, charset='utf8')
        stockCur = stockCon.cursor()
    except:
        print('数据库连接失败，请检查数据库stocktushare是否存在')
        sys.exit()

    if fileName == '' or not fileName:
        print('未指定sql文件，请重新选择')
        return

    try:
        f = open('.\\sql\\' + fileName + '.sql', 'r', encoding='utf-8')
    except:
        print('文件打开失败，请检查' + fileName + '.sql文件是否在sql文件夹中')
        return
    sql = ''
    try:
        for each_line in f.readlines():
            if not each_line or each_line == '\n':  #如果是空或者是换行符，则什么也不做
                continue
            elif each_line[0:2] == '--':
                continue  #如果遇到注释符，跳过
            elif each_line[len(each_line) - 2] == ';':  #如果读到句末是‘；’则执行一条语句，最后是换行符\n，所以减2
                sql += each_line[0:len(each_line) - 1]
                stockCur.execute(sql)
                stockCon.commit()
                sql = ''
            else:
                sql += each_line[0:len(each_line) - 1]
        print('初始化表' + fileName + '成功！！！')
        return True
    except:
        print(fileName + '数据表创建失败！！！')
        return False
    finally:
        stockCon.close()


def _creatStockTushareDB():
    try:
        mysqlCon = pymysql.connect(
            "localhost", "root", "", mysqlDB,
            charset='utf8')  # 打开mysql数据库连接，用于创建新的数据库
        mysqlcur = mysqlCon.cursor()
    except:
        print('数据库连接失败，请检查数据库是否开启或是否存在mysql数据库，请使用5.0版本以上的mysql')
        sys.exit()

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
    finally:
        mysqlCon.close()


#初始化数据库，
def initialDB():
    if _creatStockTushareDB():  #创建成功或者数据库已存在的情况下执行后面数据
        _createTable()
        print('数据库初始化完成！！！')

    else:
        print('数据库初始化失败，请检查数据库连接！！！')


#只需调用initialDB函数即可完成数据库初始化
# initialDB()
