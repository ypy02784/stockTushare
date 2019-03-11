# coding = utf-8

from SQLite import connectSQLite


def select_from_table(sql=''):
    if (sql == '') or (not sql): return None  # 如果为空或没指定则返回
    try:
        connectSQLite.DBCur.execute(sql)
        connectSQLite.DBCon.commit()
        result = connectSQLite.DBCur.fetchall()
        return result
    except:
        print('查询表失败')
        return None


def insert_into_table(sql=''):
    if (sql == '') or (not sql): return False  # 如果为空或没指定则返回
    try:
        connectSQLite.DBCur.execute(sql)
        connectSQLite.DBCon.commit()
        return True
    except:
        print('插入表失败')
        return False


def update_table(sql=''):
    if (sql == '') or (not sql): return False  # 如果为空或没指定则返回
    try:
        connectSQLite.DBCur.execute(sql)
        connectSQLite.DBCon.commit()
        return True
    except:
        print('更新表失败')
        return False
