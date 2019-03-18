from PyQt5 import QtGui


# 设置股票交易信息model,参数为数据库查找返回数据集
def _setDailyModel( df):
    """
    股票交易信息Model
    函数用以设置和tableview绑定的model，当传入的数据库返回数据为0时，返回0，当df有数据时，返回model
    """

    row = len(df)
    if row == 0: return 0
    vol = len(df[0])

    model = QtGui.QStandardItemModel()
    model.setRowCount(row)
    model.setColumnCount(vol)
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem('股票代码'))
    model.setHorizontalHeaderItem(1, QtGui.QStandardItem('交易日期'))
    model.setHorizontalHeaderItem(2, QtGui.QStandardItem('开盘价'))
    model.setHorizontalHeaderItem(3, QtGui.QStandardItem('最高价'))
    model.setHorizontalHeaderItem(4, QtGui.QStandardItem('最低价'))
    model.setHorizontalHeaderItem(5, QtGui.QStandardItem('收盘价'))
    model.setHorizontalHeaderItem(6, QtGui.QStandardItem('昨收价'))
    model.setHorizontalHeaderItem(7, QtGui.QStandardItem('涨跌额'))
    model.setHorizontalHeaderItem(8, QtGui.QStandardItem('涨跌幅'))
    model.setHorizontalHeaderItem(9, QtGui.QStandardItem('成交量 （手）'))
    model.setHorizontalHeaderItem(10, QtGui.QStandardItem('成交额 （千元）'))

    for i in range(row):
        for j in range(vol):
            tmp_data = df[i][j]
            model.setItem(i, j, QtGui.QStandardItem(str(tmp_data)))
    return model


# 设置股票指标信息model,参数为数据库查找返回数据集
def _setDailyBasickModel( df):
    """
    股票指标信息Model
    函数用以设置和tableview绑定的model，当传入的数据库返回数据为0时，返回0，当df有数据时，返回model
    """

    row = len(df)
    if row == 0: return 0
    vol = len(df[0])

    model = QtGui.QStandardItemModel()
    model.setRowCount(row)
    model.setColumnCount(vol)
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem('股票代码'))
    model.setHorizontalHeaderItem(1, QtGui.QStandardItem('交易日期'))
    model.setHorizontalHeaderItem(2, QtGui.QStandardItem('当日收盘价'))
    model.setHorizontalHeaderItem(3, QtGui.QStandardItem('换手率（%）'))
    model.setHorizontalHeaderItem(4, QtGui.QStandardItem('换手率（自由流通股）'))
    model.setHorizontalHeaderItem(5, QtGui.QStandardItem('量比'))
    model.setHorizontalHeaderItem(6, QtGui.QStandardItem('市盈率（总市值/净利润）'))
    model.setHorizontalHeaderItem(7, QtGui.QStandardItem('市盈率（TTM）'))
    model.setHorizontalHeaderItem(8, QtGui.QStandardItem('市净率（总市值/净资产）'))
    model.setHorizontalHeaderItem(9, QtGui.QStandardItem('市销率'))
    model.setHorizontalHeaderItem(10, QtGui.QStandardItem('市销率（TTM）'))
    model.setHorizontalHeaderItem(11, QtGui.QStandardItem('总股本 （万）'))
    model.setHorizontalHeaderItem(12, QtGui.QStandardItem('流通股本 （万）'))
    model.setHorizontalHeaderItem(13, QtGui.QStandardItem('自由流通股本 （万）'))
    model.setHorizontalHeaderItem(14, QtGui.QStandardItem('总市值 （万元）'))
    model.setHorizontalHeaderItem(15, QtGui.QStandardItem('流通市值（万元）'))

    for i in range(row):
        for j in range(vol):
            tmp_data = df[i][j]
            model.setItem(i, j, QtGui.QStandardItem(str(tmp_data)))
    return model


# 设置股票基本信息model,参数为数据库查找返回数据集
def _setStockBasickModel( df):
    """
    股票基本信息Model
    函数用以设置和tableview绑定的model，当传入的数据库返回数据为0时，返回0，当df有数据时，返回model
    """

    row = len(df)
    if row == 0: return 0
    vol = len(df[0])

    model = QtGui.QStandardItemModel()
    model.setRowCount(row)
    model.setColumnCount(vol)
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem('TS代码'))
    model.setHorizontalHeaderItem(1, QtGui.QStandardItem('股票代码'))
    model.setHorizontalHeaderItem(2, QtGui.QStandardItem('股票名称'))
    model.setHorizontalHeaderItem(3, QtGui.QStandardItem('所在地域'))
    model.setHorizontalHeaderItem(4, QtGui.QStandardItem('所属行业'))
    model.setHorizontalHeaderItem(5, QtGui.QStandardItem('股票全称'))
    model.setHorizontalHeaderItem(6, QtGui.QStandardItem('英文全称'))
    model.setHorizontalHeaderItem(7, QtGui.QStandardItem('市场类型 '))
    model.setHorizontalHeaderItem(8, QtGui.QStandardItem('交易所代码'))
    model.setHorizontalHeaderItem(9, QtGui.QStandardItem('交易货币'))
    model.setHorizontalHeaderItem(10, QtGui.QStandardItem('上市状态'))
    model.setHorizontalHeaderItem(11, QtGui.QStandardItem('上市日期'))
    model.setHorizontalHeaderItem(12, QtGui.QStandardItem('退市日期'))
    model.setHorizontalHeaderItem(13, QtGui.QStandardItem('是否沪深港'))

    for i in range(row):
        for j in range(vol):
            tmp_data = df[i][j]
            model.setItem(i, j, QtGui.QStandardItem(str(tmp_data)))
    return model


