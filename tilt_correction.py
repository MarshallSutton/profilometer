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

tilt_slope = .03

def tilt_corr(xi,yi):
    if len(xi)!=len(yi):
        return yi
    fulcrum = (xi[-1]-xi[0])/2
    A = np.array([ xi, np.ones(len(xi))])
    Y = np.array(yi)
    X = np.array(xi)
    w = np.linalg.lstsq(A.T,Y)[0] # obtaining the parameters
    line = w[0]*A[0,:]+w[1]
    Yp = Y+w[0]*(fulcrum-X)
    
    print(w[0],w[1])
    return Yp,line, Y

def tilt_corr_fulcrum(xi,yi,fulcrum):
    if len(xi)!=len(yi):
        return yi
    #tilt = np.arange(100)*1.2-20
    
    A = np.array([ xi, np.ones(len(xi))])
    Y = np.array(yi)
    w = np.linalg.lstsq(A.T,Y)[0] # obtaining the parameters
    line = w[0]*A[0,:]+w[1]
    #yi[xi<fulcrum]= yi[xi<fulcrum]+w[0]*fulcrum+w[1]-w[0]*w[0]*xi[xi<fulcrum]-w[1]
    #yi[xi>=fulcrum] = yi[xi>=fulcrum]+w[0]*xi[xi>=fulcrum]+w[1] 
    yi = yi+w[0]*(fulcrum-xi)
    
    print(w[0],w[1])
    return Yp,line,Y

if __name__ == '__main__':
    xi = np.arange(100)
    yi = np.random.rand(100)
    yj = tilt_slope*xi+yi+1
    
    Yp,line,Y = tilt_corr(xi,yj)
    print(Yp[:10])
    plt.plot(xi,Y,color='blue',label='Data')
    plt.plot(xi,Yp,color='red',label = 'Tilt Corrected Data')
    plt.plot(xi,line,color='green',label = 'Best Fit')
    plt.legend()
    plt.ylim(-2,10)
    plt.show()
    