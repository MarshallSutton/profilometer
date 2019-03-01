# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/msutton1/laser/forms/main_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tw_Charts = QtWidgets.QTabWidget(self.centralwidget)
        self.tw_Charts.setGeometry(QtCore.QRect(9, 65, 431, 221))
        self.tw_Charts.setObjectName("tw_Charts")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tw_Charts.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tw_Charts.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(9, 44, 139, 16))
        self.label.setObjectName("label")
        self.ScanParameters = QtWidgets.QGroupBox(self.centralwidget)
        self.ScanParameters.setGeometry(QtCore.QRect(240, 340, 231, 181))
        self.ScanParameters.setObjectName("ScanParameters")
        self.btn_SCAN = QtWidgets.QPushButton(self.ScanParameters)
        self.btn_SCAN.setGeometry(QtCore.QRect(20, 140, 80, 23))
        self.btn_SCAN.setObjectName("btn_SCAN")
        self.sb_N = QtWidgets.QSpinBox(self.ScanParameters)
        self.sb_N.setGeometry(QtCore.QRect(20, 30, 47, 24))
        self.sb_N.setObjectName("sb_N")
        self.spinBox_2 = QtWidgets.QSpinBox(self.ScanParameters)
        self.spinBox_2.setGeometry(QtCore.QRect(90, 30, 47, 24))
        self.spinBox_2.setObjectName("spinBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuProfilometer = QtWidgets.QMenu(self.menubar)
        self.menuProfilometer.setObjectName("menuProfilometer")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_File = QtWidgets.QAction(MainWindow)
        self.action_File.setObjectName("action_File")
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.menuProfilometer.addAction(self.action_File)
        self.menu_File.addAction(self.action_Save)
        self.menubar.addAction(self.menuProfilometer.menuAction())
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        self.tw_Charts.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tw_Charts.setTabText(self.tw_Charts.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tw_Charts.setTabText(self.tw_Charts.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label.setText(_translate("MainWindow", "Laser Scan MIcrometer"))
        self.ScanParameters.setTitle(_translate("MainWindow", "GroupBox"))
        self.btn_SCAN.setText(_translate("MainWindow", "SCAN"))
        self.menuProfilometer.setTitle(_translate("MainWindow", "Profilometer"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.action_File.setText(_translate("MainWindow", "&File"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))

