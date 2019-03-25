#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 15:36:22 2019

@author: scannerone
"""
from PyQt5.QtCore import pyqtSignal, QObject, QThread
import scan
import time

class Position(QObject):
    value = pyqtSignal(float)
    end = pyqtSignal()
    
    def __init__(self,s):
        QThread.__init__(self)
        self.s = s
        
    def get_position(self):
        while True:
            time.sleep(.5)
            print(scan.get_pos(self.s))
            self.value.emit(scan.get_pos(self.s))
        