# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upsdownsFm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UpsAndDownsWindow(object):
    def setupUi(self, UpsAndDownsWindow):
        UpsAndDownsWindow.setObjectName("UpsAndDownsWindow")
        UpsAndDownsWindow.resize(1343, 948)
        self.centralwidget = QtWidgets.QWidget(UpsAndDownsWindow)
        self.centralwidget.setObjectName("centralwidget")
        UpsAndDownsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UpsAndDownsWindow)
        self.statusbar.setObjectName("statusbar")
        UpsAndDownsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UpsAndDownsWindow)
        QtCore.QMetaObject.connectSlotsByName(UpsAndDownsWindow)

    def retranslateUi(self, UpsAndDownsWindow):
        _translate = QtCore.QCoreApplication.translate
        UpsAndDownsWindow.setWindowTitle(_translate("UpsAndDownsWindow", "涨跌分析"))

