#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:27:10 2018
"""
# home/profilomete/animat.py
#
# This class contains the methods and other functionality for
# the Axis Scan GUI window
#
# Author: Leor Bleier
# NASA Goddard Space Flight Center
# Flight Software Systems Branch - Code 582
# Contact: Leor.Z.Bleier@nasa.gov
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
# Last update: 12/21/2018

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scan
import threading


class plot():
    def __init__(self,fig,s,ser):
        self.s = s
        self.ser = ser
        self.fig,self.ax = plt.subplots(2,1,sharex=True)
        self.ax[0].set(ylim=(-40,2))
        self.ax[1].set(ylim=(50,260))
        self.ax[0].set(xlim=(-40,80))
        self.ax[1].set_xlabel('Distance (mm)')
        self.ax[0].set_ylabel('Position ('+r'$\mu$'+'m)')
        self.ax[1].set_ylabel('Light Intensity (0-255)')
        self.ax[1].grid(True)
        self.ax[0].grid(True)
        self.dists = []
        self.ints = []
        self.pos = []
        self.start = scan.get_pos(self.s)
        
    def fake_laser(self):
        return np.random.randint(-12,0), np.random.randint(0,100),np.random.randint(150,250)
    
    def fake_pos(self):
        if self.pos:
            self.pos.append(self.pos[-1]+10)
        else:
            self.pos.append(0)
    # Run laser and return lists of values
    def run_laser(self,nstep,distance):
        for x in range(int(nstep)):
            
            #swithch these two for random plot
            dist, posit, inty = scan.scan(nstep,distance,self.s,self.ser)
            #dist, posit, inty = self.fake_laser()
            self.dists.append(dist)
            print(dist)
            self.ints.append(inty)
            print(inty)
            
            #switch these two for random plot
            self.pos.append(scan.get_pos(self.s))
            #self.fake_pos()
            
    def start_thread(self,nstep,distance):
        self.thread = threading.Thread(target = self.run_laser,args=(nstep,distance))   
        self.thread.start() 

    def animate2(self,i):
        self.ax[1].set(xlim=(self.start,self.start+50))
        self.ax[0].plot(self.pos,self.dists,'b-o')
        self.ax[1].plot(self.pos,self.ints,'r-o')
        
    def plot(self,nsteps,distance):
        self.start_thread(nsteps,distance)
        self.ax[1].set(xlim=(self.start,self.start+50))
        ani = FuncAnimation(self.fig, self.animate2,interval=1000)
        plt.show()

    
            
if __name__ == '__main__':
    laserplot = plot()
    laserplot.plot(10,10)
