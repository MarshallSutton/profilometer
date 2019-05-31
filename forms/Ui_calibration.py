# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibration.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CalibrationWindow(object):
    def setupUi(self, CalibrationWindow):
        CalibrationWindow.setObjectName("CalibrationWindow")
        CalibrationWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CalibrationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(100, 90, 471, 321))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 301, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 100, 301, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 170, 301, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setGeometry(QtCore.QRect(320, 50, 28, 22))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_2.setGeometry(QtCore.QRect(320, 100, 28, 22))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_3.setGeometry(QtCore.QRect(320, 170, 28, 22))
        self.toolButton_3.setObjectName("toolButton_3")
        self.source_lbl = QtWidgets.QLabel(self.groupBox)
        self.source_lbl.setGeometry(QtCore.QRect(20, 30, 171, 16))
        self.source_lbl.setObjectName("source_lbl")
        self.calibration_lbl = QtWidgets.QLabel(self.groupBox)
        self.calibration_lbl.setGeometry(QtCore.QRect(30, 80, 111, 16))
        self.calibration_lbl.setObjectName("calibration_lbl")
        self.output_lbl = QtWidgets.QLabel(self.groupBox)
        self.output_lbl.setGeometry(QtCore.QRect(30, 150, 111, 16))
        self.output_lbl.setObjectName("output_lbl")
        CalibrationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalibrationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        CalibrationWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CalibrationWindow)
        self.statusbar.setObjectName("statusbar")
        CalibrationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CalibrationWindow)
        QtCore.QMetaObject.connectSlotsByName(CalibrationWindow)

    def retranslateUi(self, CalibrationWindow):
        _translate = QtCore.QCoreApplication.translate
        CalibrationWindow.setWindowTitle(_translate("CalibrationWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("CalibrationWindow", "GroupBox"))
        self.toolButton.setText(_translate("CalibrationWindow", "..."))
        self.toolButton_2.setText(_translate("CalibrationWindow", "..."))
        self.toolButton_3.setText(_translate("CalibrationWindow", "..."))
        self.source_lbl.setText(_translate("CalibrationWindow", "Scan file (to be calibrated)"))
        self.calibration_lbl.setText(_translate("CalibrationWindow", "Calibration File"))
        self.output_lbl.setText(_translate("CalibrationWindow", "Output location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalibrationWindow = QtWidgets.QMainWindow()
    ui = Ui_CalibrationWindow()
    ui.setupUi(CalibrationWindow)
    CalibrationWindow.show()
    sys.exit(app.exec_())

