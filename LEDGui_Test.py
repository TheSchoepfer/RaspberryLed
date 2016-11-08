# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LEDGui_Test.ui'
#
# Created: Fri Oct 21 11:37:38 2016
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(344, 202)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.testLabel = QtGui.QLabel(self.centralwidget)
        self.testLabel.setGeometry(QtCore.QRect(130, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Sans L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.testLabel.setFont(font)
        self.testLabel.setObjectName(_fromUtf8("testLabel"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Sans L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 60, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Sans L"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.ButtonBack = QtGui.QPushButton(self.centralwidget)
        self.ButtonBack.setGeometry(QtCore.QRect(10, 170, 83, 24))
        self.ButtonBack.setObjectName(_fromUtf8("ButtonBack"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 120, 80))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.ButtonLedOn = QtGui.QRadioButton(self.groupBox)
        self.ButtonLedOn.setGeometry(QtCore.QRect(20, 10, 100, 19))
        self.ButtonLedOn.setObjectName(_fromUtf8("ButtonLedOn"))
        self.ButtonLedOff = QtGui.QRadioButton(self.groupBox)
        self.ButtonLedOff.setGeometry(QtCore.QRect(20, 40, 100, 19))
        self.ButtonLedOff.setObjectName(_fromUtf8("ButtonLedOff"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 80, 120, 80))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.ButtonButtonOff = QtGui.QRadioButton(self.groupBox_2)
        self.ButtonButtonOff.setGeometry(QtCore.QRect(10, 30, 100, 31))
        self.ButtonButtonOff.setObjectName(_fromUtf8("ButtonButtonOff"))
        self.ButtonButtonOn = QtGui.QRadioButton(self.groupBox_2)
        self.ButtonButtonOn.setGeometry(QtCore.QRect(10, 0, 100, 31))
        self.ButtonButtonOn.setObjectName(_fromUtf8("ButtonButtonOn"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.testLabel.setText(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "LED Test:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "LED Test:", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonBack.setText(QtGui.QApplication.translate("MainWindow", "Zurück", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonLedOn.setText(QtGui.QApplication.translate("MainWindow", "LED an", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonLedOff.setText(QtGui.QApplication.translate("MainWindow", "LED aus", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonButtonOff.setText(QtGui.QApplication.translate("MainWindow", "Buttons aus", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonButtonOn.setText(QtGui.QApplication.translate("MainWindow", "Buttons an", None, QtGui.QApplication.UnicodeUTF8))

