# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\study\github\stockTushare\UI\mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 100))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.basicinfofarme = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basicinfofarme.sizePolicy().hasHeightForWidth())
        self.basicinfofarme.setSizePolicy(sizePolicy)
        self.basicinfofarme.setFrameShape(QtWidgets.QFrame.Panel)
        self.basicinfofarme.setFrameShadow(QtWidgets.QFrame.Raised)
        self.basicinfofarme.setObjectName("basicinfofarme")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.basicinfofarme)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.basicinfofarme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMinimumDate(QtCore.QDate(2011, 1, 1))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2030, 12, 31))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.pushDailyButton = QtWidgets.QPushButton(self.basicinfofarme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushDailyButton.sizePolicy().hasHeightForWidth())
        self.pushDailyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(11)
        self.pushDailyButton.setFont(font)
        self.pushDailyButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushDailyButton.setCheckable(False)
        self.pushDailyButton.setDefault(False)
        self.pushDailyButton.setFlat(False)
        self.pushDailyButton.setObjectName("pushDailyButton")
        self.verticalLayout.addWidget(self.pushDailyButton)
        self.pushDailyBasicButton = QtWidgets.QPushButton(self.basicinfofarme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushDailyBasicButton.sizePolicy().hasHeightForWidth())
        self.pushDailyBasicButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(11)
        self.pushDailyBasicButton.setFont(font)
        self.pushDailyBasicButton.setObjectName("pushDailyBasicButton")
        self.verticalLayout.addWidget(self.pushDailyBasicButton)
        self.pushStockBasicButton = QtWidgets.QPushButton(self.basicinfofarme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushStockBasicButton.sizePolicy().hasHeightForWidth())
        self.pushStockBasicButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(11)
        self.pushStockBasicButton.setFont(font)
        self.pushStockBasicButton.setObjectName("pushStockBasicButton")
        self.verticalLayout.addWidget(self.pushStockBasicButton)
        self.pushCompanyButton = QtWidgets.QPushButton(self.basicinfofarme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushCompanyButton.sizePolicy().hasHeightForWidth())
        self.pushCompanyButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(11)
        self.pushCompanyButton.setFont(font)
        self.pushCompanyButton.setObjectName("pushCompanyButton")
        self.verticalLayout.addWidget(self.pushCompanyButton)
        self.pushToplistButton = QtWidgets.QPushButton(self.basicinfofarme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushToplistButton.sizePolicy().hasHeightForWidth())
        self.pushToplistButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(11)
        self.pushToplistButton.setFont(font)
        self.pushToplistButton.setObjectName("pushToplistButton")
        self.verticalLayout.addWidget(self.pushToplistButton)
        self.pushTopInstButton = QtWidgets.QPushButton(self.basicinfofarme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushTopInstButton.sizePolicy().hasHeightForWidth())
        self.pushTopInstButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(11)
        self.pushTopInstButton.setFont(font)
        self.pushTopInstButton.setObjectName("pushTopInstButton")
        self.verticalLayout.addWidget(self.pushTopInstButton)
        self.pushBlockTradeButton = QtWidgets.QPushButton(self.basicinfofarme)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBlockTradeButton.sizePolicy().hasHeightForWidth())
        self.pushBlockTradeButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体_GB2312")
        font.setPointSize(11)
        self.pushBlockTradeButton.setFont(font)
        self.pushBlockTradeButton.setObjectName("pushBlockTradeButton")
        self.verticalLayout.addWidget(self.pushBlockTradeButton)
        self.horizontalLayout.addWidget(self.basicinfofarme)
        self.horizontalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 827, 18))
        self.menuBar.setObjectName("menuBar")
        self.menu_dataupdate = QtWidgets.QMenu(self.menuBar)
        self.menu_dataupdate.setObjectName("menu_dataupdate")
        self.menu_sys = QtWidgets.QMenu(self.menuBar)
        self.menu_sys.setObjectName("menu_sys")
        self.menu_analysis = QtWidgets.QMenu(self.menuBar)
        self.menu_analysis.setObjectName("menu_analysis")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_initialDB = QtWidgets.QAction(MainWindow)
        self.action_initialDB.setObjectName("action_initialDB")
        self.action_update_Daily_Info = QtWidgets.QAction(MainWindow)
        self.action_update_Daily_Info.setObjectName("action_update_Daily_Info")
        self.action_update_DailyBasic_Info = QtWidgets.QAction(MainWindow)
        self.action_update_DailyBasic_Info.setObjectName("action_update_DailyBasic_Info")
        self.action_update_stock_basic = QtWidgets.QAction(MainWindow)
        self.action_update_stock_basic.setObjectName("action_update_stock_basic")
        self.action_update_company = QtWidgets.QAction(MainWindow)
        self.action_update_company.setObjectName("action_update_company")
        self.action_update_All = QtWidgets.QAction(MainWindow)
        self.action_update_All.setObjectName("action_update_All")
        self.action78 = QtWidgets.QAction(MainWindow)
        self.action78.setObjectName("action78")
        self.action_GROUP_BY_ts_code = QtWidgets.QAction(MainWindow)
        self.action_GROUP_BY_ts_code.setObjectName("action_GROUP_BY_ts_code")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.actionsdf = QtWidgets.QAction(MainWindow)
        self.actionsdf.setObjectName("actionsdf")
        self.action_ups_and_downs = QtWidgets.QAction(MainWindow)
        self.action_ups_and_downs.setObjectName("action_ups_and_downs")
        self.action_turnover_rate = QtWidgets.QAction(MainWindow)
        self.action_turnover_rate.setObjectName("action_turnover_rate")
        self.action_top_list = QtWidgets.QAction(MainWindow)
        self.action_top_list.setObjectName("action_top_list")
        self.action_top_inst = QtWidgets.QAction(MainWindow)
        self.action_top_inst.setObjectName("action_top_inst")
        self.action_block_trade = QtWidgets.QAction(MainWindow)
        self.action_block_trade.setObjectName("action_block_trade")
        self.menu_dataupdate.addAction(self.action_initialDB)
        self.menu_dataupdate.addSeparator()
        self.menu_dataupdate.addAction(self.action_update_stock_basic)
        self.menu_dataupdate.addAction(self.action_update_company)
        self.menu_dataupdate.addAction(self.action_update_Daily_Info)
        self.menu_dataupdate.addAction(self.action_update_DailyBasic_Info)
        self.menu_dataupdate.addAction(self.action_top_list)
        self.menu_dataupdate.addAction(self.action_top_inst)
        self.menu_dataupdate.addAction(self.action_block_trade)
        self.menu_dataupdate.addSeparator()
        self.menu_dataupdate.addAction(self.action_update_All)
        self.menu_sys.addAction(self.action_close)
        self.menu_analysis.addAction(self.action_ups_and_downs)
        self.menu_analysis.addAction(self.action_turnover_rate)
        self.menuBar.addAction(self.menu_sys.menuAction())
        self.menuBar.addAction(self.menu_dataupdate.menuAction())
        self.menuBar.addAction(self.menu_analysis.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "tushare主界面"))
        self.pushDailyButton.setText(_translate("MainWindow", "查看选定日期股票交易信息"))
        self.pushDailyBasicButton.setText(_translate("MainWindow", "查看选定日期股票指标信息"))
        self.pushStockBasicButton.setText(_translate("MainWindow", "查看股票基本信息"))
        self.pushCompanyButton.setText(_translate("MainWindow", "查看公司基本信息"))
        self.pushToplistButton.setText(_translate("MainWindow", "查看龙虎榜信息"))
        self.pushTopInstButton.setText(_translate("MainWindow", "查看龙虎榜机构交易信息"))
        self.pushBlockTradeButton.setText(_translate("MainWindow", "查看大宗交易信息"))
        self.menu_dataupdate.setTitle(_translate("MainWindow", "数据更新"))
        self.menu_sys.setTitle(_translate("MainWindow", "文件"))
        self.menu_analysis.setTitle(_translate("MainWindow", "分析"))
        self.action_initialDB.setText(_translate("MainWindow", "初始化数据库"))
        self.action_update_Daily_Info.setText(_translate("MainWindow", "更新交易信息"))
        self.action_update_DailyBasic_Info.setText(_translate("MainWindow", "更新交易指标信息"))
        self.action_update_stock_basic.setText(_translate("MainWindow", "更新股票基本信息"))
        self.action_update_company.setText(_translate("MainWindow", "更新公司信息"))
        self.action_update_All.setText(_translate("MainWindow", "更新所有信息"))
        self.action78.setText(_translate("MainWindow", "lk"))
        self.action_GROUP_BY_ts_code.setText(_translate("MainWindow", "+ \' GROUP BY ts_code  \' "))
        self.action_close.setText(_translate("MainWindow", "退出"))
        self.actionsdf.setText(_translate("MainWindow", "sdf"))
        self.action_ups_and_downs.setText(_translate("MainWindow", "涨跌分析"))
        self.action_turnover_rate.setText(_translate("MainWindow", "换手率分析"))
        self.action_top_list.setText(_translate("MainWindow", "更新龙虎榜"))
        self.action_top_inst.setText(_translate("MainWindow", "更新龙虎榜机构交易"))
        self.action_block_trade.setText(_translate("MainWindow", "更新大宗交易信息"))

