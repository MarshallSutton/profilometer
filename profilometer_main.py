 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# /home/profilometer/my_main.py
#
# This script kicks of the profilometer main GUI.
#
# Author: Marshall Sutton
# NASA Goddard Space Flight Center
# Science Data Systems Branch - Code 586
# Contact: marsall.h.sutton@nasa.gov
#
# Copyright (Unpublished--all rights reserved under the copyright
# laws of the United States), U.S. Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# No copyright is claimed in the United States under Title 17, U.S. Code.
#
# DISCLAIMER:
#
# THE SOFTWARE IS PROVIDED 'AS IS' WITHOUT ANY WARRANTY OF ANY KIND,
# EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT
# LIMITED TO, ANY WARRANTY THAT THE SOFTWARE WILL CONFORM TO
# SPECIFICATIONS, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE, AND FREEDOM FROM INFRINGEMENT, AND ANY
# WARRANTY THAT THE DOCUMENTATION WILL CONFORM TO THE SOFTWARE, OR
# ANY WARRANTY THAT THE SOFTWARE WILL BE ERROR FREE. IN NO EVENT
# SHALL NASA BE LIABLE FOR ANY DAMAGES, INCLUDING, BUT NOT LIMITED
# TO, DIRECT, INDIRECT, SPECIAL OR CONSEQUENTIAL DAMAGES, ARISING
# OUT OF, RESULTING FROM, OR IN ANY WAY CONNECTED WITH THIS SOFTWARE
# WHETHER OR NOT BASED UPON WARRANTY, CONTRACT, TORT , OR OTHERWISE,
# WHETHER OR NOT INJURY WAS SUSTAINED BY PERSONS OR PROPERTY OR
# OTHERWISE, AND WHETHER OR NOT LOSS WAS SUSTAINED FROM, OR AROSE
# OUT OF THE RESULTS OF, OR USE OF, THE SOFTWARE OR SERVICES
# PROVIDED HEREUNDER.
#
# Last update: 2/4/2019

import scan
#from animat import plot
from forms.Ui_main_form import Ui_MainWindow

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtCore import pyqtSignal, QObject, QThread, pyqtSlot, QTimer
import sys, time
import os
from Canvas import Canvas

