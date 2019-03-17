from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from SQLite import connectSQLite

from UI.upsdownsFm import *


class upsdownsWindow(QMainWindow, Ui_UpsAndDownsWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self._init_combobox_code()
        self._init_comboBox_choice()
        self.comboBox_code.activated.connect(self._on_combobox_code_activate)
        self.textEdit_SQL.setText(self.query_sql)
        self.pushButton_add_query_info.clicked.connect(self._pushButton_add_query_info_clicked)
        # self.pushButton_daily.clicked.connect(self.pushbutton_daily_clicked)
        # self.pushButton_dailybasic.clicked.connect(self.pushbutton_daily_basic_clicked)

    stocknamelist = []  # 记录股票名称信息
    stockcodelist = []  # 记录股票代码信息

    sql_str_code = ''  # 用来记录添加到query的code语句，方便修改删除，下面几个变量作用相同
    sql_str_pe = ''
    sql_str_turnover_rate = ''
    sql_str_pct_chg = ''
    sql_str_vol = ''
    combobox_item = ['>', '=', '<']

    query_sql: str = 'select * from daily where'  # 用来记录查询语句的
    sub_query_sql: str = ' and ts_code in ( select ts_code from  daily_basic where' #用来子查询的语句

    # 初始化comboBox选项信息
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
                    self.comboBox_code.addItem(self.stocknamelist[j])
                self.comboBox_code.setCurrentIndex(-1)
            sqliteCur.close()
        except:
            return

    # 添加<=>号
    def _init_comboBox_choice(self):
        self.comboBox_pct_chg.addItems(self.combobox_item)
        self.comboBox_pe.addItems(self.combobox_item)
        self.comboBox_turnover_rate.addItems(self.combobox_item)
        self.comboBox_vol.addItems(self.combobox_item)

    # comboBox选择后自动填写ts_code到lineedit中
    def _on_combobox_code_activate(self, index):
        self.lineEdit_stock_code_name.setText(self.stockcodelist[index])

    def _lineEdit_stock_code_name_changed(self):
        # if 'ts_code' in self.query_sql:
        #     # 首先删除query_sql中的有关ts_code数据
        #     self.query_sql = self.query_sql.replace(self.sql_str_code, '')
        if self.lineEdit_stock_code_name.text() != '':
            self.sql_str_code = ''
            if 'where' != self.query_sql[
                          len(self.query_sql) - 5:len(self.query_sql)]:  # 如果query_sql最后不是‘where’注意没有空格,前面多加一个and
                self.sql_str_code += ' and '
            self.sql_str_code += ' daily.ts_code=\'' + self.lineEdit_stock_code_name.text() + '\''
            self.query_sql += self.sql_str_code

    def _lineEidt_pct_chg_changed(self):
        # if 'pct_chg' in self.query_sql:
        #     # 首先删除query_sql中的有关ts_code数据
        #     self.query_sql = self.query_sql.replace(self.sql_str_ptc_chg, '')
        if self.lineEdit_pct_chg.text() != '':
            self.sql_str_pct_chg = ''
            if 'where' != self.query_sql[
                          len(self.query_sql) - 5:len(self.query_sql)]:  # 如果query_sql最后不是‘where’注意没有空格,前面多加一个and
                self.sql_str_pct_chg += ' and '
            self.sql_str_pct_chg += ' daily.pct_chg' + self.comboBox_pct_chg.currentText() + self.lineEdit_pct_chg.text()
            self.query_sql += self.sql_str_pct_chg

    def _lineEdit_vol_changed(self):
        # if 'vol' in self.query_sql:
        #     # 首先删除query_sql中的有关vol数据
        #     self.query_sql = self.query_sql.replace(self.sql_str_vol, '')
        if self.lineEdit_vol.text() != '':
            self.sql_str_vol = ''
            if 'where' != self.query_sql[
                          len(self.query_sql) - 5:len(self.query_sql)]:  # 如果query_sql最后不是‘where’注意没有空格,前面多加一个and
                self.sql_str_vol += ' and '
            self.sql_str_vol += ' daily.vol' + self.comboBox_vol.currentText() + self.lineEdit_vol.text()
            self.query_sql += self.sql_str_vol

    def _set_sub_query_str(self):
        self.sub_query_sql = ' and ts_code in ( select ts_code from  daily_basic where'
        if (self.lineEdit_pe.text() == '')and(self.lineEdit_turnover_rate.text()==''):
            self.sub_query_sql = ''
        else:
            if 'where' == self.query_sql[
                          len(self.query_sql) - 5:len(self.query_sql)]:  # 如果query_sql最后是‘where’注意没有空格,删除sub_query_sql前面的and
                self.sub_query_sql = self.sub_query_sql.replace(' and', '')

            self._lineEdit_pe_changed()
            self._lineEdit_turnover_rate_changed()

    def _lineEdit_pe_changed(self):
        # if 'daily_basic.pe' in self.query_sql:
        #     # 首先删除query_sql中的有关vol数据
        #     self.query_sql = self.query_sql.replace(self.sql_str_pe, '')
        if self.lineEdit_pe.text() != '':
            self.sql_str_pe = ''
            if 'where' != self.sub_query_sql[
                          len(self.sub_query_sql) - 5:len(self.sub_query_sql)]:  # 如果sub_query_sql最后不是‘where’注意没有空格,前面多加一个and
                self.sub_query_sql = self.sub_query_sql.rstrip(')')#先删除）括号
                self.sql_str_pe += ' and '


            self.sql_str_pe += ' daily_basic.pe' + self.comboBox_pe.currentText() + self.lineEdit_pe.text()+')'
            self.sub_query_sql +=self.sql_str_pe

    def _lineEdit_turnover_rate_changed(self):
        # if 'daily_basic.turnover_rate' in self.query_sql:
        #     # 首先删除query_sql中的有关vol数据
        #     self.query_sql = self.query_sql.replace(self.sql_str_turnover_rate, '')
        if self.lineEdit_turnover_rate.text() != '':
            self.sql_str_turnover_rate = ''
            if 'where' != self.sub_query_sql[
                          len(self.sub_query_sql) - 5:len(
                              self.sub_query_sql)]:  # 如果sub_query_sql最后不是‘where’注意没有空格,前面多加一个and
                self.sub_query_sql = self.sub_query_sql.rstrip(')')  # 先删除）括号
                self.sql_str_turnover_rate += ' and '
            self.sql_str_turnover_rate += ' daily_basic.turnover_rate' + self.comboBox_turnover_rate.currentText() + self.lineEdit_turnover_rate.text()+')'
            self.sub_query_sql += self.sql_str_turnover_rate

    def _pushButton_add_query_info_clicked(self):
        self.query_sql = 'select * from daily where'#每次都初始化
        self._lineEdit_stock_code_name_changed()
        self._lineEidt_pct_chg_changed()
        self._lineEdit_vol_changed()

        self._set_sub_query_str()
        self.textEdit_SQL.setText(self.query_sql+self.sub_query_sql)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = upsdownsWindow()
    myWin.show()

    app.exec_()
