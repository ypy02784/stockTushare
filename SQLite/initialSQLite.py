#该文件夹主要用于初始化数据库，创建相关数据库和数据表下，此文件为手动创建数据库及数据表，第二版使用sql文档初始化数据库
#coding = utf-8

import pymysql
import sys,os
import connectSQLite


DBname = 'stocktushare'

def _create_sq_lite_table():
    file_list = _get_file_name('.//sql')#默认从sql文件夹中读取文件，TODO:在此之前应该判断该文件夹是否存在，不存在提醒并退出
    for file in file_list:
        if file == '' or not file:
            print('未指定sql文件，请重新选择')
            return

        try:
            f = open('.\\sqlite\\' + file , 'r', encoding='utf-8')
        except:
            print('文件打开失败，请检查' + file + '.sql文件是否在sql文件夹中')
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
                    connectSQLite.sqliteCur.execute(sql)
                    connectSQLite.sqliteCon.commit()
                    sql = ''
                else:
                    sql += each_line[0:len(each_line) - 1]
            print('初始化表' + file[:-4] + '成功！！！')
            
        except:
            print(file[:-4] + '数据表创建失败！！！')
            return False
        

def _get_file_name(file_dir):#查找sqlite文件下sql文件名，并返回list表   
    files = os.listdir(file_dir)#获取当前目录下所有文件名，返回为list
    list_name = []
    for file in files:
        if os.path.splitext(file)[1]=='.sql':  
            list_name.append(file)
    return list_name

    


#初始化数据库，
def initial_db():
    
    _create_sq_lite_table()
    print('数据库初始化完成！！！')


#只需调用initialDB函数即可完成数据库初始化

