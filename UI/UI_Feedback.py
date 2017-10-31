# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_Feedback.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.LatticeOfficer import *
from PyQt5.QtWidgets import *
from UI.Feedback import *

class Ui_feedback(object):
    def setupUi(self, feedback):
        feedback.setObjectName("feedback")
        feedback.resize(800, 600)
        self.groupBox = QtWidgets.QGroupBox(feedback)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 771, 171))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 54, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 70, 54, 12))
        self.label_5.setObjectName("label_5")
        self.lineEdit1 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit1.setGeometry(QtCore.QRect(110, 40, 113, 30))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit2.setGeometry(QtCore.QRect(110, 100, 113, 30))
        self.lineEdit2.setObjectName("lineEdit2")
        self.textEdit3 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit3.setGeometry(QtCore.QRect(390, 30, 361, 121))
        self.textEdit3.setObjectName("textEdit3")
        self.groupBox_2 = QtWidgets.QGroupBox(feedback)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 210, 771, 331))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rbOfficer = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbOfficer.setGeometry(QtCore.QRect(40, 50, 89, 16))
        self.rbOfficer.setObjectName("radioButton1")
        self.rbPoint = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbPoint.setGeometry(QtCore.QRect(110, 50, 89, 16))
        self.rbPoint.setObjectName("radioButton2")
        self.rbOther = QtWidgets.QRadioButton(self.groupBox_2)
        self.rbOther.setGeometry(QtCore.QRect(40, 220, 89, 16))
        self.rbOther.setObjectName("radioButton3")
        self.lineEdit4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit4.setGeometry(QtCore.QRect(110, 100, 113, 30))
        self.lineEdit4.setObjectName("lineEdit4")
        self.textEdit6 = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit6.setGeometry(QtCore.QRect(390, 120, 360, 180))
        self.textEdit6.setObjectName("textEdit6")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(310, 150, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 54, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 100, 41, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.labelDetail = QtWidgets.QLabel(self.groupBox_2)
        self.labelDetail.setGeometry(QtCore.QRect(40, 150, 250, 30))
        self.labelDetail.setObjectName("labelDetail")
        self.lineEdit5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit5.setGeometry(QtCore.QRect(110, 210, 113, 30))
        self.lineEdit5.setObjectName("lineEdit5")
        self.pushButton = QtWidgets.QPushButton(feedback)
        self.pushButton.setGeometry(QtCore.QRect(210, 560, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(feedback)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 560, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        #
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(390, 60, 90, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.labelStatus = QtWidgets.QLabel(self.groupBox_2)
        self.labelStatus.setGeometry(QtCore.QRect(310, 70, 54, 12))
        self.labelStatus.setObjectName("label_5")
        #
        self.retranslateUi(feedback)
        QtCore.QMetaObject.connectSlotsByName(feedback)

    def retranslateUi(self, feedback):
        _translate = QtCore.QCoreApplication.translate
        feedback.setWindowTitle(_translate("feedback", "投诉与反馈"))
        self.groupBox.setTitle(_translate("feedback", "投诉人信息"))
        self.label_3.setText(_translate("feedback", "姓名："))
        self.label_4.setText(_translate("feedback", "联系电话："))
        self.label_5.setText(_translate("feedback", "其他信息："))
        self.groupBox_2.setTitle(_translate("feedback", "被投诉对象"))
        self.rbOfficer.setText(_translate("feedback", "专管员"))
        self.rbPoint.setText(_translate("feedback", "网点"))
        self.rbOther.setText(_translate("feedback", "其他"))
        self.label.setText(_translate("feedback", "具体内容："))
        self.label_2.setText(_translate("feedback", "请输入："))
        self.pushButton_3.setText(_translate("feedback", "查询"))
        self.labelDetail.setText(_translate("feedback", "信息显示"))
        self.pushButton.setText(_translate("feedback", "提交"))
        self.pushButton_2.setText(_translate("feedback", "取消"))
        self.comboBox.setItemText(0, _translate("feedback", "未选择"))
        self.comboBox.setItemText(1, _translate("feedback", "未解决"))
        self.comboBox.setItemText(2, _translate("feedback", "已解决"))
        self.labelStatus.setText(_translate("feedback", "状态："))

        self.pushButton_3.clicked.connect(self.btnSearch)
        self.pushButton_2.clicked.connect(self.close)

    def btnSearch(self):
        print("sss")
        if (self.rbPoint.isChecked()):
            number = self.lineEdit4.text()
            name = ''
            ss = Feedback()
            inform = ss.getAddress(number)
            print(number)
            print(inform)
            self.labelDetail.setText("地址：" + inform)
        elif (self.rbOfficer.isChecked()):
            name = self.lineEdit4.text()
            number = ''
            ss = Feedback()
            inform = ss.getTelNum(name)
            print(name)
            print(inform)
            self.labelDetail.setText("手机号：" + inform)

