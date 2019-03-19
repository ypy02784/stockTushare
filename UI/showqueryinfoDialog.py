# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\study\github\stockTushare\UI\showqueryinfoDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_show_queryinfo(object):
    def setupUi(self, Dialog_show_queryinfo):
        Dialog_show_queryinfo.setObjectName("Dialog_show_queryinfo")
        Dialog_show_queryinfo.resize(1696, 1211)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog_show_queryinfo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(Dialog_show_queryinfo)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)

        self.retranslateUi(Dialog_show_queryinfo)
        QtCore.QMetaObject.connectSlotsByName(Dialog_show_queryinfo)

    def retranslateUi(self, Dialog_show_queryinfo):
        _translate = QtCore.QCoreApplication.translate
        Dialog_show_queryinfo.setWindowTitle(_translate("Dialog_show_queryinfo", "信息查看"))

