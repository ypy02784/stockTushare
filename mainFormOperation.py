import sys
from PyQt5.QtWidgets import QApplication, QMainWindow  #TODO:由于pyqt是用C编译的，所以vscode在编译时报错，但不影响使用
from PyQt5.QtCore import Qt, QDate
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel
from UI.mainForm import *

import pymysql
import time
from connectDB import stockDB, cursorDB, DAILYBASICTABLE, DAILYTABLE, STOCKBAISCTABLE, COMPANYTABLE


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushDailyButton.clicked.connect(self.pushDailyButtonClicked)
        self.pushDailyBasicButton.clicked.connect(
            self.pushDailyBasicButtonClicked)
        self.pushStockBasicButton.clicked.connect(
            self.pushStockBasicButtonClicked)
        self.pushCompanyButton.clicked.connect(self.pushCompanyButtonClicked)
        self.calendarWidget.setSelectedDate(QDate(2019, 3, 1))
        self.selectData = self.calendarWidget.selectedDate().toString(
            Qt.ISODate).replace('-', '')  #去掉时间中的‘-’,从2019-03-01转换成20190301格式

    global selectData
    DBname = 'stocktushare'
    NOWTIME = time.strftime('%Y%m%d', time.localtime(time.time()))  #默认系统当前日期

    def pushDailyButtonClicked(self):
        model = self._setDailyModel(self._getDailyinfo(self.selectData))
        self.tableView.setModel(model)

    def pushDailyBasicButtonClicked(self):
        model = self._setDailyBasickModel(
            self._getDailyBasicInfo(self.selectData))
        self.tableView.setModel(model)

    def pushStockBasicButtonClicked(self):
        model = self._setStockBasickModel(self._getStockBasicInfo())
        self.tableView.setModel(model)

    def pushCompanyButtonClicked(self):
        model = self._setCompanyModel(self._getCompanyInfo())
        self.tableView.setModel(model)

    #设置股票交易信息model,参数为数据库查找返回数据集
    def _setDailyModel(self, df):
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

    #设置股票指标信息model,参数为数据库查找返回数据集
    def _setDailyBasickModel(self, df):
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

    #设置股票基本信息model,参数为数据库查找返回数据集
    def _setStockBasickModel(self, df):
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

    #设置公司信息model,参数为数据库查找返回数据集
    def _setCompanyModel(self, df):
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

    def _getDailyinfo(self, temDay=NOWTIME):
        sql = 'select * from daily where trade_date = ' + temDay + ' GROUP BY ts_code  '
        cursorDB.execute(sql)
        df = cursorDB.fetchall()
        stockDB.commit()
        return df

    def _getDailyBasicInfo(self, temDay=NOWTIME):
        sql = 'select * from daily_basic where trade_date = ' + temDay + ' GROUP BY ts_code  '
        cursorDB.execute(sql)
        df = cursorDB.fetchall()
        stockDB.commit()
        return df

    def _getStockBasicInfo(self):
        sql = 'select * from stock_basic '
        cursorDB.execute(sql)
        df = cursorDB.fetchall()
        stockDB.commit()
        return df

    def _getCompanyInfo(self):
        sql = 'select * from stock_company '
        cursorDB.execute(sql)
        df = cursorDB.fetchall()
        stockDB.commit()
        return df


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()

    app.exec_()