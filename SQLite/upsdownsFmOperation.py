from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QLabel
import sys

from PyQt5.QtWidgets import QMenu

from SQLite import connectSQLite, model_qtableview

from UI.upsdownsFm import *


class upsdownsWindow(QMainWindow, Ui_UpsAndDownsWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self._init_combobox_code()
        self._init_comboBox_choice()
        self.comboBox_daily_name.activated.connect(self._on_combobox_code_activate)
        self.comboBox_top_name.activated.connect(self._on_combobox_top_code_activate)
        self.comboBox_moneyflow_name.activated.connect(self._on_combobox_moneyflow_code_activate)
        self.pushButton_add_query_info.clicked.connect(self._pushButton_add_query_info_clicked)

        self.pushButton_query.clicked.connect(self._pushButton_query_clicked)
        self.pushButton_add_top_query_info.clicked.connect(self._pushButton_add_top_query_info_clicked)
        self.pushButton_top_query.clicked.connect(self.pushButton_top_query_clicked)
        self.tabWidget.setCurrentIndex(0)
        # daily查询界面自动更新查询语句
        self.calendarWidget.selectionChanged.connect(self._pushButton_add_query_info_clicked)
        self.lineEdit_pct_chg.textChanged.connect(self._pushButton_add_query_info_clicked)
        self.lineEdit_turnover_rate.textChanged.connect(self._pushButton_add_query_info_clicked)
        self.lineEdit_pe.textChanged.connect(self._pushButton_add_query_info_clicked)
        self.lineEdit_vol.textChanged.connect(self._pushButton_add_query_info_clicked)
        self.lineEdit_daily_code.textChanged.connect(self._pushButton_add_query_info_clicked)
        self.comboBox_pct_chg.activated.connect(self._pushButton_add_query_info_clicked)
        self.comboBox_turnover_rate.activated.connect(self._pushButton_add_query_info_clicked)
        self.comboBox_vol.activated.connect(self._pushButton_add_query_info_clicked)
        self.comboBox_pe.activated.connect(self._pushButton_add_query_info_clicked)
        self.checkBox_daily_date_select.stateChanged.connect(self._pushButton_add_query_info_clicked)
        # 龙虎榜查询界面自动更新查询语句
        self.calendarWidget_top.selectionChanged.connect(self._pushButton_add_top_query_info_clicked)
        self.lineEdit_top_code.textChanged.connect(self._pushButton_add_top_query_info_clicked)
        self.lineEdit_top_pct_change.textChanged.connect(self._pushButton_add_top_query_info_clicked)
        self.lineEdit_top_net_amount.textChanged.connect(self._pushButton_add_top_query_info_clicked)
        self.lineEdit_top_l_amount.textChanged.connect(self._pushButton_add_top_query_info_clicked)
        self.lineEdit_top_turnover_rate.textChanged.connect(self._pushButton_add_top_query_info_clicked)
        self.lineEdit_top_amount_rate.textChanged.connect(self._pushButton_add_top_query_info_clicked)
        self.comboBox_top_name.activated.connect(self._pushButton_add_top_query_info_clicked)
        self.comboBox_top_amount_rate.activated.connect(self._pushButton_add_top_query_info_clicked)
        self.comboBox_top_net_amount.activated.connect(self._pushButton_add_top_query_info_clicked)
        self.comboBox_top_l_amount.activated.connect(self._pushButton_add_top_query_info_clicked)
        self.comboBox_top_pct_change.activated.connect(self._pushButton_add_top_query_info_clicked)
        # 资金流自动更新查询语句
        self.pushButton_add_moneyflow_query.clicked.connect(self._pushButton_add_moneyflow_query_clicked)
        self.lineEdit_moneyflow_code.textChanged.connect(self._pushButton_add_moneyflow_query_clicked)
        self.checkBox_moneyflow_date_select.stateChanged.connect(self._pushButton_add_moneyflow_query_clicked)
        self.calendarWidget_moneyflow.selectionChanged.connect(self._pushButton_add_moneyflow_query_clicked)
        self.pushButton_moneyflow_query.clicked.connect(self.pushButton_moneyflow_query_clicked)
        self.checkBox_high_light_net_positive.stateChanged.connect(self._checkBox_high_light_net_positive_clicked)

        # 申明tableview的右键菜单功能
        # self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tableView.customContextMenuRequested.connect(self.showContextMenu)

    # 类内变量
    stocknamelist = []  # 记录股票名称信息
    stockcodelist = []  # 记录股票代码信息
    top_model: QtGui.QStandardItemModel = None  # 记录当前tableview中的mode
    daily_model: QtGui.QStandardItemModel = None  # 记录当前tableview中的model
    moneyflow_model: QtGui.QStandardItemModel = None  # 记录当前tableview中的model

    sql_str_code = ''  # 用来记录添加到query的code语句，方便修改删除，下面几个变量作用相同
    sql_str_pe = ''
    sql_str_turnover_rate = ''
    sql_str_pct_chg = ''
    sql_str_vol = ''
    sql_str_date = ''
    daily_query_sql: str = 'select * from daily where'  # 用来记录查询语句的
    sub_daily_query_sql: str = ' and ts_code in ( select ts_code from  daily_basic where'  # 用来子查询的语句

    sql_top_code = ''  # 用来记录添加到query的code语句，方便修改删除，下面几个变量作用相同
    sql_top_l_amount = ''  # 龙虎榜交易总额
    sql_top_turnover_rate = ''
    sql_top_pct_change = ''
    sql_top_net_amount = ''  # 龙虎榜净买入额
    sql_top_amount_rate = ''  # 龙虎榜成交占比
    sql_top_date = ''
    top_query_sql: str = 'select * from top_list where'
    sql_order_by_trade_date = ' order by trade_date desc'

    sql_money_code = ''
    sql_money_date = ''
    money_query_sql: str = 'select * from moneyflow '

    combobox_item = ['>', '>=', '=', '<', '<=']

    # daily页面相关操作函数
    def _lineEdit_stock_code_name_changed(self):
        tmpsql = ''
        if self.lineEdit_daily_code.text() != '':
            if 'where' != self.daily_query_sql[
                          len(self.daily_query_sql) - 5:len(
                              self.daily_query_sql)]:  # 如果query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' daily.ts_code=\'' + self.lineEdit_daily_code.text() + '\''
            self.sql_str_code = tmpsql  # 预留
        return tmpsql

    def _lineEidt_pct_chg_changed(self):
        tmpsql = ''
        if self.lineEdit_pct_chg.text() != '':
            if 'where' != self.daily_query_sql[
                          len(self.daily_query_sql) - 5:len(
                              self.daily_query_sql)]:  # 如果query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' daily.pct_chg' + self.comboBox_pct_chg.currentText() + self.lineEdit_pct_chg.text()
            self.sql_str_pct_chg = tmpsql
        return tmpsql

    def _lineEdit_vol_changed(self):
        tmpsql = ''
        if self.lineEdit_vol.text() != '':
            if 'where' != self.daily_query_sql[
                          len(self.daily_query_sql) - 5:len(
                              self.daily_query_sql)]:  # 如果query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' daily.vol' + self.comboBox_vol.currentText() + self.lineEdit_vol.text()
            self.sql_str_vol = tmpsql
        return tmpsql

    def _set_sub_query_str(self):
        tmp = ''
        tmp2 = ''
        sql = ''
        self.sub_daily_query_sql = ' and ts_code in ( select ts_code from  daily_basic where'
        if (self.lineEdit_pe.text() == '') and (self.lineEdit_turnover_rate.text() == ''):
            self.sub_daily_query_sql = ''
        else:
            if 'where' == self.daily_query_sql[
                          len(self.daily_query_sql) - 5:len(
                              self.daily_query_sql)]:  # 如果query_sql最后是‘where’注意没有空格,删除sub_query_sql前面的and
                self.sub_daily_query_sql = self.sub_daily_query_sql.replace(' and', '')
            tmp += self._lineEdit_turnover_rate_changed()
            self.sub_daily_query_sql += tmp
            tmp2 += self._lineEdit_pe_changed()
            self.sub_daily_query_sql += tmp2
            sql = self.sub_daily_query_sql
        return sql

    def _lineEdit_pe_changed(self):
        tmpsql = ''
        if self.lineEdit_pe.text() != '':
            if 'where' != self.sub_daily_query_sql[
                          len(self.sub_daily_query_sql) - 5:len(
                              self.sub_daily_query_sql)]:  # 如果sub_query_sql最后不是‘where’注意没有空格,前面多加一个and
                self.sub_daily_query_sql = self.sub_daily_query_sql.rstrip(')')  # 先删除）括号
                tmpsql += ' and '

            tmpsql += ' daily_basic.pe' + self.comboBox_pe.currentText() + self.lineEdit_pe.text() + ')'
            self.sql_str_pe = tmpsql
        return tmpsql

    def _lineEdit_turnover_rate_changed(self):
        tmpsql = ''
        if self.lineEdit_turnover_rate.text() != '':
            if 'where' != self.sub_daily_query_sql[
                          len(self.sub_daily_query_sql) - 5:len(
                              self.sub_daily_query_sql)]:  # 如果sub_query_sql最后不是‘where’注意没有空格,前面多加一个and
                self.sub_daily_query_sql = self.sub_daily_query_sql.rstrip(')')  # 先删除）括号
                tmpsql += ' and '
            tmpsql += ' daily_basic.turnover_rate' + self.comboBox_turnover_rate.currentText() + self.lineEdit_turnover_rate.text() + ')'
            self.sql_str_turnover_rate = tmpsql
        return tmpsql

    def _calendarWidget_clicked(self):
        tmpsql = ''
        select_date = self.calendarWidget.selectedDate().toString(Qt.ISODate).replace('-', '')  # 获取选中日期
        if 'where' != self.daily_query_sql[
                      len(self.daily_query_sql) - 5:len(
                          self.daily_query_sql)]:  # 如果query_sql最后不是‘where’注意没有空格,前面多加一个and
            tmpsql += ' and '
        tmpsql += ' daily.trade_date=\'' + select_date + '\''
        self.sql_str_date = tmpsql
        return tmpsql

    def _checkbox_daily_state_change_clicked(self):
        # 删除时间信息后如果最后为where，则继续删除where
        if 'where' == self.daily_query_sql[
                      len(self.daily_query_sql) - 5:len(
                          self.daily_query_sql)]:  # 如果query_sql最后是‘where’删除
            self.daily_query_sql = self.daily_query_sql.replace('where', '')

    def _pushButton_add_query_info_clicked(self):
        self.daily_query_sql = 'select * from daily where'  # 每次都初始化
        self.daily_query_sql += self._lineEdit_stock_code_name_changed()
        self.daily_query_sql += self._lineEidt_pct_chg_changed()
        self.daily_query_sql += self._lineEdit_vol_changed()
        self.daily_query_sql += self._set_sub_query_str()
        if self.checkBox_daily_date_select.isChecked():
            self.daily_query_sql += self._calendarWidget_clicked()
        else:
            self._checkbox_daily_state_change_clicked()
        self.daily_query_sql += ' order by trade_date desc'
        self.textEdit_SQL.setPlainText(self.daily_query_sql)

    def _pushButton_query_clicked(self):
        sql = self.textEdit_SQL.toPlainText()
        if sql == '':
            return
        model = model_qtableview._setDailyModel(self._get_data_info(self.textEdit_SQL.toPlainText()))
        if model != 0:
            self.tableView_daily.setModel(model)
            self.tableView_daily.resizeColumnsToContents()
            self.daily_model = model
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog(
                '没有' + self.calendarWidget.selectedDate().toString(Qt.ISODate).replace('-', '') + '数据')

    # 龙虎榜查询
    def _lineEdit_top_code_changed(self):
        tmpsql = ''
        if self.lineEdit_top_code.text() != '':
            if 'where' != self.top_query_sql[
                          len(self.top_query_sql) - 5:len(
                              self.top_query_sql)]:  # 如果top_query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' ts_code=\'' + self.lineEdit_top_code.text() + '\''
        self.sql_top_code = tmpsql  # 先设置一下，按目前思路不需要
        return tmpsql

    def _lineEdit_top_pct_chg_changed(self):
        tmpsql = ''
        if self.lineEdit_top_pct_change.text() != '':
            if 'where' != self.top_query_sql[
                          len(self.top_query_sql) - 5:len(
                              self.top_query_sql)]:  # 如果top_query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' pct_change ' + self.comboBox_top_pct_change.currentText() + ' ' + self.lineEdit_top_pct_change.text()
        self.sql_top_pct_change = tmpsql  # 先设置一下，按目前思路不需要
        return tmpsql

    def _lineEdit_top_turnover_rate_changed(self):
        tmpsql = ''
        if self.lineEdit_top_turnover_rate.text() != '':
            if 'where' != self.top_query_sql[
                          len(self.top_query_sql) - 5:len(
                              self.top_query_sql)]:  # 如果top_query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' turnover_rate ' + self.comboBox_top_turnover_rate.currentText() + ' ' + self.lineEdit_top_turnover_rate.text()
        self.sql_top_turnover_rate = tmpsql  # 先设置一下，按目前思路不需要
        return tmpsql

    def _lineEdit_top_l_amount_changed(self):
        tmpsql = ''
        if self.lineEdit_top_l_amount.text() != '':
            if 'where' != self.top_query_sql[
                          len(self.top_query_sql) - 5:len(
                              self.top_query_sql)]:  # 如果top_query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' l_amount ' + self.comboBox_top_l_amount.currentText() + ' ' + self.lineEdit_top_l_amount.text()
        self.sql_top_l_amount = tmpsql  # 先设置一下，按目前思路不需要
        return tmpsql

    def _lineEdit_top_net_amount_changed(self):
        tmpsql = ''
        if self.lineEdit_top_net_amount.text() != '':
            if 'where' != self.top_query_sql[
                          len(self.top_query_sql) - 5:len(
                              self.top_query_sql)]:  # 如果top_query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' net_amount ' + self.comboBox_top_net_amount.currentText() + ' ' + self.lineEdit_top_net_amount.text()
        self.sql_top_net_amount = tmpsql  # 先设置一下，按目前思路不需要
        return tmpsql

    def _lineEdit_top_amount_rate_changed(self):
        tmpsql = ''
        if self.lineEdit_top_amount_rate.text() != '':
            if 'where' != self.top_query_sql[
                          len(self.top_query_sql) - 5:len(
                              self.top_query_sql)]:  # 如果top_query_sql最后不是‘where’注意没有空格,前面多加一个and
                tmpsql += ' and '
            tmpsql += ' amount_rate ' + self.comboBox_top_amount_rate.currentText() + ' ' + self.lineEdit_top_amount_rate.text()
        self.sql_top_amount_rate = tmpsql  # 先设置一下，按目前思路不需要
        return tmpsql

    def _calendarWidget_top_changed(self):
        tmpsql = ''
        select_date = self.calendarWidget_top.selectedDate().toString(Qt.ISODate).replace('-', '')  # 获取选中日期
        if 'where' != self.top_query_sql[
                      len(self.top_query_sql) - 5:len(
                          self.top_query_sql)]:  # 如果query_sql最后不是‘where’注意没有空格,前面多加一个and
            tmpsql += ' and '
        tmpsql += ' trade_date=\'' + select_date + '\''
        self.sql_top_date = tmpsql
        return tmpsql

    def _pushButton_add_top_query_info_clicked(self):
        self.top_query_sql = 'select * from top_list where'  # 每次都初始化
        self.top_query_sql += self._lineEdit_top_code_changed()
        self.top_query_sql += self._lineEdit_top_pct_chg_changed()
        self.top_query_sql += self._lineEdit_top_turnover_rate_changed()
        self.top_query_sql += self._lineEdit_top_l_amount_changed()
        self.top_query_sql += self._lineEdit_top_net_amount_changed()
        self.top_query_sql += self._lineEdit_top_amount_rate_changed()
        self.top_query_sql += self._calendarWidget_top_changed()
        self.textEdit_top_SQL.setText(self.top_query_sql)

    def pushButton_top_query_clicked(self):
        sql = self.textEdit_top_SQL.toPlainText()
        if sql == '':
            return
        model = model_qtableview._setToplistModel(self._get_data_info(self.textEdit_top_SQL.toPlainText()))
        if model != 0:
            self.tableView_top.setModel(model)
            self.tableView_top.resizeColumnsToContents()
            self.top_model = model
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有龙虎榜数据')

    # 资金流查询
    def _pushButton_add_moneyflow_query_clicked(self):
        sql = ''
        select_date = self.calendarWidget_moneyflow.selectedDate().toString(Qt.ISODate).replace('-', '')  # 获取选中日期
        ts_code = self.lineEdit_moneyflow_code.text()
        if ts_code == '':
            if self.checkBox_moneyflow_date_select.isChecked():
                sql += ' where trade_date=\'' + select_date + '\''
        else:
            if self.checkBox_moneyflow_date_select.isChecked():
                sql += ' where ts_code=\'' + ts_code + '\'' + ' and  trade_date=\'' + select_date + '\''
            else:
                sql += ' where ts_code=\'' + ts_code + '\''

        sql = self.money_query_sql + sql
        self.textEdit_moneyflow_SQL.setText(sql)

    def pushButton_moneyflow_query_clicked(self):
        sql = self.textEdit_moneyflow_SQL.toPlainText()
        if sql == '':
            return
        model = model_qtableview._setmoneyflowModel(self._get_data_info(self.textEdit_moneyflow_SQL.toPlainText()))
        if model != 0:
            self.tableView_moneyflow.setModel(model)
            self.tableView_moneyflow.resizeColumnsToContents()
            self.moneyflow_model = model
            self._checkBox_high_light_net_positive_clicked()
        else:  # TODO:弹出对话框说明无数据
            self._show_message_dialog('没有资金流向数据')

    def _checkBox_high_light_net_positive_clicked(self):
        if self.checkBox_high_light_net_positive.isChecked():
            if self.moneyflow_model is None:
                return
            model = self.moneyflow_model
            row = model.rowCount()
            vol = model.columnCount()
            # moneyflow的列有20个,特大单卖出额，买入额分别17，15，大单卖出额，买入额为13，11

            for i in range(row):
                if float(model.item(i, 11).text()) > float(model.item(i, 13).text()):
                    model.item(i, 11).setBackground(QColor(255, 0, 0))

                if float(model.item(i, 15).text()) > float(model.item(i, 17).text()):
                    model.item(i, 15).setBackground(QColor(255, 0, 0))

    """
    公共函数
    """

    # 初始化comboBox和comboBox_top_code选项信息
    def _init_combobox_code(self):
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
                    self.comboBox_daily_name.addItem(self.stocknamelist[j])
                    self.comboBox_top_name.addItem(self.stocknamelist[j])
                    self.comboBox_moneyflow_name.addItem(self.stocknamelist[j])
                self.comboBox_daily_name.setCurrentIndex(-1)
                self.comboBox_top_name.setCurrentIndex(-1)
                self.comboBox_moneyflow_name.setCurrentIndex(-1)
            sqliteCur.close()
        except:
            return

    # 添加<=>号
    def _init_comboBox_choice(self):
        self.comboBox_pct_chg.addItems(self.combobox_item)
        self.comboBox_pe.addItems(self.combobox_item)
        self.comboBox_turnover_rate.addItems(self.combobox_item)
        self.comboBox_vol.addItems(self.combobox_item)
        self.comboBox_top_amount_rate.addItems(self.combobox_item)
        self.comboBox_top_l_amount.addItems(self.combobox_item)
        self.comboBox_top_net_amount.addItems(self.combobox_item)
        self.comboBox_top_turnover_rate.addItems(self.combobox_item)
        self.comboBox_top_pct_change.addItems(self.combobox_item)

    # comboBox选择后自动填写ts_code到lineedit中
    def _on_combobox_code_activate(self, index):
        self.lineEdit_daily_code.setText(self.stockcodelist[index])

    def _on_combobox_top_code_activate(self, index):
        self.lineEdit_top_code.setText(self.stockcodelist[index])

    def _on_combobox_moneyflow_code_activate(self, index):
        self.lineEdit_moneyflow_code.setText(self.stockcodelist[index])

    @staticmethod
    def _get_data_info(sql):
        try:
            connectSQLite.DBCur.execute(sql)
            df = connectSQLite.DBCur.fetchall()
            connectSQLite.DBCon.commit()
        except:
            df = None
        return df

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

    """
    实现tableview右键菜单功能
    """
    # def showContextMenu(self):  # 创建右键菜单
    #     self.tableView.contextMenu = QMenu(self)
    #     self.actionA = self.tableView.contextMenu.addAction(u'动作a')
    #     # self.actionA = self.view.contextMenu.exec_(self.mapToGlobal(pos))  # 1
    #     self.tableView.contextMenu.popup(QCursor.pos())  # 2菜单显示的位置
    #     self.actionA.triggered.connect(self.actionHandler)
    #     # self.view.contextMenu.move(self.pos())  # 3
    #     self.tableView.contextMenu.show()
    #
    # def actionHandler(self):
    #     self._show_message_dialog('测试成功')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = upsdownsWindow()
    myWin.showMaximized()

    app.exec_()