# 设置公司信息model,参数为数据库查找返回数据集
def _setCompanyModel( df):
    """
    公司信息Model
    函数用以设置和tableview绑定的model，当传入的数据库返回数据为0时，返回0，当df有数据时，返回model
    """

    row = len(df)
    if row == 0: return 0
    vol = len(df[0])

    model = QtGui.QStandardItemModel()
    model.setRowCount(row)
    model.setColumnCount(vol)
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem('TS代码'))
    model.setHorizontalHeaderItem(1, QtGui.QStandardItem('交易所代码'))
    model.setHorizontalHeaderItem(2, QtGui.QStandardItem('法人代表'))
    model.setHorizontalHeaderItem(3, QtGui.QStandardItem('总经理'))
    model.setHorizontalHeaderItem(4, QtGui.QStandardItem('董秘'))
    model.setHorizontalHeaderItem(5, QtGui.QStandardItem('注册资本'))
    model.setHorizontalHeaderItem(6, QtGui.QStandardItem('注册日期'))
    model.setHorizontalHeaderItem(7, QtGui.QStandardItem('所在省份'))
    model.setHorizontalHeaderItem(8, QtGui.QStandardItem('所在城市'))
    model.setHorizontalHeaderItem(9, QtGui.QStandardItem('公司介绍'))
    model.setHorizontalHeaderItem(10, QtGui.QStandardItem('公司主页'))
    model.setHorizontalHeaderItem(11, QtGui.QStandardItem('电子邮件'))
    model.setHorizontalHeaderItem(12, QtGui.QStandardItem('办公室'))
    model.setHorizontalHeaderItem(13, QtGui.QStandardItem('员工人数'))
    model.setHorizontalHeaderItem(14, QtGui.QStandardItem('主要业务及产品'))
    model.setHorizontalHeaderItem(15, QtGui.QStandardItem('经营范围'))

    for i in range(row):
        for j in range(vol):
            tmp_data = df[i][j]
            model.setItem(i, j, QtGui.QStandardItem(str(tmp_data)))
    return model


# 设置龙虎榜信息model,参数为数据库查找返回数据集
def _setToplistModel( df):
    """
    股票交易信息Model
    函数用以设置和tableview绑定的model，当传入的数据库返回数据为0时，返回0，当df有数据时，返回model
    """

    row = len(df)
    if row == 0: return 0
    vol = len(df[0])

    model = QtGui.QStandardItemModel()
    model.setRowCount(row)
    model.setColumnCount(vol)
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem('交易日期'))
    model.setHorizontalHeaderItem(1, QtGui.QStandardItem('股票代码'))
    model.setHorizontalHeaderItem(2, QtGui.QStandardItem('名称'))
    model.setHorizontalHeaderItem(3, QtGui.QStandardItem('收盘价'))
    model.setHorizontalHeaderItem(4, QtGui.QStandardItem('涨跌幅'))
    model.setHorizontalHeaderItem(5, QtGui.QStandardItem('换手率'))
    model.setHorizontalHeaderItem(6, QtGui.QStandardItem('总成交额'))
    model.setHorizontalHeaderItem(7, QtGui.QStandardItem('龙虎榜卖出额'))
    model.setHorizontalHeaderItem(8, QtGui.QStandardItem('龙虎榜买入额'))
    model.setHorizontalHeaderItem(9, QtGui.QStandardItem('龙虎榜成交额'))
    model.setHorizontalHeaderItem(10, QtGui.QStandardItem('龙虎榜净买入额'))
    model.setHorizontalHeaderItem(11, QtGui.QStandardItem('龙虎榜净买额占比'))
    model.setHorizontalHeaderItem(12, QtGui.QStandardItem('龙虎榜成交额占比'))
    model.setHorizontalHeaderItem(13, QtGui.QStandardItem('当日流通市值'))
    model.setHorizontalHeaderItem(14, QtGui.QStandardItem('上榜理由'))

    for i in range(row):
        for j in range(vol):
            tmp_data = df[i][j]
            model.setItem(i, j, QtGui.QStandardItem(str(tmp_data)))
    return model


