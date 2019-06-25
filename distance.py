#!python3

# /home/profilometer/distance.py
#
# This script kicks of the profilometer main GUI.
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

from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QObject
import scan
import numpy as np
import time

class Distance(QObject):
    dist = pyqtSignal(float)
    end = pyqtSignal(bool)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.stop_scanner = True

    def get_distance(self):
        try:
            distance = scan.laser_connect()[0]
        except:
            distance = 0
        self.dist.emit(distance)

    def loop_distance(self):
        while self.stop_scanner:
            self.get_distance()
            time.sleep(.5)

    def stop_loop(self):
        self.stop_scanner = False
        self.end.emit()
