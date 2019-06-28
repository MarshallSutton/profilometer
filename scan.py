
#functions and objects for moving the stage and scanning with the laser
# /home/profilometer/scan.py
#
# 
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
import socket
import serial
import statistics
import numpy as np  
#import matplotlib 
#import matplotlib.pyplot as plt
import random

#from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.figure import Figure


def init_devices(rehome=False):
    s = connect()
    ser = laser_connect()
    enable(s)
    
    if rehome:
        send_cmd('HOME\n',s)
        move_position(100,10,s)
    return s, ser

def scan(nsample,distance):
    """ scans mirror segment nsample times, each sample is 
    distance microns apart. Connects to Laser and motion controller
    """
    positions = []
    distances = []
    intensity = []
    dist, ints = laser_measurement()
    pos = get_pos()
    distances.append(dist)
    intensity.append(ints)
    positions.append(pos)
    
    move = distance
    err = moveinc(move,10,)
    if err !='%':
        print('laser did not move')
    return pos,dist,ints

     
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tcp_ip = '192.168.239.104'
    tcp_port = 10308
    s.connect((tcp_ip,tcp_port))
    return s

def laser_connect():
    ser = serial.Serial('/dev/ttyUSB0')
    print(ser.name)
    ser.timeout = 1
    return ser
    
def send_cmd(cmd):
    socket = connect()
    socket.send(cmd.encode())
    output = socket.recv(4096)
    foutput = int.from_bytes(output[1:], 'big')
    #print(bin(foutput))
    print(output)
    socket.close()
    return output

def get_pos():
    try:
        pos = send_cmd('PCMD\n')
        return float(pos.decode('utf-8').strip('%').strip())
    except:
        return 0
    

def move_position(position,velocity):
    """Moves controller to position (in cm)
    """
    cmd = 'MOVEABS D %s F %s\n' %(position,velocity)
    send_cmd(cmd)
    return get_pos()

def enable():
    send_cmd('ENABLE\n')
   

def moveinc(distance,velocity):
    """
    Move the stage incrementally, distance in milimeters
    """
    cmd = 'MOVEINC D %s F %s\n' %(distance,velocity)
    #print(cmd)
    send_cmd(cmd)
    
    return get_pos()

def sign(string):
    try:
        if string[0]=='+':
            flot = float(string[1:])
        elif string == 'OP':
            flot = 0
        else:
            flot = float(string)
    except Exception as e:
        flot = 0
        print(e)
    return flot
        

def laser_measurement():
    ser = laser_connect()
    
    #ser.write(b'SD,SC,1\r')
    #  ser.write(b'SD,SC,3\r')
    ser.write(b'OP,3\r')
    
    
    meas = ser.readline().decode('ascii').split('\r')
    # meas = ser.read(286).decode('ascii').split('\r')
    print(meas)
    meas.pop(-1)
    values = []
    intensity = []
    position = []
    
    for mea in meas:
        
        meat = mea.split(',')
        print(meat)
        values.append(sign(meat[1]))
        intensity.append(sign(meat[3]))
        position.append(sign(meat[2]))
    try:
        value = values[position.index(0.)]
        intent = intensity[position.index(0.)]
        #value = statistics.mean(values) 
        #intent = statistics.mean(intensity)
        #print(position)
        return value, intent
    except statistics.StatisticsError:
        pass
    ser.close()

def check_fault():
    try:
        pos = send_cmd('AXISFAULT\n')
        return float(pos.decode('utf-8').strip('%').strip())
    except:
        return 0
    
    
if __name__ == "__main__":

    send_cmd('AXISFAULT\n')
    #ser.write(b'VR\r')
    #s.close()
    #print(laser_measurement(ser))
    #scan(5,10,s,ser)
