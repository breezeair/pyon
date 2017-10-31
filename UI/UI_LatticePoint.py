# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI_LatticePoint.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.LatticeOfficer import *
from PyQt5.QtWidgets import *
from UI.UI_LatticePoint import *
from PyQt5.QtCore import QStringListModel

class Ui_LatticePoint(object):
    def setupUi(self, LatticePoint):
        LatticePoint.setObjectName("LatticePoint")
        LatticePoint.resize(640, 480)
        self.comboBox = QtWidgets.QComboBox(LatticePoint)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 75, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.listView = QtWidgets.QListView(LatticePoint)
        self.listView.setGeometry(QtCore.QRect(30, 80, 131, 341))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(LatticePoint)
        self.label.setGeometry(QtCore.QRect(200, 90, 54, 12))
        self.label.setObjectName("label")
        #
        self.labWorkNum = QtWidgets.QLabel(LatticePoint)
        self.labWorkNum.setGeometry(QtCore.QRect(400, 90, 54, 12))
        self.labWorkNum.setObjectName("labWorkNum")
        self.labWorkNum_1 = QtWidgets.QLabel(LatticePoint)
        self.labWorkNum_1.setGeometry(QtCore.QRect(470, 90, 54, 12))
        self.labWorkNum_1.setObjectName("labWorkNum_1")
        #
        self.label_2 = QtWidgets.QLabel(LatticePoint)
        self.label_2.setGeometry(QtCore.QRect(200, 130, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(LatticePoint)
        self.label_3.setGeometry(QtCore.QRect(200, 210, 54, 12))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(LatticePoint)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 210, 80, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(LatticePoint)
        self.label_4.setGeometry(QtCore.QRect(270, 90, 54, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(LatticePoint)
        self.label_5.setGeometry(QtCore.QRect(270, 130, 54, 12))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(LatticePoint)
        self.textEdit.setGeometry(QtCore.QRect(200, 250, 401, 171))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(LatticePoint)
        self.pushButton.setGeometry(QtCore.QRect(200, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(LatticePoint)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 440, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(LatticePoint)
        self.label_6.setGeometry(QtCore.QRect(200, 170, 54, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(LatticePoint)
        self.label_7.setGeometry(QtCore.QRect(270, 170, 54, 12))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(LatticePoint)
        QtCore.QMetaObject.connectSlotsByName(LatticePoint)

    def retranslateUi(self, LatticePoint):
        _translate = QtCore.QCoreApplication.translate
        LatticePoint.setWindowTitle(_translate("LatticePoint", "Form"))
        self.comboBox.setItemText(0, _translate("LatticePoint", "请选择"))
        self.comboBox.setItemText(1, _translate("LatticePoint", "玄武区"))
        self.comboBox.setItemText(2, _translate("LatticePoint", "鼓楼区"))
        self.comboBox.setItemText(3, _translate("LatticePoint", "秦淮区"))
        self.comboBox.setItemText(4, _translate("LatticePoint", "建邺区"))
        self.comboBox.setItemText(5, _translate("LatticePoint", "雨花台区"))
        self.comboBox.setItemText(6, _translate("LatticePoint", "栖霞区"))
        self.comboBox.setItemText(7, _translate("LatticePoint", "浦口区"))
        self.comboBox.setItemText(8, _translate("LatticePoint", "六合区"))
        self.comboBox.setItemText(9, _translate("LatticePoint", "江宁区"))
        self.comboBox.setItemText(10, _translate("LatticePoint", "溧水区"))
        self.comboBox.setItemText(11, _translate("LatticePoint", "高淳区"))
        self.label.setText(_translate("LatticePoint", "专管员："))
        self.labWorkNum.setText(_translate("LatticePoint", "办公电话："))
        self.labWorkNum_1.setText(_translate("LatticePoint", "0"))
        self.label_2.setText(_translate("LatticePoint", "工作手机："))
        self.label_3.setText(_translate("LatticePoint", "咨询内容："))
        self.comboBox_2.setItemText(0, _translate("LatticePoint", "申办流程"))
        self.comboBox_2.setItemText(1, _translate("LatticePoint", "申办渠道"))
        self.comboBox_2.setItemText(2, _translate("LatticePoint", "申办条件"))
        self.comboBox_2.setItemText(3, _translate("LatticePoint", "其他"))
        self.label_4.setText(_translate("LatticePoint", "0"))
        self.label_5.setText(_translate("LatticePoint", "0"))
        self.pushButton.setText(_translate("LatticePoint", "提交"))
        self.pushButton_2.setText(_translate("LatticePoint", "取消"))
        self.label_6.setText(_translate("LatticePoint", "个人手机："))
        self.label_7.setText(_translate("LatticePoint", "0"))

        self.comboBox.currentIndexChanged.connect(self.getNameList)
        self.listView.clicked.connect(self.getOfficerDetail)
        self.pushButton_2.clicked.connect(self.close)
        

    nameList = []

    def getNameList(self, i):
        area = self.comboBox.currentText()
        ss = LatticeOfficer(area)
        yy = ss.getOfficerList()
        self.nameList = yy
        print(yy)
        slm = QStringListModel()
        slm.setStringList(yy)
        self.listView.setModel(slm)
        

    def getOfficerDetail(self, qModelIndex):
        ss = LatticeOfficer()
        name = self.nameList[qModelIndex.row()]
        print(name)
        zz = ss.getDetail(name)
        print(zz)
        #self.label_2.setText(zz[0])
        self.label_4.setText(zz[0])
        self.label_5.setText(zz[2])
        self.label_7.setText(zz[1])
        self.labWorkNum_1.setText(zz[3])

