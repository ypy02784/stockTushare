# noinspection PyInterpreter
import sys
from typing import List, Any

sys.path.append("./")  # 中上级目录为./
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog  # TODO:由于pyqt是用C编译的，所以vscode在编译时报错，但不影响使用
from PyQt5.QtCore import Qt
from UI.mainForm import *
import time
# 程序单元导入
from SQLite import  connectSQLite



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushDailyButton.clicked.connect(self.push_daily_button_clicked)
        self.pushDailyBasicButton.clicked.connect(
            self.push_daily_basic_button_clicked)
        self.pushStockBasicButton.clicked.connect(
            self.push_stock_basic_button_clicked)
        self.pushCompanyButton.clicked.connect(self.push_company_button_clicked)
        self.pushToplistButton.clicked.connect(self.push_top_list_button_clicked)
        self.pushTopInstButton.clicked.connect(self.push_top_inst_button_clicked)
        self.pushBlockTradeButton.clicked.connect(self.push_block_trade_button_clicked)
        self.action_update_Daily_Info.triggered.connect(self.action_daily_clicked)
        self.calendarWidget.selectionChanged.connect(self.calendar_widget_selected)
        self.selectData = self.calendarWidget.selectedDate().toString(
            Qt.ISODate).replace('-', '')  # 去掉时间中的‘-’,从2019-03-01转换成20190301格式

    global selectData
    DBname = 'stocktushare'
    NOWTIME = time.strftime('%Y%m%d', time.localtime(time.time()))  # 默认系统当前日期

    def calendar_widget_selected(self):
        self.selectData = self.calendarWidget.selectedDate().toString(
            Qt.ISODate).replace('-', '')

    def push_daily_button_clicked(self):
        model = self._set_daily_model(self._get_daily_info(self.selectData))
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            dialog = QDialog()
            label = QLabel('没有' + self.selectData + '交易数据', dialog)
            label.move(50, 50)
            dialog.resize(400, 200)
            dialog.setWindowTitle("提示")
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def push_daily_basic_button_clicked(self):
        model = self._set_daily_basick_model(
            self._get_daily_basic_info(self.selectData))
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            dialog = QDialog()
            label = QLabel('没有' + self.selectData + '交易指标数据', dialog)
            label.move(50, 50)
            dialog.resize(400, 200)
            dialog.setWindowTitle("提示")
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def push_stock_basic_button_clicked(self):
        model = self._set_stock_basick_model(self._get_stock_basic_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            dialog = QDialog()
            label = QLabel('没有股票基本信息数据', dialog)
            label.move(50, 50)
            dialog.setWindowTitle("提示")
            dialog.resize(400, 200)
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def push_company_button_clicked(self):
        model = self._set_company_model(self._get_company_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            dialog = QDialog()
            label = QLabel('没有公司基本信息数据', dialog)
            label.move(50, 50)
            dialog.setWindowTitle("提示")
            dialog.resize(400, 200)
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def push_top_list_button_clicked(self):
        model = self._set_toplist_model(self._get_top_list_info(self.selectData))
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            dialog = QDialog()
            label = QLabel('没有' + self.selectData + '龙虎榜数据数据', dialog)
            label.move(50, 50)
            dialog.resize(400, 200)
            dialog.setWindowTitle("提示")
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def push_top_inst_button_clicked(self):
        model = self._set_top_inst_model(self._get_top_inst_info(self.selectData))
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            dialog = QDialog()
            label = QLabel('没有' + self.selectData + '龙虎榜机构交易数据数据', dialog)
            label.move(50, 50)
            dialog.resize(400, 200)
            dialog.setWindowTitle("提示")
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def push_block_trade_button_clicked(self):
        model = self._set_block_trade_model(self._get_block_trade_info(self.selectData))
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            dialog = QDialog()
            label = QLabel('没有' + self.selectData + '大宗交易数据数据', dialog)
            label.move(50, 50)
            dialog.resize(400, 200)
            dialog.setWindowTitle("提示")
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def action_daily_clicked(self):
        return

    # 设置股票交易信息model,参数为数据库查找返回数据集
    def _set_daily_model(self, df):
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
    def _set_daily_basick_model(self, df):
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
    def _set_stock_basick_model(self, df):
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
    def _set_company_model(self, df):
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
    def _set_toplist_model(self, df):
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
    def _set_top_inst_model(self, df):
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
    def _set_block_trade_model(self, df):
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

    def _get_daily_info(self, temDay=NOWTIME):
        sql = 'select * from daily where trade_date = ' + temDay + ' GROUP BY ts_code  '
        connectSQLite.DBCur.execute(sql)
        df = connectSQLite.DBCur.fetchall()
        connectSQLite.DBCon.commit()
        return df

    def _get_daily_basic_info(self, temDay=NOWTIME):
        sql = 'select * from daily_basic where trade_date = ' + temDay + ' GROUP BY ts_code  '
        connectSQLite.DBCur.execute(sql)
        df = connectSQLite.DBCur.fetchall()
        connectSQLite.DBCon.commit()
        return df

    def _get_stock_basic_info(self):
        sql = 'select * from stock_basic '
        connectSQLite.DBCur.execute(sql)
        df = connectSQLite.DBCur.fetchall()
        connectSQLite.DBCon.commit()
        return df

    def _get_company_info(self):
        sql = 'select * from stock_company '
        connectSQLite.DBCur.execute(sql)
        df = connectSQLite.DBCur.fetchall()
        connectSQLite.DBCon.commit()
        return df

    def _get_top_list_info(self, temDay=NOWTIME):
        sql = 'select * from top_list where trade_date = ' + temDay + ' GROUP BY ts_code '
        connectSQLite.DBCur.execute(sql)
        df = connectSQLite.DBCur.fetchall()
        connectSQLite.DBCon.commit()
        return df

    def _get_top_inst_info(self, temDay=NOWTIME):
        sql = 'select * from top_inst where trade_date = ' + temDay + ' GROUP BY ts_code '
        connectSQLite.DBCur.execute(sql)
        df = connectSQLite.DBCur.fetchall()
        connectSQLite.DBCon.commit()
        return df

    def _get_block_trade_info(self, temDay=NOWTIME):
        sql = 'select * from block_trade where trade_date = ' + temDay + ' GROUP BY ts_code '
        connectSQLite.DBCur.execute(sql)
        df = connectSQLite.DBCur.fetchall()
        connectSQLite.DBCon.commit()
        return df


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()

    app.exec_()
