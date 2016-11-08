# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LEDGui_Optionen.ui'
#
# Created: Sat Oct 22 00:02:55 2016
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
        MainWindow.resize(348, 227)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Sans L"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 151, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 110, 61, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(170, 60, 62, 20))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 190, 83, 24))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.buttonAktualisieren = QtGui.QPushButton(self.centralwidget)
        self.buttonAktualisieren.setGeometry(QtCore.QRect(242, 190, 91, 24))
        self.buttonAktualisieren.setObjectName(_fromUtf8("buttonAktualisieren"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Optionen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Pausen zwischen LEDs:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Helligkeit der LEDs:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "0.05", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "0.15", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "0.2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "0.25", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "0.3", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(7, QtGui.QApplication.translate("MainWindow", "0.35", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(8, QtGui.QApplication.translate("MainWindow", "0.4", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(9, QtGui.QApplication.translate("MainWindow", "0.45", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(10, QtGui.QApplication.translate("MainWindow", "0.5", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(11, QtGui.QApplication.translate("MainWindow", "0.55", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(12, QtGui.QApplication.translate("MainWindow", "0.6", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(13, QtGui.QApplication.translate("MainWindow", "0.65", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(14, QtGui.QApplication.translate("MainWindow", "0.7", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(15, QtGui.QApplication.translate("MainWindow", "0.75", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(16, QtGui.QApplication.translate("MainWindow", "0.8", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(17, QtGui.QApplication.translate("MainWindow", "0.85", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(18, QtGui.QApplication.translate("MainWindow", "0.9", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(19, QtGui.QApplication.translate("MainWindow", "0.95", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(20, QtGui.QApplication.translate("MainWindow", "1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Zurück", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAktualisieren.setText(QtGui.QApplication.translate("MainWindow", "Aktualisieren", None, QtGui.QApplication.UnicodeUTF8))

