#!/usr/bin/env python3
 #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# /home/profilometer/profilometer_main.py
#
# This class contains methods and objects for creating a calibration file
 #and applying that file to measurements made with the profilometer.
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
 
import sys
import os
import numpy as np
import math
class Calibration():
    
    def __init__(self):
        self.calibration_file_path = 'calibration/current_file'
        self.pos = []
        self.dists = []
        self.ints = []
        
        
        pass
    
    def load_calibration(self):
        with open(self.calibration_file_path,'r') as calibration:
            calibration_file = calibration.readlines()
            pos,dists,ints= np.loadtxt(calibration_file,unpack=True)
            return self.pos,self.dists,self.ints
        
    def set_calibration_file(self,calibration_file):
        with open(self.calibration_file_path,'w') as calibration:
            calibration.write(calibration_file)
            
    def apply_calibration(self,meas,pos):
        matches = abs(pos-self.pos)
        

