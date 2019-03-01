#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:57:18 2018

@author: msutton1
"""
# /home/profilometer/tilt_correction.py
#
# This script corrects possible tilt in the stage by subtracting a linear
# regression.
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
import matplotlib.pyplot as plt

def tilt_corr(xi,yi):
    if len(xi)!=len(yi):
        return yi
    #tilt = np.arange(100)*1.2-20
    A = np.array([ xi, np.ones(len(xi))])
    Y = np.array(yi)
    w = np.linalg.lstsq(A.T,Y)[0] # obtaining the parameters
    line = w[0]*A[0,:]#+w[1]
    print(w[0],w[1])
    return Y-line,line,Y

if __name__ == '__main__':
    xi = np.arange(100)
    yi = np.random.rand(100)
    
    Yp,line,Y = tilt_corr(xi,yi)
    print(Yp[:10])
    plt.plot(xi,yi,color='blue')
    plt.plot(xi,Yp,color='red')
    plt.plot(xi,line,color='green')
    plt.show()
    