#!/usr/bin/env python3

#The main control file for my GUI
#Pyqt imports
from PyQt5.QtGui import QDialog
from forms.Ui_main_form import Ui_MainWindow
from PyQt5 import QtWidgets

#Backend imports
import scan
class ImageDialog(QDialog, Ui_MainWindow):
    def __init__(self):
        super(ImageDialog, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Make some local modifications.
        self.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        self.btn_SCAN.clicked.connect(scan.scan)
        self.btn_goto1.clicked.connect(scan.move_position)
        self.btn_goto2.clicked.connect(scan.move_position)
        
        #run main form
        
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())