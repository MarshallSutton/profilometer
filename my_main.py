#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 08:15:29 2018
"""
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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QThread, pyqtSlot
import numpy as np
import sys

from Canvas import Canvas



    
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
        
        #self.s,self.ser = scan.init_devices()

        self.canvas = Canvas(parent = self.ui.widget)
        self.ui.widget.show(  )
        
        self.ui.btn_SCAN.clicked.connect(self.scan_button)
        self.ui.btn_go1.clicked.connect(self.goto1)
        self.ui.btn_goto2.clicked.connect(self.goto2)
        self.ui.btn_goto3.clicked.connect(self.goto3)
        self.ui.btn_goto3_2.clicked.connect(self.goto4)
        self.ui.btn_Clear.clicked.connect(self.clear)
        self.ui.toolButton_x_dec.clicked.connect(self.dec_x)
        self.ui.toolButton_x_inc.clicked.connect(self.inc_x)
        self.ui.toolButton_y_dec.clicked.connect(self.dec_y)
        self.ui.toolButton_y_inc.clicked.connect(self.inc_y)
        self.ui.toolButton_y_dec_by_factor.clicked.connect(self.dec_y_fac)
        self.ui.toolButton_y_inc_by_factor.clicked.connect(self.inc_y_fac)
        self.ui.actionTilt_Correct.triggered.connect(self.canvas.correct_tilt)
        self.ui.action_Save.triggered.connect(self.save)
        self.ui.actionLoad.triggered.connect(self.load)
        self.MainWindow.show()
        sys.exit(self.app.exec_()) 
        
    def goto1(self):
            loc = self.ui.sb_goto1.value()
            scan.move_position(loc,self.speed,self.s)
    
    def goto2(self):
            loc = self.ui.sb_goto2.value()
            scan.move_position(loc,self.speed,self.s)
            
    def goto3(self):
            loc = self.ui.sb_goto3.value()
            scan.move_position(loc,self.speed,self.s)
            
    def goto4(self):
            loc = self.ui.sb_goto3_2.value()
            scan.move_position(loc,self.speed,self.s)
            
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
        self.end = self.start + 100
        self.canvas.resizeX(self.start,self.end)
        self.canvas.laser(nsamples,distance,connected=True)
        self.app.processEvents()
        
    def clear(self):
        self.canvas.clear()
        
    def save(self):
        saved, _ = QtWidgets.QFileDialog.getSaveFileName()
        print(saved)
        self.canvas.save(saved)
        
    def load(self):
        loaded,_ = QtWidgets.QFileDialog.getOpenFileName()
        self.canvas.load(loaded)
       
    

if __name__ == "__main__":
    MainWindow_EXEC()
    
