import cv2


def make(mov_x,mov_y,key):
    
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
            
        return pin

    begining_zero(mov_x, key)
    begining_zero(mov_y, key)


    pin_x = middle_zero(mov_x,key)
    pin_y = middle_zero(mov_y,key)


    return pin_x, pin_y
