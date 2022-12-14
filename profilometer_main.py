 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# /home/profilometer/profilometer_main.py
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
from forms.Ui_calibration import Ui_CalibrationWindow

from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtCore import pyqtSignal, QObject, QThread, pyqtSlot, QTimer
import sys, time, datetime, threading
import os
from Canvas import Canvas

from calibration import Calibration
from distance import Distance

    
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

        self.canvas = Canvas(parent = self.ui.widget)
        self.calibrate = Calibration()
        self.ui.widget.show(  )
        
        self.ui.btn_SCAN.clicked.connect(self.scan_button)
        self.ui.btn_go1.clicked.connect(self.goto1)
        self.ui.btn_goto2.clicked.connect(self.goto2)
        self.ui.btn_goto3.clicked.connect(self.goto3)
        self.ui.up_btn.clicked.connect(self.move_up)
        self.ui.down_btn.clicked.connect(self.move_down)
        self.ui.btn_Clear.clicked.connect(self.clear)
        self.ui.btn_stop.clicked.connect(self.stop_scan)
        
        self.ui.sb_lower_limit.valueChanged.connect(self.changeY)
        self.ui.sb_upper_limit.valueChanged.connect(self.changeY)
        self.ui.sb_lower_limit_intensity.valueChanged.connect(self.changeY_intensity)
        self.ui.sb_upper_limit_intensity.valueChanged.connect(self.changeY_intensity)
        self.ui.sb_left.valueChanged.connect(self.changeX)
        self.ui.sb_right.valueChanged.connect(self.changeX)
        self.ui.actionTilt_Correct.triggered.connect(self.canvas.correct_tilt)
        self.ui.action_Save.triggered.connect(self.save)
        self.ui.actionLoad.triggered.connect(self.load)
        self.ui.action_Print.triggered.connect(self.qt_print)
        self.ui.action_Close.triggered.connect(self.close)
        self.ui.actionCalibrate.triggered.connect(self.update_calibration_file)
        self.ui.actionApply_Calibration.triggered.connect(self.apply_calibration)
        self.ui.actionInitialize_Axis.triggered.connect(self.rehome)
        self.ui.limit_lable.setHidden(True)
        self.menu_calibration_path()

        self.distance_thread = None
        self.update_spinbox(scan.get_pos())
        self.update_thread()
        

        
        
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def menu_calibration_path(self):
        
        try:
            calibrate = Calibration()
            filename = self.canvas.calibrate.get_calibration_filename()
            self.ui.actioncalibration_path.setText(filename)
        except Exception as e:
            print('no file listed ',e)

    def rehome(self):
        scan.send_cmd('HOME\n')
        self.update_spinbox(scan.get_pos())
        #self.update_distance()
        
        
    def goto1(self):
        loc = self.ui.sb_goto1.value()
        pos = self.moving(loc)
        self.update_spinbox(pos)
        #self.update_distance()
            #scan.move_position(loc,self.speed)
    
    def goto2(self):
        loc = self.ui.sb_goto2.value()
        pos = self.moving(loc)
        self.update_spinbox(pos)
        #self.update_distance()

    def goto3(self):
        loc = self.ui.sb_goto3.value()
        pos = self.moving(loc)
        self.update_spinbox(pos)
        #self.update_distance()
            
    def move_up(self):
        loc = self.ui.sb_goto3_2.value()
        scan.moveinc(-loc,self.speed)
        self.update_spinbox(scan.get_pos())

    def update_distance(self,distance):
        self.ui.dist_value.setValue(distance)
        
    def update_thread(self):
        self.distance_thread = Distance()
        self.qthread3 = QtCore.QThread()
        self.distance_thread.moveToThread(self.qthread3)
        self.qthread3.started.connect(self.distance_thread.loop_distance)
        self.distance_thread.dist.connect(self.update_distance)
        self.qthread3.start()
        self.distance_thread.end.connect(self.qthread3.quit)
            
    def move_down(self):
        loc = self.ui.sb_goto3_2.value()
        scan.moveinc(loc,self.speed)
        self.update_spinbox(scan.get_pos())
        #self.update_distance()
            
    def moving(self,loc):
        #pool = mp.Pool(processes=1)
        result = scan.move_position(loc,self.speed)
        #self.update_distance()         
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
        self.distance_thread.stop_loop()
        self.qthread3.quit()
        self.canvas.clear()
        self.ui.btn_SCAN.setDisabled(True)
        nsamples = self.ui.sb_Npoints.value()
        interval = self.ui.sb_interval.value()
        distance = self.ui.sb_distance.value()
        nsamp, interva, dist = self.pick2(nsamples, interval, distance)
        self.ui.sb_distance.setValue(dist)
        self.ui.sb_Npoints.setValue(nsamp)
        self.ui.sb_interval.setValue(interva)
        self.start = scan.get_pos()
        self.end = self.start + nsamp*interva
        self.canvas.resizeX(self.start,self.end)
        self.canvas.laser(nsamp,interva,connected=True)
        self.canvas.laserscan.position.connect(self.update_spinbox)
        self.canvas.laserscan.end.connect(self.enable_scan)
        
        
        
    def enable_scan(self):
        self.ui.btn_SCAN.setEnabled(True)
        self.auto_save()
        
    def stop_scan(self):
        self.canvas.laser_stop()
        
    def close(self):
        self.stop_scan()
        self.MainWindow.close()
        
    def set_spin_box_values(self):
        self.ui.sb_lower_limit.setValue(self.canvas.ax[1].get_ylim()[0])
        self.ui.sb_upper_limit.setValue(self.canvas.ax[1].get_ylim()[1])
        self.ui.sb_left.setValue(self.canvas.ax[0].get_xlim()[0])
        self.ui.sb_right.setVprint(scan.get_pos())
        #alue(self.canvas.ax[0].get_xlim()[1])-10.000000
        
    def clear(self):
        self.canvas.clear()
        
    def save(self,saved = None):
        if not saved:
            saved, _ = QtWidgets.QFileDialog.getSaveFileName()
        #print(saved)
        title = os.path.basename(saved)
        comments = self.ui.comments.toPlainText()
        self.canvas.save(saved,comments=comments)
        #self.canvas.print_fig(saved)
        
    def load(self):
        try:
            loaded,_ = QtWidgets.QFileDialog.getOpenFileName()
            self.canvas.load(loaded)
            self.ui.comments.setPlainText(self.get_comments(loaded))
        except Exception as e:
            print('unable to load because %s' % e.message())
            
    def get_comments(self,filename):
        with open(filename,'r') as name:
            comment = name.readlines()[0]
            if comment[:9] == '\n\tDistance':
                return ''
            else:
                comment=comment[2:]
            return comment
        
    def qt_print(self):
        printer= QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog()
        if (dialog.exec_() !=QtWidgets.QDialog.Accepted):
            return
        screen = self.MainWindow
        painter = QtGui.QPainter()
        painter.begin(printer)
        print(printer.paperRect().x())
        XScale = (printer.pageRect().width()/(screen.width()))
        YScale = (printer.pageRect().height()/(screen.height()))
        scale = min(XScale,YScale)
        painter.translate((printer.paperRect().x()) + 
        (printer.pageRect().width()/2),(printer.paperRect().y()) +
        (printer.pageRect().height()/2))
        painter.scale(scale,scale)
        painter.translate(-1*screen.width()/2,-1*screen.height()/2)
        screen.render(painter)
        painter.end()
       
    def changeY(self):
        self.canvas.resizeY(self.ui.sb_lower_limit.value(),
                            self.ui.sb_upper_limit.value())
        
    def changeY_intensity(self):
        self.canvas.resizeY_intensity(self.ui.sb_lower_limit_intensity.value(),
                            self.ui.sb_upper_limit_intensity.value())
            
        
    def changeX(self):
        self.canvas.resizeX(self.ui.sb_left.value(),
                            self.ui.sb_right.value())
        
    def update_current_position(self):
        # Not used. May be used later to implement threads
        self.laser_pos = Position()
        self.qthread2 = QThread()
        self.laser_pos.moveToThread(self.qthread2)
        self.qthread2.started.connect(self.laser_pos.get_position)
        self.laser_pos.value.connect(self.update_spinbox)
        self.qthread2.start()
        self.qthread2.quit()
        self.app.processEvents()
        
    def update_spinbox(self,position):
        try:
            self.ui.curr_position.setValue(position)
            fault = scan.check_fault()
            if fault == 32 or fault == 16:
                self.ui.limit_lable.setVisible(True)
            else:
                self.ui.limit_lable.setVisible(False)
                print('not at end')
        except:
            pass
    
    def pick2(self,num_points,interval,distance):
        if num_points != 0 and interval != 0:
            dist = num_points*interval
            return num_points, interval, dist
        if num_points != 0 and distance !=0 and interval == 0:
            return num_points, distance/num_points, distance
        if num_points == 0 and distance !=0 and interval != 0:
            return int(distance/interval), interval, distance
        else:
            return 20,1.0,10
        
    def auto_save(self):
        today = datetime.datetime.now()
        file_name = 'scan-%s-%s-%s-%s-%s-%s.txt' % (str(today.year),
                                                 str(today.month),
                                                 str(today.day),
                                                 str(today.hour),
                                                 str(today.minute),
                                                 str(today.second))
        path = os.path.join('/home/scannerone/autosave/',file_name)
        self.ui.autosave_path.setText(path)
        self.save(saved=path)
        
    def update_calibration_file(self):
        calibration_path, _ = QtWidgets.QFileDialog.getOpenFileName()
        if calibration_path:
            self.calibrate.change_calibration_file(calibration_path)
        self.menu_calibration_path()
    
    def apply_calibration(self):
        self.canvas.calibrate_data()

    
        
    
if __name__ == "__main__":
    MainWindow_EXEC()
    
