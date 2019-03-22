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
from SQLite import getStockInfoSQLite



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self._init_combobox_stock_name()
        self.comboBox_stock_name.activated.connect(self._on_combobox_stock_name_activate)
        # 按钮操作
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
        self.pushButton_delete_code.clicked.connect(self.pushButton_delete_code_clicked)

        self.calendarWidget.selectionChanged.connect(self.calendar_widget_selected)

        # 更新菜单操作
        self.action_ups_and_downs.triggered.connect(self._upsdowns_show)
        self.action_update_stock_basic_info.triggered.connect(self._update_stock_basic_info_clicked)
        self.action_update_daily_info.triggered.connect(self._update_stock_daily_info_clicked)
        self.action_update_daily_basic_info.triggered.connect(self._update_stock_daily_basic_info_clicked)
        self.action_update_company_info.triggered.connect(self._update_company_info_clicked)
        self.action_update_top_list_info.triggered.connect(self._update_top_list_info_clicked)
        self.action_update_top_inst_info.triggered.connect(self._update_top_inst_info_clicked)
        self.action_update_block_trade_info.triggered.connect(self._update_block_trade_info_clicked)
        self.action_update_moneyflow_info.triggered.connect(self._update_moneyflow_info_clicked)
        self.action_update_all_info.triggered.connect(self._update_all_info_clicked)

    stocknamelist = []  # 记录股票名称信息
    stockcodelist = []  # 记录股票代码信息
    selectData = ''
    DBname = 'stocktushare'
    NOWTIME = time.strftime('%Y%m%d', time.localtime(time.time()))  # 默认系统当前日期
    upsdownsFm = upsdownsWindow

    def calendar_widget_selected(self):
        self.selectData = self.calendarWidget.selectedDate().toString(
            Qt.ISODate).replace('-', '')

    def pushButton_delete_code_clicked(self):
        self.lineEdit_stock_code.setText('')
        self.comboBox_stock_name.setCurrentIndex(-1)

    def add_query_code_sql(self):
        sql = ''
        if self.checkBox_select_date.isChecked():
            # 去掉时间中的‘-’,从2019-03-01转换成20190301格式
            self.selectData = self.calendarWidget.selectedDate().toString(
                Qt.ISODate).replace('-', '')
            if self.lineEdit_stock_code.text() != '':
                sql = 'where ts_code = \'' + self.lineEdit_stock_code.text() + '\'' + ' and trade_date=\'' + self.selectData + '\''
            else:
                sql = 'where trade_date=\'' + self.selectData + '\''
        elif self.lineEdit_stock_code.text() == '':
            # 如果时间未勾选，代码框没有数据，则返回空
            return ''
        else:
            sql = 'where ts_code = \'' + self.lineEdit_stock_code.text() + '\''
        return sql

    def push_daily_button_clicked(self):
        model = model_qtableview._setDailyModel(self._get_daily_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有' + self.selectData + '交易数据')

    def push_daily_basic_button_clicked(self):
        model = model_qtableview._setDailyBasickModel(
            self._get_daily_basic_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有' + self.selectData + '交易指标数据')

    def push_stock_basic_button_clicked(self):
        model = model_qtableview._setStockBasickModel(self._get_stock_basic_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有股票基本信息数据')

    def push_company_button_clicked(self):
        model = model_qtableview._setCompanyModel(self._get_company_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有公司基本信息数据')

    def push_top_list_button_clicked(self):
        model = model_qtableview._setToplistModel(self._get_top_list_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有' + self.selectData + '龙虎榜数据数据')

    def push_top_inst_button_clicked(self):
        model = model_qtableview._setTopInstModel(self._get_top_inst_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有' + self.selectData + '龙虎榜机构交易数据数据')

    def push_block_trade_button_clicked(self):
        model = model_qtableview._setBlockTradeModel(self._get_block_trade_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有' + self.selectData + '大宗交易数据数据')

    def push_button_moneyflow_clicked(self):
        model = model_qtableview._setmoneyflowModel(self._get_moneyflow_info())
        if model != 0:
            self.tableView.setModel(model)
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有' + self.selectData + '个股资金流向数据数据')

    def _get_moneyflow_info(self):
        sql = 'select * from moneyflow  ' + self.add_query_code_sql() + ' order BY ts_code  asc'
        return self._get_date_info(sql)

    def _get_daily_info(self):
        sql = 'select * from daily ' + self.add_query_code_sql() + ' order BY ts_code  asc'
        return self._get_date_info(sql)

    def _get_daily_basic_info(self):
        sql = 'select * from daily_basic ' + self.add_query_code_sql() + ' order BY ts_code  asc'
        return self._get_date_info(sql)

    def _get_stock_basic_info(self):
        sql = 'select * from stock_basic '
        return self._get_date_info(sql)

    def _get_company_info(self):
        sql = 'select * from stock_company '
        return self._get_date_info(sql)

    def _get_top_list_info(self):
        sql = 'select * from top_list ' + self.add_query_code_sql() + ' order BY ts_code  asc'
        return self._get_date_info(sql)

    def _get_top_inst_info(self):
        sql = 'select * from top_inst ' + self.add_query_code_sql() + ' order BY ts_code  asc'
        return self._get_date_info(sql)

    def _get_block_trade_info(self):
        sql = 'select * from block_trade ' + self.add_query_code_sql() + ' order BY ts_code  asc'
        return self._get_date_info(sql)

    def _get_date_info(self, sql):
        try:
            connectSQLite.DBCur.execute(sql)
            df = connectSQLite.DBCur.fetchall()
            connectSQLite.DBCon.commit()
        except:
            df = None
        return df

    def _upsdowns_show(self):
        self.upsdownsFm = upsdownsWindow()
        self.upsdownsFm.showMaximized()

    def _update_stock_basic_info_clicked(self):
        returnstr = getStockInfoSQLite.update_stockbasic_to_db()
        self._show_message_dialog(returnstr)

    def _update_company_info_clicked(self):
        returnstr = getStockInfoSQLite.update_company_info_to_db()
        self._show_message_dialog(returnstr)

    def _update_stock_daily_info_clicked(self):
        returnstr = getStockInfoSQLite.get_all_stock_daily_info()
        self._show_message_dialog(returnstr)

    def _update_stock_daily_basic_info_clicked(self):
        returnstr = getStockInfoSQLite.get_all_stock_daily_basic_info()
        self._show_message_dialog(returnstr)

    def _update_top_list_info_clicked(self):
        returnstr = getStockInfoSQLite.get_all_top_list_info()
        self._show_message_dialog(returnstr)

    def _update_top_inst_info_clicked(self):
        returnstr = getStockInfoSQLite.get_all_top_inst_info()
        self._show_message_dialog(returnstr)

    def _update_block_trade_info_clicked(self):
        returnstr = getStockInfoSQLite.get_all_block_trade_info()
        self._show_message_dialog(returnstr)

    def _update_moneyflow_info_clicked(self):
        returnstr = getStockInfoSQLite.get_all_moneyflow_info()
        self._show_message_dialog(returnstr)

    def _update_all_info_clicked(self):
        returnstr = getStockInfoSQLite.update_stock_info()
        self._show_message_dialog(returnstr)

    @staticmethod
    def _show_message_dialog(message='没有信息'):
        dialog = QDialog()
        label = QLabel(message, dialog)
        label.adjustSize()  # label自动根据内容变更大小
        label.setWordWrap(True)  # 设置自动换行
        label.move(50, 50)
        dialog.resize(label.size().width() + 200, label.size().height() + 200)
        dialog.setWindowTitle("提示")
        # 设置窗口的属性为ApplicationModal模态，用户只有关闭弹窗后，才能关闭主界面
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

    # 初始化comboBox和comboBox_top_code选项信息
    def _init_combobox_stock_name(self):
        sql = 'select * from stock_basic '
        try:
            sqliteCur = connectSQLite.DBCon.cursor()
            sqliteCur.execute(sql)
            result = sqliteCur.fetchall()
            if result == None:
                return
            else:
                for i in result:
                    self.stocknamelist.append(i[2])
                    self.stockcodelist.append(i[0])
                for j in range(len(self.stocknamelist)):
                    self.comboBox_stock_name.addItem(self.stocknamelist[j])
                self.comboBox_stock_name.setCurrentIndex(-1)
            sqliteCur.close()
        except:
            return

    # comboBox选择后自动填写ts_code到lineedit中
    def _on_combobox_stock_name_activate(self, index):
        self.lineEdit_stock_code.setText(self.stockcodelist[index])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    # myWin.show()
    myWin.showMaximized()

    app.exec_()
