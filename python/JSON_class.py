import numpy as np
import scipy.interpolate as ip

class graph_maker:
    def __init__(self, keypoint, mov_x, mov_y, side_x, side_y):
        self.keypoint = keypoint

        self.splX, self.splX_x = self.all(mov_x,keypoint)
        self.splY, self.splY_x = self.all(mov_y,keypoint)
        self.splX_s, self.splX_sx = self.all(side_x,keypoint)
        self.splY_s, self.splY_sx = x =self.all(side_y,keypoint)


    def all(self, mov, key):
        self.begining_zero(mov,key)
        result = self.middle_zero(mov,key)
        npr = np.asarray(result)
        a = ip.UnivariateSpline(range(len(npr)),npr)
        b = np.linspace(0,range(len(npr)),10000)
        return a,b


    def begining_zero(self, mov, key):
        for i in range(len(mov)):
            if((mov[i][key] > 0)):
                for j in range (0, i):
                    mov[j][key] = mov[i][key]
                return

    def middle_zero(self, mov,key):
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

        return pin   

        
        
