# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1939, 1362)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setMinimumSize(QtCore.QSize(380, 0))
        self.tableView.setBaseSize(QtCore.QSize(380, 0))
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.checkBox_select_date = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_select_date.setChecked(True)
        self.checkBox_select_date.setObjectName("checkBox_select_date")
        self.verticalLayout.addWidget(self.checkBox_select_date)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox_stock_name = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_stock_name.sizePolicy().hasHeightForWidth())
        self.comboBox_stock_name.setSizePolicy(sizePolicy)
        self.comboBox_stock_name.setMinimumSize(QtCore.QSize(60, 0))
        self.comboBox_stock_name.setEditable(True)
        self.comboBox_stock_name.setCurrentText("")
        self.comboBox_stock_name.setObjectName("comboBox_stock_name")
        self.horizontalLayout_3.addWidget(self.comboBox_stock_name)
        self.lineEdit_stock_code = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_stock_code.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_stock_code.sizePolicy().hasHeightForWidth())
        self.lineEdit_stock_code.setSizePolicy(sizePolicy)
        self.lineEdit_stock_code.setReadOnly(True)
        self.lineEdit_stock_code.setObjectName("lineEdit_stock_code")
        self.horizontalLayout_3.addWidget(self.lineEdit_stock_code)
        self.pushButton_delete_code = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_delete_code.sizePolicy().hasHeightForWidth())
        self.pushButton_delete_code.setSizePolicy(sizePolicy)
        self.pushButton_delete_code.setObjectName("pushButton_delete_code")
        self.horizontalLayout_3.addWidget(self.pushButton_delete_code)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.pushDailyButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushDailyButton.setObjectName("pushDailyButton")
        self.verticalLayout.addWidget(self.pushDailyButton)
        self.pushDailyBasicButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushDailyBasicButton.setObjectName("pushDailyBasicButton")
        self.verticalLayout.addWidget(self.pushDailyBasicButton)
        self.pushToplistButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushToplistButton.setObjectName("pushToplistButton")
        self.verticalLayout.addWidget(self.pushToplistButton)
        self.pushTopInstButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushTopInstButton.setObjectName("pushTopInstButton")
        self.verticalLayout.addWidget(self.pushTopInstButton)
        self.pushBlockTradeButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushBlockTradeButton.setFlat(False)
        self.pushBlockTradeButton.setObjectName("pushBlockTradeButton")
        self.verticalLayout.addWidget(self.pushBlockTradeButton)
        self.pushButton_moneyflow = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_moneyflow.setFlat(False)
        self.pushButton_moneyflow.setObjectName("pushButton_moneyflow")
        self.verticalLayout.addWidget(self.pushButton_moneyflow)
        self.pushStockBasicButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushStockBasicButton.setObjectName("pushStockBasicButton")
        self.verticalLayout.addWidget(self.pushStockBasicButton)
        self.pushCompanyButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushCompanyButton.setObjectName("pushCompanyButton")
        self.verticalLayout.addWidget(self.pushCompanyButton)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1939, 45))
        self.menubar.setObjectName("menubar")
        self.menu_query = QtWidgets.QMenu(self.menubar)
        self.menu_query.setObjectName("menu_query")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_ups_and_downs = QtWidgets.QAction(MainWindow)
        self.action_ups_and_downs.setObjectName("action_ups_and_downs")
        self.action_update_daily_info = QtWidgets.QAction(MainWindow)
        self.action_update_daily_info.setObjectName("action_update_daily_info")
        self.action_update_daily_basic_info = QtWidgets.QAction(MainWindow)
        self.action_update_daily_basic_info.setObjectName("action_update_daily_basic_info")
        self.action_update_top_list_info = QtWidgets.QAction(MainWindow)
        self.action_update_top_list_info.setObjectName("action_update_top_list_info")
        self.action_update_top_inst_info = QtWidgets.QAction(MainWindow)
        self.action_update_top_inst_info.setObjectName("action_update_top_inst_info")
        self.action_update_block_trade_info = QtWidgets.QAction(MainWindow)
        self.action_update_block_trade_info.setObjectName("action_update_block_trade_info")
        self.action_update_moneyflow_info = QtWidgets.QAction(MainWindow)
        self.action_update_moneyflow_info.setObjectName("action_update_moneyflow_info")
        self.action_update_all_info = QtWidgets.QAction(MainWindow)
        self.action_update_all_info.setObjectName("action_update_all_info")
        self.action_update_stock_basic_info = QtWidgets.QAction(MainWindow)
        self.action_update_stock_basic_info.setObjectName("action_update_stock_basic_info")
        self.action_update_company_info = QtWidgets.QAction(MainWindow)
        self.action_update_company_info.setObjectName("action_update_company_info")
        self.menu_query.addAction(self.action_ups_and_downs)
        self.menu.addAction(self.action_update_daily_info)
        self.menu.addAction(self.action_update_daily_basic_info)
        self.menu.addAction(self.action_update_top_list_info)
        self.menu.addAction(self.action_update_top_inst_info)
        self.menu.addAction(self.action_update_block_trade_info)
        self.menu.addAction(self.action_update_moneyflow_info)
        self.menu.addAction(self.action_update_stock_basic_info)
        self.menu.addAction(self.action_update_company_info)
        self.menu.addSeparator()
        self.menu.addAction(self.action_update_all_info)
        self.menubar.addAction(self.menu_query.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox_stock_name.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox_select_date.setToolTip(_translate("MainWindow", "勾选后，将查询选定日期数据"))
        self.checkBox_select_date.setText(_translate("MainWindow", "按选定日期查询"))
        self.groupBox_3.setTitle(_translate("MainWindow", "选择具体股票"))
        self.comboBox_stock_name.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>1</p><p>2</p><p>3</p><p>4</p><p>5</p><p><br/></p></body></html>"))
        self.lineEdit_stock_code.setToolTip(_translate("MainWindow", "<html><head/><body><p>请输入完整的股票代码或者股票名称</p></body></html>"))
        self.pushButton_delete_code.setText(_translate("MainWindow", "删除"))
        self.pushDailyButton.setText(_translate("MainWindow", "查看股票交易信息"))
        self.pushDailyBasicButton.setText(_translate("MainWindow", "查看股票指标信息"))
        self.pushToplistButton.setText(_translate("MainWindow", "查看龙虎榜信息"))
        self.pushTopInstButton.setText(_translate("MainWindow", "查看龙虎榜机构交易信息"))
        self.pushBlockTradeButton.setText(_translate("MainWindow", "查看大宗交易信息"))
        self.pushButton_moneyflow.setText(_translate("MainWindow", "查看个股资金流向信息"))
        self.pushStockBasicButton.setText(_translate("MainWindow", "查看股票基本信息"))
        self.pushCompanyButton.setText(_translate("MainWindow", "查看公司基本信息"))
        self.menu_query.setTitle(_translate("MainWindow", "具体查询"))
        self.menu.setTitle(_translate("MainWindow", "数据更新"))
        self.action_ups_and_downs.setText(_translate("MainWindow", "涨跌查询"))
        self.action_ups_and_downs.setToolTip(_translate("MainWindow", "涨跌查询"))
        self.action_ups_and_downs.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.action_update_daily_info.setText(_translate("MainWindow", "更新每日交易信息"))
        self.action_update_daily_basic_info.setText(_translate("MainWindow", "更新每日指标信息"))
        self.action_update_top_list_info.setText(_translate("MainWindow", "更新龙虎榜信息"))
        self.action_update_top_inst_info.setText(_translate("MainWindow", "更新龙虎榜机构信息"))
        self.action_update_block_trade_info.setText(_translate("MainWindow", "更新大宗交易信息"))
        self.action_update_moneyflow_info.setText(_translate("MainWindow", "更新个股资金流向信息"))
        self.action_update_all_info.setText(_translate("MainWindow", "更新所有信息"))
        self.action_update_all_info.setToolTip(_translate("MainWindow", "更新所有信息"))
        self.action_update_stock_basic_info.setText(_translate("MainWindow", "更新股票基本信息"))
        self.action_update_company_info.setText(_translate("MainWindow", "更新上市公司信息"))

