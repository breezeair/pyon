# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lottery.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from UI.LotteryGetData import *

class Ui_Lottery(object):
    def setupUi(self, Lottery):
        Lottery.setObjectName("Lottery")
        Lottery.resize(800, 621)
        self.pushButton = QtWidgets.QPushButton(Lottery)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Lottery)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Lottery)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 30, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Lottery)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 30, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Lottery)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 30, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableView = QtWidgets.QTableView(Lottery)
        self.tableView.setGeometry(QtCore.QRect(20, 70, 761, 531))
        self.tableView.setObjectName("tableView")

        self.pushButton_6 = QtWidgets.QPushButton(Lottery)
        self.pushButton_6.setGeometry(QtCore.QRect(530, 30, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(Lottery)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton2_clicked)
        self.pushButton_3.clicked.connect(self.pushButton3_clicked)
        self.pushButton_4.clicked.connect(self.pushButton4_clicked)
        self.pushButton_5.clicked.connect(self.pushButton5_clicked)
        self.pushButton_6.clicked.connect(self.close)
        QtCore.QMetaObject.connectSlotsByName(Lottery)

    def retranslateUi(self, Lottery):
        _translate = QtCore.QCoreApplication.translate
        Lottery.setWindowTitle(_translate("Lottery", "Form"))
        self.pushButton.setText(_translate("Lottery", "超级大乐透"))
        self.pushButton_2.setText(_translate("Lottery", "七位数"))
        self.pushButton_3.setText(_translate("Lottery", "排列3"))
        self.pushButton_4.setText(_translate("Lottery", "排列5"))
        self.pushButton_5.setText(_translate("Lottery", "11选5"))
        self.pushButton_6.setText(_translate("Lottery", "返回"))

    def initializeMode(self, code):
        ss = LotteryGetData(code)
        yy =ss.getData()
        model=QStandardItemModel(20,3);
        model.setHorizontalHeaderLabels(['期号','开奖号码','开奖时间'])
        for row in range(20):
            for column in range(3):
                item = QStandardItem("%s"%(yy[row][column]))
                model.setItem(row, column, item)
        #self.tableView=QTableView();
        return model
        
    
    def pushButton_clicked(self):
        print("超级大乐透")
        model = self.initializeMode('dlt')
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 200)

    def pushButton2_clicked(self):
        print("七位数")
        model = self.initializeMode('jstc7ws')
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 200)

    def pushButton3_clicked(self):
        print("排列3")
        model = self.initializeMode('pl3')
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 200)
    
    def pushButton4_clicked(self):
        print("排列5")
        model = self.initializeMode('yzfcpl5')
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 200)

    def pushButton5_clicked(self):
        print("11选5")
        model = self.initializeMode('jx11x5')
        self.tableView.setModel(model)
        self.tableView.setColumnWidth(0, 100)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 200)
