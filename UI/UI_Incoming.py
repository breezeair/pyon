# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_Incoming.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Lottery import *
from UI.UI_LatticePoint import *
from UI.UI_Maintenance import *
from UI.UI_Feedback import *
from UI.UI_Other import *

class Ui_IncomingInfo(object):
    def setupUi(self, IncomingInfo):
        IncomingInfo.setObjectName("IncomingInfo")
        IncomingInfo.resize(650, 480)
        self.groupBox = QtWidgets.QGroupBox(IncomingInfo)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 621, 211))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 84, 20))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 70, 84, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 110, 84, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 48, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(140, 30, 120, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 120, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 110, 120, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 150, 120, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushPlace = QtWidgets.QPushButton(self.groupBox)
        self.pushPlace.setGeometry(QtCore.QRect(450, 100, 75, 23))
        self.pushPlace.setObjectName("pushButton_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(320, 40, 261, 31))
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(IncomingInfo)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 220, 621, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(80, 40, 90, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 40, 100, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 130, 90, 60))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 40, 90, 60))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 130, 90, 60))
        self.pushButton_5.setObjectName("pushButton_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(320, 100, 110, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.retranslateUi(IncomingInfo)
        QtCore.QMetaObject.connectSlotsByName(IncomingInfo)

    def retranslateUi(self, IncomingInfo):
        _translate = QtCore.QCoreApplication.translate
        IncomingInfo.setWindowTitle(_translate("IncomingInfo", "Form"))
        self.groupBox.setTitle(_translate("IncomingInfo", "来电信息"))
        self.label_2.setText(_translate("IncomingInfo", "来电号码："))
        self.label.setText(_translate("IncomingInfo", "时间："))
        self.label_3.setText(_translate("IncomingInfo", "今日来电序号："))
        self.label_4.setText(_translate("IncomingInfo", "登记员："))
        self.pushPlace.setText(_translate("IncomingInfo", "归档"))
        self.label_5.setText(_translate("IncomingInfo", "如为有效来电，请点击归档，再进行后续操作："))
        self.groupBox_2.setTitle(_translate("IncomingInfo", "咨询内容"))
        self.pushButton.setText(_translate("IncomingInfo", "开奖号码查询"))
        self.pushButton_2.setText(_translate("IncomingInfo", "新网点申办咨询"))
        self.pushButton_3.setText(_translate("IncomingInfo", "设备维修"))
        self.pushButton_4.setText(_translate("IncomingInfo", "投诉与建议"))
        self.pushButton_5.setText(_translate("IncomingInfo", "其他"))
        #
        self.comboBox.setItemText(0, _translate("IncomingInfo", "请选择"))
        self.comboBox.setItemText(1, _translate("IncomingInfo", "开奖号码查询"))
        self.comboBox.setItemText(2, _translate("IncomingInfo", "新网点申办咨询"))
        self.comboBox.setItemText(3, _translate("IncomingInfo", "设备维修"))
        self.comboBox.setItemText(4, _translate("IncomingInfo", "投诉与建议"))
        self.comboBox.setItemText(5, _translate("IncomingInfo", "其他"))
        now = datetime.datetime.now()
        strnow = now.strftime('%Y-%m-%d %H:%M:%S')
        self.lineEdit_2.setText(_translate("IncomingInfo", strnow))

        self.pushButton.clicked.connect(self.btnLottery)
        self.pushButton_2.clicked.connect(self.btnLattice)
        self.pushButton_3.clicked.connect(self.btnMaintenance)
        self.pushButton_4.clicked.connect(self.btnFeedback)
        self.pushButton_5.clicked.connect(self.btnOther)
        self.pushPlace.clicked.connect(self.btnPlace)

    def btnLottery(self):
        lotteryWin = LotteryWindow(self)
        lotteryWin.show()

    def btnLattice(self):
        lotteryWin = LatticeyWindow(self)
        lotteryWin.show()

    def btnMaintenance(self):
        lotteryWin = MaintenanceWindow(self)
        lotteryWin.show()

    def btnOther(self):
        lotteryWin = OtherWindow(self)
        lotteryWin.show()

    def btnFeedback(self):
        lotteryWin = FeedbackWindow(self)
        lotteryWin.show()

    def btnPlace(self):
        content = self.comboBox.currentText()
        number = self.lineEdit.text()
        now = datetime.datetime.now()
        dateNow = now.strftime('%Y-%m-%d')
        timeNow = now.strftime('%H:%M:%S')
        worker = self.lineEdit_4.text()

        

class LotteryWindow(QMainWindow, Ui_Lottery):
    def __init__(self, parent=None):    
        super(LotteryWindow, self).__init__(parent)
        self.setupUi(self)

class LatticeyWindow(QMainWindow, Ui_LatticePoint):
    def __init__(self, parent=None):    
        super(LatticeyWindow, self).__init__(parent)
        self.setupUi(self)

class FeedbackWindow(QMainWindow, Ui_feedback):
    def __init__(self, parent=None):    
        super(FeedbackWindow, self).__init__(parent)
        self.setupUi(self)

class OtherWindow(QMainWindow, Ui_Other):
    def __init__(self, parent=None):    
        super(OtherWindow, self).__init__(parent)
        self.setupUi(self)

class MaintenanceWindow(QMainWindow, Ui_Maintenance):
    def __init__(self, parent=None):    
        super(MaintenanceWindow, self).__init__(parent)
        self.setupUi(self)