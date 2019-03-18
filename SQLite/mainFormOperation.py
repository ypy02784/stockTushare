# noinspection PyInterpreter
import sys
from typing import List, Any

sys.path.append("./")  # 中上级目录为./
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDialog  # TODO:由于pyqt是用C编译的，所以vscode在编译时报错，但不影响使用
from PyQt5.QtCore import Qt
from UI.mainForm import Ui_MainWindow
import time
# 程序单元导入
from SQLite import connectSQLite
from SQLite import model_qtableview
from SQLite.upsdownsFmOperation import upsdownsWindow


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
        self.pushButton_moneyflow.clicked.connect(self.push_button_moneyflow_clicked)

        self.calendarWidget.selectionChanged.connect(self.calendar_widget_selected)
        self.selectData = self.calendarWidget.selectedDate().toString(
            Qt.ISODate).replace('-', '')  # 去掉时间中的‘-’,从2019-03-01转换成20190301格式
        # self.testfrom = upsdownsWindow()
        self.action_ups_and_downs.triggered.connect(self._upsdowns_show)
    global selectData
    DBname = 'stocktushare'
    NOWTIME = time.strftime('%Y%m%d', time.localtime(time.time()))  # 默认系统当前日期
    upsdownsFm = upsdownsWindow

    def calendar_widget_selected(self):
        self.selectData = self.calendarWidget.selectedDate().toString(
            Qt.ISODate).replace('-', '')

    def push_daily_button_clicked(self):
        model = model_qtableview._setDailyModel(self._get_daily_info(self.selectData))
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
        model = model_qtableview._setDailyBasickModel(
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
        model = model_qtableview._setStockBasickModel(self._get_stock_basic_info())
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
        model = model_qtableview._setCompanyModel(self._get_company_info())
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
        model = model_qtableview._setToplistModel(self._get_top_list_info(self.selectData))
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
        model = model_qtableview._setTopInstModel(self._get_top_inst_info(self.selectData))
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
        model = model_qtableview._setBlockTradeModel(self._get_block_trade_info(self.selectData))
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

    def push_button_moneyflow_clicked(self):
        model = model_qtableview._setmoneyflowModel(self._get_moneyflow_info(self.selectData))
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            dialog = QDialog()
            label = QLabel('没有' + self.selectData + '个股资金流向数据数据', dialog)
            label.move(50, 50)
            dialog.resize(400, 200)
            dialog.setWindowTitle("提示")
            # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog.exec_()

    def _get_moneyflow_info(self, temDay=NOWTIME):
        sql = 'select * from moneyflow where trade_date = ' + temDay + ' GROUP BY ts_code  '
        connectSQLite.DBCur.execute(sql)
        df = connectSQLite.DBCur.fetchall()
        connectSQLite.DBCon.commit()
        return df

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

    def _upsdowns_show(self):
        self.upsdownsFm = upsdownsWindow()
        self.upsdownsFm.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    # myWin.show()
    myWin.showMaximized()

    app.exec_()
