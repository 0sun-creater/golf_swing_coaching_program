import json
import numpy as np
import scipy.interpolate as ip

from matplotlib import pyplot as plt


def make(mov_x,mov_y):
    
    def begining_zero(mov, key):
        for i in range(len(mov)):
            if((mov[i][key] > 0)):
                for j in range (0, i):
                    mov[j][key] = mov[i][key]
                return

    def middle_zero(mov,key):
        pin =[]
        cnt = 0
        key_max = 0
        key_min = 999999
            
        for b in range(len(mov)):
            if (mov[b][key] == 0) and (b != 0):
                while (mov[(b+cnt)][key]) == 0:
                    cnt = cnt + 1
                    if ((b+cnt) == len(mov)):
                        mov[b][key] =  mov[b-1][key]
                        break
                    if (b + cnt) == (len(mov)-1):
                        mov[b][key] =  mov[b-1][key]
                        break
                    if (mov[(b+cnt)][key]) > 0:
                        mov[b][key] =  (mov[b-1][key] + mov[b+cnt][key]) / 2                
                        break
                cnt = 0
            pin.append(mov[b][key])
        key_max = max(pin)
        key_min = min(pin)       
            
        return pin, key_max, key_min

    pin4_x=[]
    pin4_y=[]
    pin7_x=[]
    pin7_y=[]

    begining_zero(mov_x, 4)
    begining_zero(mov_y, 4)
    begining_zero(mov_x, 7)
    begining_zero(mov_y, 7)


    pin4_x, k4_x_max, k4_x_min = middle_zero(mov_x,4)
    pin4_y, k4_y_max, k4_y_min = middle_zero(mov_y,4)
    pin7_x, k7_x_max, k7_x_min = middle_zero(mov_x,7)
    pin7_y, k7_y_max, k7_y_min = middle_zero(mov_y,7)
    
    
    x_min=min(k4_x_min,k7_x_min)
    x_max=max(k4_x_max,k7_x_max)
    y_min=min(k4_y_min,k7_y_min)
    y_max=max(k4_y_max,k7_y_max)


    #SET Relative Error
    Re_x = (x_max - x_min) * 0.17
    Re_y = (y_max - y_min) * 0.17


    #오차가 크면 0으로 내리기
    for k in range(len(pin4_x)):
        for b in range(len(pin4_x)):
            if ( (abs(pin4_x[b] - pin7_x[b])) > Re_x):
                pin4_x[b] = 0
                pin7_x[b] = 0
            if ( (abs(pin4_y[b] - pin7_y[b])) > Re_y):
                pin4_y[b] = 0
                pin7_y[b] = 0



    Tnpdx4 = np.expand_dims(np.asarray(pin4_x),axis=0).transpose()
    Tnpdy4 = np.expand_dims(np.asarray(pin4_y),axis=0).transpose()
    Tnpdx7 = np.expand_dims(np.asarray(pin7_x),axis=0).transpose()
    Tnpdy7 = np.expand_dims(np.asarray(pin7_y),axis=0).transpose()

    begining_zero(Tnpdx4,0)
    begining_zero(Tnpdy4,0)
    begining_zero(Tnpdx7,0)
    begining_zero(Tnpdy7,0)

    pin4_x, trash_max, trash_min = middle_zero(Tnpdx4,0)
    pin4_y, trash_max, trash_min = middle_zero(Tnpdy4,0)
    pin7_x, trash_max, trash_min = middle_zero(Tnpdx7,0)
    pin7_y, trash_max, trash_min = middle_zero(Tnpdy7,0)


    '''
    plt.figure()
    plt.plot(pin4_x[:],'.',color='r')
    plt.plot(pin4_y[:],'.',color='g')

    plt.plot(pin7_x[:],'.',color='b')
    plt.plot(pin7_y[:],'.',color='y')

    '''
    return pin4_x, pin4_y
