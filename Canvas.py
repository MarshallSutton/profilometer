#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:03:17 2018
"""
# /home/profilometer/Canvas.py
#
# Uses Matplotlib and QT Figure canvas to create and animate plots.
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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FingureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PyQt5 import QtCore
import numpy as np
import time
from laser_scan import Laser_scan
import tilt_correction as tilt
from calibration import Calibration
class Canvas(FingureCanvas):
    
    
    def __init__(self, parent = None, width =7, height = 4.5, dpi = 100):
        self.fig = Figure(figsize=(width, height),constrained_layout = True)
        FingureCanvas.__init__(self, self.fig)
        self.setParent(parent) 
        spec = gridspec.GridSpec(ncols=1,nrows=3, figure=self.fig)
        self.dists = []
        self.ints = []
        self.pos = np.arange(10)
        self.xstart = 0
        self.xend = 100
        gridspec.GridSpec(3,1)
        
        self.ax = []
        self.ax.append(self.fig.add_subplot(spec[:2,0]))
        self.ax.append(self.fig.add_subplot(spec[2,0]))
        self.ax[0].set(ylim=(-10,10))
        self.ax[1].set(ylim=(50,260))
        self.ax[1].set_xlabel('Position (mm)')
        self.ax[0].set_ylabel('Distance ('+r'$\mu$'+'m)')
        self.ax[1].set_ylabel('Light Intensity (0-255)')
        self.ax[1].grid(True)
        self.ax[0].grid(True)
        self.start = 0
        self.ax[0].set(xlim=(self.start,self.start+100))
        self.ax[1].set(xlim=(self.start,self.start+100))
        self.qthread = None
        self.laserscan = None
        self.legend = None
        self.calibrate = Calibration()
        
          
       
    def update_graph(self,posit,dist,inty):
        self.dists.append(dist)
        self.pos.append(posit)
        self.ints.append(inty)
        if len(self.pos) <= 1:
            self.resizeY(self.dists[0]-30 ,self.dists[0]+30)
        self.animate2()
   
    def animate2(self):
        #print(self.pos,self.dists,self.ints)
        print(len(self.dists))
        self.ax[0].lines = [] 
        self.ax[0].plot(self.pos[:len(self.dists)],self.dists,'b-o',markersize=3)
        self.ax[1].lines = []
        self.ax[1].plot(self.pos[:len(self.dists)],self.ints,'r-o',markersize=3)
        self.draw()

            
    def laser(self,nstep,distance,connected):
        self.dists = []
        self.ints = []
        self.pos = []#range(0,distance,int(distance/nstep))
        self.laserscan = Laser_scan(nstep,distance,connected)
        self.qthread = QtCore.QThread()
        self.laserscan.moveToThread(self.qthread)
        self.qthread.started.connect(self.laserscan.run_laser)
           
        self.laserscan.values.connect(self.update_graph)
        self.qthread.start()
        self.laserscan.end.connect(self.qthread.quit)
        
    def laser_stop(self):
        if self.qthread is not None:  
            self.qthread.quit()
            self.laserscan.STOP_BUTTON_PRESSED = True
        
    def resizeX(self,start,end):
        self.ax[0].set(xlim=(start,end))
        self.ax[1].set(xlim=(start,end))
        self.draw()
        
    def resizeY(self,start,end):
        print(start,end)
        self.ax[0].set_ylim(start,end)
        self.draw()
        
    def resizeY_intensity(self,start,end):
        print('intensity',start,end)
        self.ax[1].set_ylim(start,end)
        self.draw()
        
        
    def correct_tilt(self):
        Yp,line,Y = tilt.tilt_corr(self.pos,self.dists)
        self.ax[0].lines = []
        self.dists = Yp
        self.ax[0].plot(self.pos[:len(self.dists)],Y,'g-o',markersize=3,
                       label='before correction')
        #self.legend = self.ax[0].legend()
        self.animate2()

    def calibrate_data(self):
        old_dists = self.dists
        self.dists = self.dists+self.calibrate.interpolation(self.pos)
        self.ax[0].lines = []
        self.ax[0].plot(self.pos[:len(old_dists)],old_dists,'m-o',markersize=3,
                       label='before calibration')  
        self.animate2() 
            
    def clear(self):
        self.dists = []
        self.ints = []
        self.pos = []
        self.ax[0].lines = []
        self.ax[1].lines = []
        self.draw()
        #self.legend.remove()
        #self.animate2()
        
    def save(self,filename,comments='None'):
        head = comments+'\n'+'\tPosition (mm)     Distance (microns)    Light Intensity (0-255)'
        distsnp = np.asarray(self.dists)
        intsnp = np.asarray(self.ints)
        posnp = np.asarray(self.pos)
        np.savetxt(filename,np.c_[posnp,distsnp,intsnp],header=head,fmt=['%11.4f','%20.1f','%20.0d'])
        
        
    def load(self,filename):
        self.clear()
        self.pos, self.dists,self.ints= np.loadtxt(filename,unpack=True)
        self.resizeY(self.dists[0]-30,self.dists[0]+30)
        self.resizeX(self.pos[0],self.pos[-1])
        self.animate2()
        
    def add_title(self,title):
        self.fig.suptitle(title)
        
    def print_fig(self,filename):
        self.fig.set_size_inches(10.5,8)
        self.fig.savefig(filename+'.pdf', dpi=300, orientation = 'landscape',
                         papertype= 'letter')
        self.fig.set_size_inches(7,4.5)
        
     #def set_calibration(self,)
        
        
  
        
        
        
    def fake_laser(self):
        return np.random.randint(-10,10), np.random.randint(0,100),np.random.randint(150,250)
    
if __name__ == '__main__':
    canvas = Canvas()
    canvas.fig.show()
    