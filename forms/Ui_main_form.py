# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 139, 16))
        self.label.setObjectName("label")
        self.ScanParameters = QtWidgets.QGroupBox(self.centralwidget)
        self.ScanParameters.setGeometry(QtCore.QRect(270, 520, 221, 181))
        self.ScanParameters.setObjectName("ScanParameters")
        self.btn_SCAN = QtWidgets.QPushButton(self.ScanParameters)
        self.btn_SCAN.setGeometry(QtCore.QRect(20, 110, 80, 23))
        self.btn_SCAN.setObjectName("btn_SCAN")
        self.sb_Npoints = QtWidgets.QSpinBox(self.ScanParameters)
        self.sb_Npoints.setGeometry(QtCore.QRect(20, 70, 47, 24))
        self.sb_Npoints.setMaximum(2000)
        self.sb_Npoints.setProperty("value", 10)
        self.sb_Npoints.setObjectName("sb_Npoints")
        self.lbl_Nsamples = QtWidgets.QLabel(self.ScanParameters)
        self.lbl_Nsamples.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.lbl_Nsamples.setWordWrap(True)
        self.lbl_Nsamples.setObjectName("lbl_Nsamples")
        self.lbl_sampleLength = QtWidgets.QLabel(self.ScanParameters)
        self.lbl_sampleLength.setGeometry(QtCore.QRect(130, 30, 91, 16))
        self.lbl_sampleLength.setObjectName("lbl_sampleLength")
        self.lbl_microns = QtWidgets.QLabel(self.ScanParameters)
        self.lbl_microns.setGeometry(QtCore.QRect(190, 70, 59, 15))
        self.lbl_microns.setObjectName("lbl_microns")
        self.btn_stop = QtWidgets.QPushButton(self.ScanParameters)
        self.btn_stop.setGeometry(QtCore.QRect(110, 110, 80, 23))
        self.btn_stop.setObjectName("btn_stop")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.ScanParameters)
        self.doubleSpinBox.setGeometry(QtCore.QRect(120, 70, 66, 24))
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setSingleStep(0.05)
        self.doubleSpinBox.setProperty("value", 1.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.limit_lable = QtWidgets.QLabel(self.ScanParameters)
        self.limit_lable.setEnabled(False)
        self.limit_lable.setGeometry(QtCore.QRect(0, 160, 111, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.limit_lable.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.limit_lable.setFont(font)
        self.limit_lable.setAutoFillBackground(True)
        self.limit_lable.setStyleSheet("color: red")
        self.limit_lable.setTextFormat(QtCore.Qt.PlainText)
        self.limit_lable.setObjectName("limit_lable")
        self.gb_ = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_.setGeometry(QtCore.QRect(10, 530, 251, 191))
        self.gb_.setObjectName("gb_")
        self.formLayout = QtWidgets.QFormLayout(self.gb_)
        self.formLayout.setObjectName("formLayout")
        self.btn_go1 = QtWidgets.QPushButton(self.gb_)
        self.btn_go1.setObjectName("btn_go1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_go1)
        self.sb_goto1 = QtWidgets.QDoubleSpinBox(self.gb_)
        self.sb_goto1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.sb_goto1.setToolTipDuration(2)
        self.sb_goto1.setDecimals(3)
        self.sb_goto1.setMinimum(-10.0)
        self.sb_goto1.setMaximum(300.0)
        self.sb_goto1.setProperty("value", 60.0)
        self.sb_goto1.setObjectName("sb_goto1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.sb_goto1)
        self.btn_goto2 = QtWidgets.QPushButton(self.gb_)
        self.btn_goto2.setObjectName("btn_goto2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.btn_goto2)
        self.sb_goto2 = QtWidgets.QDoubleSpinBox(self.gb_)
        self.sb_goto2.setDecimals(3)
        self.sb_goto2.setMinimum(-10.0)
        self.sb_goto2.setMaximum(300.0)
        self.sb_goto2.setProperty("value", 100.0)
        self.sb_goto2.setObjectName("sb_goto2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sb_goto2)
        self.btn_goto3 = QtWidgets.QPushButton(self.gb_)
        self.btn_goto3.setObjectName("btn_goto3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.btn_goto3)
        self.sb_goto3 = QtWidgets.QDoubleSpinBox(self.gb_)
        self.sb_goto3.setDecimals(3)
        self.sb_goto3.setMinimum(-10.0)
        self.sb_goto3.setMaximum(300.0)
        self.sb_goto3.setProperty("value", 125.0)
        self.sb_goto3.setObjectName("sb_goto3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sb_goto3)
        self.btn_goto3_2 = QtWidgets.QPushButton(self.gb_)
        self.btn_goto3_2.setObjectName("btn_goto3_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.btn_goto3_2)
        self.sb_goto3_2 = QtWidgets.QDoubleSpinBox(self.gb_)
        self.sb_goto3_2.setDecimals(3)
        self.sb_goto3_2.setMinimum(-10.0)
        self.sb_goto3_2.setMaximum(300.0)
        self.sb_goto3_2.setProperty("value", 150.0)
        self.sb_goto3_2.setObjectName("sb_goto3_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sb_goto3_2)
        self.lbl_current_pos = QtWidgets.QLabel(self.gb_)
        self.lbl_current_pos.setObjectName("lbl_current_pos")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lbl_current_pos)
        self.curr_position = QtWidgets.QDoubleSpinBox(self.gb_)
        self.curr_position.setReadOnly(True)
        self.curr_position.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.curr_position.setDecimals(3)
        self.curr_position.setMinimum(-10.0)
        self.curr_position.setMaximum(300.0)
        self.curr_position.setObjectName("curr_position")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.curr_position)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 30, 681, 471))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        self.sb_left = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_left.setGeometry(QtCore.QRect(70, 500, 47, 24))
        self.sb_left.setMinimum(-100)
        self.sb_left.setMaximum(120)
        self.sb_left.setObjectName("sb_left")
        self.sb_right = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_right.setGeometry(QtCore.QRect(130, 500, 47, 24))
        self.sb_right.setMaximum(200)
        self.sb_right.setProperty("value", 100)
        self.sb_right.setObjectName("sb_right")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 500, 81, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 81, 141))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.sb_lower_limit = QtWidgets.QSpinBox(self.groupBox)
        self.sb_lower_limit.setGeometry(QtCore.QRect(20, 90, 47, 24))
        self.sb_lower_limit.setMinimum(-100)
        self.sb_lower_limit.setMaximum(100)
        self.sb_lower_limit.setProperty("value", -10)
        self.sb_lower_limit.setObjectName("sb_lower_limit")
        self.sb_upper_limit = QtWidgets.QSpinBox(self.groupBox)
        self.sb_upper_limit.setGeometry(QtCore.QRect(20, 60, 47, 24))
        self.sb_upper_limit.setMinimum(-100)
        self.sb_upper_limit.setMaximum(100)
        self.sb_upper_limit.setProperty("value", 10)
        self.sb_upper_limit.setObjectName("sb_upper_limit")
        self.lbl_limit = QtWidgets.QLabel(self.groupBox)
        self.lbl_limit.setGeometry(QtCore.QRect(10, 30, 59, 15))
        self.lbl_limit.setObjectName("lbl_limit")
        self.btn_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Clear.setGeometry(QtCore.QRect(510, 670, 80, 23))
        self.btn_Clear.setObjectName("btn_Clear")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 300, 81, 141))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.sb_lower_limit_intensity = QtWidgets.QSpinBox(self.groupBox_2)
        self.sb_lower_limit_intensity.setGeometry(QtCore.QRect(20, 90, 47, 24))
        self.sb_lower_limit_intensity.setMinimum(-100)
        self.sb_lower_limit_intensity.setMaximum(100)
        self.sb_lower_limit_intensity.setProperty("value", 50)
        self.sb_lower_limit_intensity.setObjectName("sb_lower_limit_intensity")
        self.sb_upper_limit_intensity = QtWidgets.QSpinBox(self.groupBox_2)
        self.sb_upper_limit_intensity.setGeometry(QtCore.QRect(20, 60, 47, 24))
        self.sb_upper_limit_intensity.setMinimum(50)
        self.sb_upper_limit_intensity.setMaximum(300)
        self.sb_upper_limit_intensity.setProperty("value", 250)
        self.sb_upper_limit_intensity.setObjectName("sb_upper_limit_intensity")
        self.lbl_limit_2 = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_limit_2.setGeometry(QtCore.QRect(10, 30, 59, 15))
        self.lbl_limit_2.setObjectName("lbl_limit_2")
        self.comments = QtWidgets.QTextBrowser(self.centralwidget)
        self.comments.setGeometry(QtCore.QRect(510, 540, 231, 121))
        self.comments.setReadOnly(False)
        self.comments.setOverwriteMode(True)
        self.comments.setObjectName("comments")
        self.comment_label = QtWidgets.QLabel(self.centralwidget)
        self.comment_label.setGeometry(QtCore.QRect(520, 510, 71, 16))
        self.comment_label.setObjectName("comment_label")
        self.btn_Clear_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Clear_2.setGeometry(QtCore.QRect(610, 670, 111, 23))
        self.btn_Clear_2.setObjectName("btn_Clear_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 20))
        self.menubar.setObjectName("menubar")
        self.menuProfilometer = QtWidgets.QMenu(self.menubar)
        self.menuProfilometer.setObjectName("menuProfilometer")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuTIlt_Correction = QtWidgets.QMenu(self.menubar)
        self.menuTIlt_Correction.setObjectName("menuTIlt_Correction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_File = QtWidgets.QAction(MainWindow)
        self.action_File.setObjectName("action_File")
        self.action_Save = QtWidgets.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.actionTilt_Correct = QtWidgets.QAction(MainWindow)
        self.actionTilt_Correct.setObjectName("actionTilt_Correct")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.action_Print = QtWidgets.QAction(MainWindow)
        self.action_Print.setObjectName("action_Print")
        self.action_Close = QtWidgets.QAction(MainWindow)
        self.action_Close.setObjectName("action_Close")
        self.menuProfilometer.addAction(self.action_File)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionLoad)
        self.menu_File.addAction(self.action_Print)
        self.menu_File.addAction(self.action_Close)
        self.menuTIlt_Correction.addAction(self.actionTilt_Correct)
        self.menubar.addAction(self.menuProfilometer.menuAction())
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuTIlt_Correction.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Profilometer"))
        self.label.setText(_translate("MainWindow", "Laser Scan MIcrometer"))
        self.ScanParameters.setTitle(_translate("MainWindow", "Scan Parameters"))
        self.btn_SCAN.setText(_translate("MainWindow", "SCAN"))
        self.lbl_Nsamples.setText(_translate("MainWindow", "Number of Samples"))
        self.lbl_sampleLength.setText(_translate("MainWindow", "Interval (mm)"))
        self.lbl_microns.setText(_translate("MainWindow", "mm"))
        self.btn_stop.setText(_translate("MainWindow", "Stop SCAN"))
        self.limit_lable.setText(_translate("MainWindow", "End of Limit"))
        self.gb_.setTitle(_translate("MainWindow", " Motion control distance along axis (mm)"))
        self.btn_go1.setText(_translate("MainWindow", "Go"))
        self.btn_goto2.setText(_translate("MainWindow", "Go"))
        self.btn_goto3.setText(_translate("MainWindow", "Go"))
        self.btn_goto3_2.setText(_translate("MainWindow", "Go"))
        self.lbl_current_pos.setText(_translate("MainWindow", "Current Position"))
        self.label_2.setText(_translate("MainWindow", "Set X-range"))
        self.lbl_limit.setText(_translate("MainWindow", "Set Limits"))
        self.btn_Clear.setText(_translate("MainWindow", "Clear Graph"))
        self.lbl_limit_2.setText(_translate("MainWindow", "Set Limits"))
        self.comment_label.setText(_translate("MainWindow", "Comments"))
        self.btn_Clear_2.setText(_translate("MainWindow", "Clear Comments"))
        self.menuProfilometer.setTitle(_translate("MainWindow", "Profilometer"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuTIlt_Correction.setTitle(_translate("MainWindow", "TIlt Correction"))
        self.action_File.setText(_translate("MainWindow", "&File"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.actionTilt_Correct.setText(_translate("MainWindow", "Tilt Correct"))
        self.actionLoad.setText(_translate("MainWindow", "&Load"))
        self.action_Print.setText(_translate("MainWindow", "&Print"))
        self.action_Close.setText(_translate("MainWindow", "&Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

