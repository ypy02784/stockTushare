from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from SQLite import connectSQLite

from UI.upsdownsFm import *

class upsdownsWindow(QMainWindow,Ui_UpsAndDownsWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self._init_combobox()
        self.comboBox.activated.connect(self._on_combobox_activate)
        self.textEdit_SQL.setText(self.query_sql)
        self.pushButton_daily.clicked.connect(self.pushbutton_daily_clicked)
        self.pushButton_dailybasic.clicked.connect(self.pushbutton_daily_basic_clicked)

    stocknamelist = []#记录股票名称信息
    stockcodelist = []#记录股票代码信息
    query_sql: str ='select * from daily where '#用来记录查询语句的

    #初始化comboBox选项信息
    def _init_combobox(self):
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
                    self.comboBox.addItem(self.stocknamelist[j])
                self.comboBox.setCurrentIndex(-1)
        except:
            return
        finally:
            sqliteCur.close()

    #comboBox选择后自动填写ts_code到lineedit中
    def _on_combobox_activate(self, index):
        self.lineEdit_stock_code_name.setText(self.stockcodelist[index])

    def pushbutton_daily_clicked(self):
        if self.lineEdit_stock_code_name.text() != '' :
            if not ('ts_code' in self.query_sql ):
                if 'where ' != self.query_sql[len(self.query_sql) - 6:len(self.query_sql)]:
                    self.query_sql = self.query_sql + ' and '
                self.query_sql = self.query_sql + ' daily.ts_code=\''+self.lineEdit_stock_code_name.text()+'\''

        if self.lineEdit_ptc_chg.text() != '':
            if not ('ptc_chg' in self.query_sql):
                if not self.query_sql[len(self.query_sql) - 6:len(self.query_sql)] == 'where ':
                    self.query_sql = self.query_sql + ' and '
                self.query_sql = self.query_sql + ' daily.ptc_chg>\''+self.lineEdit_ptc_chg.text()+'\''

        if self.lineEdit_vol.text() != '':
            if not ('vol' in self.query_sql):
                if not self.query_sql[len(self.query_sql) - 6:len(self.query_sql)] == 'where ':
                    self.query_sql = self.query_sql + ' and '
            self.query_sql = self.query_sql + ' daily.vol>\''+self.lineEdit_vol.text()+'\''
        self.textEdit_SQL.setText(self.query_sql)

    def pushbutton_daily_basic_clicked(self):

        if self.lineEdit_pe.text()!= '':
            if not ('daily_basic.pe' in self.query_sql):
                if self.query_sql[len(self.query_sql) - 6:len(self.query_sql) ] != 'where ':
                    self.query_sql = self.query_sql + ' and '
                self.query_sql = self.query_sql + ' daily_basic.pe<\'' + self.lineEdit_pe.text() + '\''

        if self.lineEdit_turnover_rate.text() != '':
            if not ('daily_basic.turnover_rate' in self.query_sql):
                if self.query_sql[len(self.query_sql) - 6:len(self.query_sql) ] != 'where ':
                    self.query_sql = self.query_sql + ' and '

                self.query_sql = self.query_sql + ' daily_basic.turnover_rate>\'' + self.lineEdit_turnover_rate.text() + '\''

        self.textEdit_SQL.setText(self.query_sql)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     myWin = upsdownsWindow()
#     myWin.show()
#
#     app.exec_()
