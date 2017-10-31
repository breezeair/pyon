# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_Other.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Other(object):
    def setupUi(self, Other):
        Other.setObjectName("Other")
        Other.resize(800, 600)
        self.label = QtWidgets.QLabel(Other)
        self.label.setGeometry(QtCore.QRect(80, 80, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Other)
        self.label_2.setGeometry(QtCore.QRect(80, 250, 54, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Other)
        self.pushButton.setGeometry(QtCore.QRect(290, 520, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Other)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 520, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Other)
        self.textEdit.setGeometry(QtCore.QRect(190, 60, 491, 81))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Other)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 190, 491, 271))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Other)
        QtCore.QMetaObject.connectSlotsByName(Other)

    def retranslateUi(self, Other):
        _translate = QtCore.QCoreApplication.translate
        Other.setWindowTitle(_translate("Other", "Form"))
        self.label.setText(_translate("Other", "问题概述："))
        self.label_2.setText(_translate("Other", "备注："))
        self.pushButton.setText(_translate("Other", "提交"))
        self.pushButton_2.setText(_translate("Other", "取消"))

        self.pushButton_2.clicked.connect(self.close)

