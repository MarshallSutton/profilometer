#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:27:10 2018

@author: msutton1
"""

"""
=====
Decay
=====

This example showcases a sinusoidal decay animation.
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scan
import threading


class plot():
    def __init__(self,fig):
        self.ax = []
        self.fig=fig
        self.ax.append(self.fig.add_subplot(2,1,1))
        self.ax.append(self.fig.add_subplot(2,1,2))
        self.ax[0].set(ylim=(-20,2))
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
        #self.s,self.ser= scan.init_devices()
        self.start = 0#scan.get_pos(self.s)

    def fake_laser(self):
        return 400*np.random.rand()-200, np.random.randint(0,100),np.random.randint(150,250)
    

# Run laser and return lists of values
    def run_laser(self,nstep,distance):
        for x in range(int(nstep)):
            #dist, posit, inty = scan.scan(nstep,distance,self.s,self.ser)
            dist, posit, inty = self.fake_laser()
            self.dists.append(dist)
            print(dist)
            self.ints.append(inty)
            print(inty)
            self.pos.append(self.pos[:-1]+1)
    
    def start_thread(self,nstep,distance):
        self.thread = threading.Thread(target = self.run_laser,args=(nstep,distance))   
        self.thread.start() 

    def animate2(self,i):
        self.ax[1].set(xlim=(self.start,self.start+50))
        self.ax[0].plot(self.pos,self.dists,'b-o')
        self.ax[1].plot(self.pos,self.ints,'r-o')
        
    def plot(self,nsteps,distance):
        self.start_thread(nsteps,distance)
        ani = FuncAnimation(self.fig, self.animate2,interval=1000)
        self.ax[1].set(xlim=(self.start,self.start+50))
        self.ax[0].plot(self.pos,self.dists,'b-o')
        self.ax[1].plot(self.pos,self.ints,'r-o')
        plt.show()

    
            
if __name__ == '__main__':
    fig = plt.figure()
    laserplot = plot(fig)
    laserplot.plot(10,10)
