#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:05:24 2018

@author: scannerone
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon
import scan
import numpy as np
import time

class Laser_scan(QObject):
    values = pyqtSignal(float,float,float)
    end = pyqtSignal()
    
    
    def __init__(self,nstep,distance,socket,serial,connected=True):
        QtCore.QThread.__init__(self)
        #self.s,self.ser = scan.init_devices()
        self.connected = connected
        self.nstep = nstep
        self.distance = distance
        self.start = 0
        self.STOP_BUTTON_PRESSED = False
        self.socket = socket
        self.serial = serial
        
        
    def run_laser(self):
        
        if self.connected:
            self.s,self.ser = scan.init_devices(rehome=False)
            #self.ser.write(b'SD,SC,3\r')
            for x in range(int(self.nstep)):
                if not self.STOP_BUTTON_PRESSED:
                    #swithch these two for random plot
                    posit,dist,inty = scan.scan(self.nstep,self.distance,self.socket,self.serial)
                    self.values.emit(posit,dist,inty)
                    #self.values.connect(self.print_things)
                else:
                    pass
            
        else:
            for x in range(int(self.nstep)):
                if not self.STOP_BUTTON_PRESSED:
                    posit,dist,inty = self.fake_laser()
                    print (posit,dist,inty)#import pdb; pdb.set_trace(
                    self.values.emit(posit,dist,inty)
                    self.values.connect(self.print_things)
                    time.sleep(1)
                
        self.end.emit()
         
    def print_things(posi,dis,iny):  
        print (posi,dis,iny, 'from laser_scan')        
            
    def run(s0elf):
        # your logic here
        self.run_laser()
        
    def fake_laser(self):
        return np.random.randint(-10,10), np.random.randint(0,100),np.random.randint(150,250)