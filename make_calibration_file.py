#python3
import numpy as np 


def make_calibration():
    pos = np.linspace(0,200,1000)
    dist = np.zeros(1000)#np.random.random(1000)*200 -100
    ints = np.random.randint(200,250,1000)
    comments = 'Calibration file'
    head = comments+'\n'+'\tPosition (mm)     Distance (microns)    Light Intensity (0-255)'
    filename = 'data.txt'
    np.savetxt(filename,np.c_[pos,dist,ints],header=head)

make_calibration()