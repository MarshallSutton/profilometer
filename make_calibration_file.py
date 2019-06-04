#python3
import numpy as np 


def make_calibration():
    pos = np.linspace(0,200,100)
    dist = np.random.random(100)*10 -10
    ints = np.random.randint(200,250,100)
    comments = 'Calibration file'
    head = comments+'\n'+'\tPosition (mm)     Distance (microns)    Light Intensity (0-255)'
    filename = 'data.txt'
    np.savetxt(filename,np.c_[pos,dist,ints],header=head)

make_calibration()