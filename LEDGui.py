# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LEDGui.ui'
#
# Created: Fri Oct 21 08:04:33 2016
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
        MainWindow.resize(324, 410)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ButtonLauflichtRL = QtGui.QPushButton(self.centralwidget)
        self.ButtonLauflichtRL.setGeometry(QtCore.QRect(40, 130, 83, 24))
        self.ButtonLauflichtRL.setObjectName(_fromUtf8("ButtonLauflichtRL"))
        self.ButtonVerschieden = QtGui.QPushButton(self.centralwidget)
        self.ButtonVerschieden.setGeometry(QtCore.QRect(202, 130, 81, 24))
        self.ButtonVerschieden.setObjectName(_fromUtf8("ButtonVerschieden"))
        self.ButtonLauflichtLR = QtGui.QPushButton(self.centralwidget)
        self.ButtonLauflichtLR.setGeometry(QtCore.QRect(40, 70, 83, 24))
        self.ButtonLauflichtLR.setObjectName(_fromUtf8("ButtonLauflichtLR"))
        self.ButtonTrennend = QtGui.QPushButton(self.centralwidget)
        self.ButtonTrennend.setGeometry(QtCore.QRect(200, 70, 83, 24))
        self.ButtonTrennend.setObjectName(_fromUtf8("ButtonTrennend"))
        self.ButtonSchliessen = QtGui.QPushButton(self.centralwidget)
        self.ButtonSchliessen.setGeometry(QtCore.QRect(240, 380, 83, 24))
        self.ButtonSchliessen.setObjectName(_fromUtf8("ButtonSchliessen"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Sans L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.LEDButton8 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton8.setGeometry(QtCore.QRect(230, 240, 84, 19))
        self.LEDButton8.setText(_fromUtf8(""))
        self.LEDButton8.setObjectName(_fromUtf8("LEDButton8"))
        self.LEDButton9 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton9.setGeometry(QtCore.QRect(260, 240, 84, 19))
        self.LEDButton9.setText(_fromUtf8(""))
        self.LEDButton9.setObjectName(_fromUtf8("LEDButton9"))
        self.LEDButton10 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton10.setGeometry(QtCore.QRect(290, 240, 84, 19))
        self.LEDButton10.setText(_fromUtf8(""))
        self.LEDButton10.setObjectName(_fromUtf8("LEDButton10"))
        self.LEDButton7 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton7.setGeometry(QtCore.QRect(200, 240, 84, 19))
        self.LEDButton7.setText(_fromUtf8(""))
        self.LEDButton7.setObjectName(_fromUtf8("LEDButton7"))
        self.LEDButton6 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton6.setGeometry(QtCore.QRect(170, 240, 84, 19))
        self.LEDButton6.setText(_fromUtf8(""))
        self.LEDButton6.setObjectName(_fromUtf8("LEDButton6"))
        self.LEDButton3 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton3.setGeometry(QtCore.QRect(80, 240, 84, 19))
        self.LEDButton3.setText(_fromUtf8(""))
        self.LEDButton3.setObjectName(_fromUtf8("LEDButton3"))
        self.LEDButton4 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton4.setGeometry(QtCore.QRect(110, 240, 84, 19))
        self.LEDButton4.setText(_fromUtf8(""))
        self.LEDButton4.setObjectName(_fromUtf8("LEDButton4"))
        self.LEDButton5 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton5.setGeometry(QtCore.QRect(140, 240, 84, 19))
        self.LEDButton5.setText(_fromUtf8(""))
        self.LEDButton5.setObjectName(_fromUtf8("LEDButton5"))
        self.LEDButton2 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton2.setGeometry(QtCore.QRect(50, 240, 84, 19))
        self.LEDButton2.setText(_fromUtf8(""))
        self.LEDButton2.setObjectName(_fromUtf8("LEDButton2"))
        self.LEDButton1 = QtGui.QCheckBox(self.centralwidget)
        self.LEDButton1.setGeometry(QtCore.QRect(20, 240, 84, 19))
        self.LEDButton1.setText(_fromUtf8(""))
        self.LEDButton1.setObjectName(_fromUtf8("LEDButton1"))
        self.buttonTest = QtGui.QPushButton(self.centralwidget)
        self.buttonTest.setGeometry(QtCore.QRect(162, 380, 61, 24))
        self.buttonTest.setObjectName(_fromUtf8("buttonTest"))
        self.buttonOptionen = QtGui.QPushButton(self.centralwidget)
        self.buttonOptionen.setGeometry(QtCore.QRect(0, 380, 83, 24))
        self.buttonOptionen.setObjectName(_fromUtf8("buttonOptionen"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonLauflichtRL.setText(QtGui.QApplication.translate("MainWindow", "Lauflicht RL", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonVerschieden.setText(QtGui.QApplication.translate("MainWindow", "Verschieden", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonLauflichtLR.setText(QtGui.QApplication.translate("MainWindow", "Lauflicht LR", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonTrennend.setText(QtGui.QApplication.translate("MainWindow", "Trennend", None, QtGui.QApplication.UnicodeUTF8))
        self.ButtonSchliessen.setText(QtGui.QApplication.translate("MainWindow", "Schliessen", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Raspberry Pi Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonTest.setText(QtGui.QApplication.translate("MainWindow", "Testen", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOptionen.setText(QtGui.QApplication.translate("MainWindow", "Optionen", None, QtGui.QApplication.UnicodeUTF8))

