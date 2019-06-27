 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# /home/profilometer/profilometer_main.py
#
#  class that adds calibration functionality
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

import numpy as np 
import os
import matplotlib.pyplot as plt




class Calibration():

    

    def __init__(self):
        self.calibration_file_path = 'calibration_file'
        self.load_calibration_file(self.get_calibration_filename())
        self.norm_distance = self.normalize(self.dists)  

    def get_calibration_filename(self):
        filename = None
        with open(self.calibration_file_path, 'r') as cal:
            filename = cal.read()
        return filename

    def load_calibration_file(self,filename):
        try:
            self.pos, self.dists, self.ints = np.loadtxt(filename, unpack=True)
        except Exception as e:
            self.pos, self.dists, self.ints = ([],[],[])
            print(e)

    def change_calibration_file(self,filename):
        with open(self.calibration_file_path,'w') as cal:
            cal.write(filename)
        self.load_calibration_file(self.get_calibration_filename())

    def normalize(self,distance_array):
        return distance_array-np.mean(distance_array)
  
    def interpolation(self,input):
        return np.interp(input,self.pos,self.dists)

    def plot_data(self):
        plt.plot(self.pos,self.dists,'-r')
        plt.plot(self.pos,self.normalize(self.dists),'-p')
        plt.show()