# 设置龙虎榜机构交易信息model,参数为数据库查找返回数据集
def _setTopInstModel( df):
    """
    股票交易信息Model
    函数用以设置和tableview绑定的model，当传入的数据库返回数据为0时，返回0，当df有数据时，返回model
    """

    row = len(df)
    if row == 0: return 0
    vol = len(df[0])

    model = QtGui.QStandardItemModel()
    model.setRowCount(row)
    model.setColumnCount(vol)
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem('交易日期'))
    model.setHorizontalHeaderItem(1, QtGui.QStandardItem('股票代码'))
    model.setHorizontalHeaderItem(2, QtGui.QStandardItem('营业部名称'))
    model.setHorizontalHeaderItem(3, QtGui.QStandardItem('买入额（万）'))
    model.setHorizontalHeaderItem(4, QtGui.QStandardItem('买入占总成交比例'))
    model.setHorizontalHeaderItem(5, QtGui.QStandardItem('卖出额（万）'))
    model.setHorizontalHeaderItem(6, QtGui.QStandardItem('卖出占总成交比例'))
    model.setHorizontalHeaderItem(7, QtGui.QStandardItem('净成交额（万）'))

    for i in range(row):
        for j in range(vol):
            tmp_data = df[i][j]
            model.setItem(i, j, QtGui.QStandardItem(str(tmp_data)))
    return model


# 设置大宗交易信息model,参数为数据库查找返回数据集
def _setBlockTradeModel( df):
    """
    股票交易信息Model
    函数用以设置和tableview绑定的model，当传入的数据库返回数据为0时，返回0，当df有数据时，返回model
    """

    row = len(df)
    if row == 0: return 0
    vol = len(df[0])

    model = QtGui.QStandardItemModel()
    model.setRowCount(row)
    model.setColumnCount(vol)
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem('股票代码'))
    model.setHorizontalHeaderItem(1, QtGui.QStandardItem('交易日期'))
    model.setHorizontalHeaderItem(2, QtGui.QStandardItem('成交价'))
    model.setHorizontalHeaderItem(3, QtGui.QStandardItem('成交量（万股）'))
    model.setHorizontalHeaderItem(4, QtGui.QStandardItem('成交金额'))
    model.setHorizontalHeaderItem(5, QtGui.QStandardItem('买方营业部'))
    model.setHorizontalHeaderItem(6, QtGui.QStandardItem('卖方营业部'))

    for i in range(row):
        for j in range(vol):
            tmp_data = df[i][j]
            model.setItem(i, j, QtGui.QStandardItem(str(tmp_data)))
    return model

# 设置个股资金流向信息model,参数为数据库查找返回数据集
def _setmoneyflowModel(df):
    """
    个股交易信息信息Model
    函数用以设置和tableview绑定的model，当传入的数据库返回数据为0时，返回0，当df有数据时，返回model
    """

    row = len(df)
    if row == 0: return 0
    vol = len(df[0])

    model = QtGui.QStandardItemModel()
    model.setRowCount(row)
    model.setColumnCount(vol)
    model.setHorizontalHeaderItem(0, QtGui.QStandardItem('交易日期'))
    model.setHorizontalHeaderItem(1, QtGui.QStandardItem('股票代码'))
    model.setHorizontalHeaderItem(2, QtGui.QStandardItem('小单买入量（手）'))
    model.setHorizontalHeaderItem(3, QtGui.QStandardItem('小单买入金额（万元）'))
    model.setHorizontalHeaderItem(4, QtGui.QStandardItem('小单卖出量（手）'))
    model.setHorizontalHeaderItem(5, QtGui.QStandardItem('小单卖出金额（万元）'))
    model.setHorizontalHeaderItem(6, QtGui.QStandardItem('中单买入量（手）'))
    model.setHorizontalHeaderItem(7, QtGui.QStandardItem('中单买入金额（万元）'))
    model.setHorizontalHeaderItem(8, QtGui.QStandardItem('中单卖出量（手）'))
    model.setHorizontalHeaderItem(9, QtGui.QStandardItem('中单卖出金额（万元）'))
    model.setHorizontalHeaderItem(10, QtGui.QStandardItem('大单买入量（手）'))
    model.setHorizontalHeaderItem(11, QtGui.QStandardItem('大单买入金额（万元）'))
    model.setHorizontalHeaderItem(12, QtGui.QStandardItem('大单卖出量（手）'))
    model.setHorizontalHeaderItem(13, QtGui.QStandardItem('大单卖出金额（万元）'))
    model.setHorizontalHeaderItem(14, QtGui.QStandardItem('特大单买入量（手）'))
    model.setHorizontalHeaderItem(15, QtGui.QStandardItem('特大单买入金额（万元）'))
    model.setHorizontalHeaderItem(16, QtGui.QStandardItem('特大单卖出量（手）'))
    model.setHorizontalHeaderItem(17, QtGui.QStandardItem('特大单卖出金额（万元）'))
    model.setHorizontalHeaderItem(18, QtGui.QStandardItem('净流入量（手）'))
    model.setHorizontalHeaderItem(19, QtGui.QStandardItem('净流入额（万元）'))

    for i in range(row):
        for j in range(vol):
            tmp_data = df[i][j]
            model.setItem(i, j, QtGui.QStandardItem(str(tmp_data)))
    return model