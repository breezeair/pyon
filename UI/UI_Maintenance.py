# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_Maintenance.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.LatticeOfficer import *
from PyQt5.QtWidgets import *
from UI.Mainten import *

class Ui_Maintenance(object):
    def setupUi(self, Maintenance):
        Maintenance.setObjectName("Maintenance")
        Maintenance.resize(800, 600)
        self.groupBox = QtWidgets.QGroupBox(Maintenance)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 771, 171))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit1.setGeometry(QtCore.QRect(90, 40, 113, 30))
        self.lineEdit1.setObjectName("lineEdit1")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 50, 54, 12))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(370, 40, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(370, 80, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(370, 120, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(450, 40, 80, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(450, 80, 80, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(450, 120, 250, 12))
        self.label_12.setObjectName("label_12")
        self.groupBox_2 = QtWidgets.QGroupBox(Maintenance)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 771, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(110, 60, 120, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 70, 54, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(40, 120, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(40, 220, 54, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(40, 170, 54, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(270, 140, 54, 12))
        self.label_9.setObjectName("label_9")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(340, 30, 411, 241))
        self.textEdit.setObjectName("textEdit")
        self.lineEdit2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit2.setGeometry(QtCore.QRect(110, 110, 113, 30))
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit3.setGeometry(QtCore.QRect(110, 160, 113, 30))
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit4.setGeometry(QtCore.QRect(110, 210, 113, 30))
        self.lineEdit4.setObjectName("lineEdit4")
        self.comboBox.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.textEdit.raise_()
        self.lineEdit2.raise_()
        self.lineEdit3.raise_()
        self.lineEdit4.raise_()
        self.groupBox.raise_()
        self.pushButton_2 = QtWidgets.QPushButton(Maintenance)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 540, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Maintenance)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 540, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        #self.comboBox.currentIndexChanged.connect(self.getNameList)
        #self.listView.clicked.connect(self.getOfficerDetail)
        self.pushButton.clicked.connect(self.getSearchResult)
        self.pushButton_3.clicked.connect(self.close)

        self.retranslateUi(Maintenance)
        QtCore.QMetaObject.connectSlotsByName(Maintenance)

    def retranslateUi(self, Maintenance):
        _translate = QtCore.QCoreApplication.translate
        Maintenance.setWindowTitle(_translate("Maintenance", "Form"))
        self.groupBox.setTitle(_translate("Maintenance", "站点信息"))
        self.label.setText(_translate("Maintenance", "站点号："))
        self.pushButton.setText(_translate("Maintenance", "查询"))
        self.label_2.setText(_translate("Maintenance", "专管员："))
        self.label_3.setText(_translate("Maintenance", "手机号："))
        self.label_4.setText(_translate("Maintenance", "网点地址："))
        self.label_10.setText(_translate("Maintenance", ""))
        self.label_11.setText(_translate("Maintenance", ""))
        self.label_12.setText(_translate("Maintenance", ""))
        self.groupBox_2.setTitle(_translate("Maintenance", "报修设备"))
        self.comboBox.setItemText(0, _translate("Maintenance", "请选择"))
        self.comboBox.setItemText(1, _translate("Maintenance", "TPT-IU"))
        self.comboBox.setItemText(2, _translate("Maintenance", "CP8608"))
        self.comboBox.setItemText(3, _translate("Maintenance", "CP8609"))
        self.comboBox.setItemText(4, _translate("Maintenance", "TPT-II-61-06"))
        self.comboBox.setItemText(5, _translate("Maintenance", "TPT-II-61-01"))
        self.comboBox.setItemText(6, _translate("Maintenance", "其它"))
        self.label_5.setText(_translate("Maintenance", "设备型号："))
        self.label_6.setText(_translate("Maintenance", "设备编号："))
        self.label_7.setText(_translate("Maintenance", "联系号码："))
        self.label_8.setText(_translate("Maintenance", "联系人："))
        self.label_9.setText(_translate("Maintenance", "问题描述："))
        self.pushButton_2.setText(_translate("Maintenance", "提交"))
        self.pushButton_3.setText(_translate("Maintenance", "取消"))

    def getSearchResult(self):
        num = self.lineEdit1.text()
        ss = Mainten(num)
        na = []
        na = ss.getNameandAddress()
        if (na != []):
            cc = ss.getTelNum(na[0])
            print(ss.getTelNum(na[0]))
            self.label_10.setText(na[0])
            self.label_12.setText(na[1])
            self.label_11.setText(cc)
        else:
            print("站点号有误")
        print(na)
