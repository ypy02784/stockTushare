# 该文件夹主要用于初始化数据库，创建相关数据库和数据表下，此文件为手动创建数据库及数据表，第二版使用sql文档初始化数据库
# coding = utf-8

import os
import sqlite3
from SQLite.global_variable import DB_TABLE_LIST


def _create_sq_lite_table(DBCur):
    # 默认从sql文件夹中读取文件，sql文件必须用utf-8无bom方式保存，否则会出现语法错误，特别是有中文字符的是否，
    # TODO:在此之前应该判断该文件夹及相关sql文件是否存在，不存在提醒并退出
    if os.path.exists('sql'):
        file_list = _get_file_name('.//sql')
        lose_sql = ''
        for i in DB_TABLE_LIST:
            if not(i+'.sql' in file_list):
                lose_sql += '文件'+i+'.sql不存在'+'\n'
                continue
        if lose_sql != '':
            print(lose_sql+'数据文件不全，请重新安装本程序！')
            os.sys.exit()
        for file in file_list:
            if file == '' or not file:
                print('未指定sql文件，请重新选择')
                return
            try:
                f = open('.\\sql\\' + file, 'r', encoding='utf-8')
            except:
                print('文件打开失败，请检查' + file + '文件是否在sql文件夹中')
                return

            sql = ''
            try:
                for each_line in f.readlines():
                    if not each_line or each_line == '\n':  # 如果是空或者是换行符，则什么也不做
                        continue
                    elif each_line[0:2] == '--':
                        continue  # 如果遇到注释符，跳过
                    # elif each_line[len(each_line) - 2] == ';':  #如果读到句末是‘；’则执行一条语句，最后是换行符\n，所以减2
                    #     sql += str.strip(each_line[0:len(each_line) - 1])
                    #     DBCur.execute(sql)
                    #     DBCon.commit()
                    #     sql = ''
                    else:
                        sql += each_line[0:len(each_line) - 1]
                    # sql += each_line[0:len(each_line) - 1]
                # 该函数先commit，再运行sql语句，所以不需要再commit一下
                DBCur.executescript(sql)
                print('初始化表' + file[:-4] + '成功！！！')

            except Exception as e:
                print(e)
                return False
    else:
        print('数据库初始化失败，请确认sql文件夹是否存在，否则请重新安装本程序！！！')
        os.sys.exit()


def _get_file_name(file_dir):  # 查找sqlite文件下sql文件名，并返回list表
    files = os.listdir(file_dir)  # 获取当前目录下所有文件名，返回为list
    list_name = []
    for file in files:
        if os.path.splitext(file)[1] == '.sql':
            list_name.append(file)
    return list_name


# 初始化数据库，
def initial_db():
    # connect函数连接数据库，数据库存在则连接，不存在则创建一个数据库
    DBCon = sqlite3.connect("stockTushare.db")
    DBCur = DBCon.cursor()  # TODO:需要确认一下，是否是可以打开一个占用数据库，还是每次都要打开然后关闭
    _create_sq_lite_table(DBCur)
    DBCur.close()
    DBCon.close()
    print('数据库初始化完成！！！')

# initial_db()