from Position import Position

    
class MainWindow_EXEC():
   
    def __init__(self,speed =10):
        self.app = QtWidgets.QApplication(sys.argv)
        self.speed = speed
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.start = 0
        self.end = 100 
        self.ystart = -5
        self.yend = 5
        self.timer = None
        
        self.s,self.ser = scan.init_devices(rehome=False)

        self.canvas = Canvas(parent = self.ui.widget)
        self.ui.widget.show(  )
        
        self.ui.btn_SCAN.clicked.connect(self.scan_button)
        self.ui.btn_go1.clicked.connect(self.goto1)
        self.ui.btn_goto2.clicked.connect(self.goto2)
        self.ui.btn_goto3.clicked.connect(self.goto3)
        self.ui.btn_goto3_2.clicked.connect(self.goto4)
        self.ui.btn_Clear.clicked.connect(self.clear)
        
        self.ui.sb_lower_limit.valueChanged.connect(self.changeY)
        self.ui.sb_upper_limit.valueChanged.connect(self.changeY)
        self.ui.sb_left.valueChanged.connect(self.changeX)
        self.ui.sb_right.valueChanged.connect(self.changeX)
        self.ui.actionTilt_Correct.triggered.connect(self.canvas.correct_tilt)
        self.ui.action_Save.triggered.connect(self.save)
        self.ui.actionLoad.triggered.connect(self.load)
        self.ui.action_Print.triggered.connect(self.print_page)
        #self.position_timer()
        #self.update_current_position()# 
        self.update_spinbox(scan.get_pos(self.s))
        
        
        self.MainWindow.show()
        sys.exit(self.app.exec_()) 
        
    def goto1(self):
        loc = self.ui.sb_goto1.value()
        pos = self.moving(loc)
        #scan.get_pos(self.s)
        self.update_spinbox(pos)
            #scan.move_position(loc,self.speed,self.s)
    
    def goto2(self):
        loc = self.ui.sb_goto2.value()
        self.moving(loc)
            #self.update_spinbox()
            #scan.move_positioself.ui.curr_position display(scan.get_pos(self.s))n(loc,self.speed,self.s)
            
    def goto3(self):
        loc = self.ui.sb_goto3.value()
        self.moving(loc)
            #self.update_spinbox()
            #scan.move_position(loc,self.speed,self.s)
            
    def goto4(self):
        loc = self.ui.sb_goto3_2.value()
        self.moving(loc)
            #self.update_spinbox()
            #scan.move_position(loc,self.speed,self.s)
            
    def moving(self,loc):
        #pool = mp.Pool(processes=1)
        result = scan.move_position(loc,self.speed,self.s)         
        return result
        
            
    def dec_x(self):
        self.start*=0.8
        self.end*=0.8
        self.canvas.resizeX(self.start,self.end)
    
    def inc_x(self):
        self.start*=1.2
        self.end*=1.2
        self.canvas.resizeX(self.start,self.end)
        
    def dec_y(self):
        self.ystart-=5.
        self.yend-=5.
        self.canvas.resizeY(self.ystart,self.yend)
    
    def inc_y(self):
        self.ystart+=5
        self.yend+=5
        self.canvas.resizeY(self.ystart,self.yend)
        
    def dec_y_fac(self):
        self.ystart*=0.8
        self.yend*=0.8
        self.canvas.resizeY(self.ystart,self.yend)
    
    def inc_y_fac(self):
        self.ystart*=1.2
        self.yend*=1.2
        self.canvas.resizeY(self.ystart,self.yend)
        
    def scan_button(self):
        self.canvas.clear()
        nsamples = self.ui.sb_Npoints.value()
        distance = self.ui.sb_sample_spacing.value()
        self.start = scan.get_pos(self.s)
        self.end = self.start + distance+10
        self.canvas.resizeX(self.start,self.end)
        self.canvas.laser(nsamples,distance,connected=True)
        #self.set_spin_box_values()
        
    def set_spin_box_values(self):
        self.ui.sb_lower_limit.setValue(self.canvas.ax[1].get_ylim()[0])
        self.ui.sb_upper_limit.setValue(self.canvas.ax[1].get_ylim()[1])
        self.ui.sb_left.setValue(self.canvas.ax[0].get_xlim()[0])
        self.ui.sb_right.setVprint(scan.get_pos(self.s))
        #alue(self.canvas.ax[0].get_xlim()[1])
        
    def clear(self):
        self.canvas.clear()
        
    def save(self):
        saved, _ = QtWidgets.QFileDialog.getSaveFileName()
        #print(saved)
        title = os.path.basename(saved)
        self.canvas.save(saved)
        self.canvas.add_title(title)
        self.canvas.print_fig(saved)
        
    def load(self):
        try:
            loaded,_ = QtWidgets.QFileDialog.getOpenFileName()
            self.canvas.load(loaded)
        except Exception as e:
            print('unable to load because %s' %e.message)
            
    def print_page(self):
        saved, _ = QtWidgets.QFileDialog.getSaveFileName()
        self.canvas.print_fig(saved[:-4])
        cmd = 'gnome-open %s' % saved
        os.system(cmd)
       
    def changeY(self):
        self.canvas.resizeY(self.ui.sb_lower_limit.value(),
                            self.ui.sb_upper_limit.value())
            
        
    def changeX(self):
        self.canvas.resizeX(self.ui.sb_left.value(),
                            self.ui.sb_right.value())
        
    def update_current_position(self):
        self.laser_pos = Position(self.s)
        self.qthread2 = QThread()
        self.laser_pos.moveToThread(self.qthread2)
        self.qthread2.started.connect(self.laser_pos.get_position)
        self.laser_pos.value.connect(self.update_spinbox)
        self.qthread2.start()
        self.qthread2.quit()
        self.app.processEvents()
        
    def update_spinbox(self,position):
        self.ui.curr_position.setValue(position)
        #print(scan.get_pos(self.s))
    

if __name__ == "__main__":
    MainWindow_EXEC()
    
