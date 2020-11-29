import json
import numpy as np
import scipy.interpolate as ip

from matplotlib import pyplot as plt

def read_file(file_number):
    number = -1
    mov_x = [[]]
    mov_y = [[]]
    mov_c = [[]]
    while(True):
        number=number+1
        pos_x =[]
        pos_y =[]
        pos_c =[]
        #filename='golf_pose' + str(file_number)+ '_'+str("%012d"%number)+'_keypoints.json'
        filename='Camera' + str(file_number)+ '_'+str("%012d"%number)+'_keypoints.json'
        try:
            #with open("GOLF_JSON/%s"%filename) as json_file:
            with open("output/%s"%filename) as json_file:
                json_data = json.load(json_file)
                
                try:
                    json_data = json_data['people'][0]['pose_keypoints_2d']
                    
                    for a in range(len(json_data)):

                        if a % 3==0:
                            pos_x.append(json_data[a])
                        elif a % 3==1:
                            pos_y.append(json_data[a])
                        elif a % 3==2:
                            pos_c.append(json_data[a])
                    mov_x.append(pos_x)
                    mov_y.append(pos_y)
                    mov_c.append(pos_c)
                    
                except IndexError:
                    print("No detecting")
                       
        except FileNotFoundError:
            print("All JSON_file read")
            break

    del pos_x
    del pos_y
    del pos_c

    del mov_x[0]
    del mov_y[0]
    del mov_c[0]

    return mov_x, mov_y

def parts(mov_x,mov_y):

    test1=[]
    test2=[] 
    
    test3=[]
    test4=[]


    for i in range(len(mov_x)):
        test1.append(mov_x[i][4])
        test2.append(mov_y[i][4])
        test3.append(mov_x[i][7])
        test4.append(mov_y[i][7])        
 


    '''
    ax = plt.gca()
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)

    

    ############### 원본 plot ###############
    plt.plot(test1[:], '.', color='black')
    plt.plot(test2[:], '.', color='navy')
    plt.plot(test3[:], '.', color='orange')
    plt.plot(test4[:], '.', color='skyblue')
    ########################################

    plt.figure()
    '''    
    ################################### 잡음 잡기 ###################################
    #손 키포인트 4, 7번

    pin4_x=[]  #잡음 잡은 원본 값
    pin4_y=[]
    pin7_x=[]
    pin7_y=[]



    # value for 0
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
            

    begining_zero(mov_x, 4)
    begining_zero(mov_y, 4)
    begining_zero(mov_x, 7)
    begining_zero(mov_y, 7)


    pin4_x, k4_x_max, k4_x_min = middle_zero(mov_x,4)
    pin4_y, k4_y_max, k4_y_min = middle_zero(mov_y,4)
    pin7_x, k7_x_max, k7_x_min = middle_zero(mov_x,7)
    pin7_y, k7_y_max, k7_y_min = middle_zero(mov_y,7)

    top_y = list(pin4_y)
    
    x_min=min(k4_x_min,k7_x_min)
    x_max=max(k4_x_max,k7_x_max)
    y_min=min(k4_y_min,k7_y_min)
    y_max=max(k4_y_max,k7_y_max)


    '''
    --------- 입력 그래프 -------------
    plt.plot(pin4_x[:],'.',color='r')
    plt.plot(pin4_y[:],'.',color='g')

    plt.plot(pin7_x[:],'.',color='b')
    plt.plot(pin7_y[:],'.',color='y')
    '''


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
      


    #print(pin4_x)

    '''
    
    #-------원본 점 찍기--------

    plt.plot(pin4_x[:],'.',color='r')
    plt.plot(pin4_y[:],'.',color='g')

    plt.plot(pin7_x[:],'.',color='b')
    plt.plot(pin7_y[:],'.',color='y')
    plt.figure()
    '''
    ######################## 그래프 만들기(interpolate) ##############################


    npdx4 = pin4_x
    npdy4 = pin4_y
    npdx7 = pin7_x
    npdy7 = pin7_y


    splX4 = ip.UnivariateSpline(range(len(npdx4)),npdx4)
    splX4_x = np.linspace(0,range(len(npdx4)),10000)

    splY4 = ip.UnivariateSpline(range(len(npdy4)),npdy4)
    splY4_x = np.linspace(0,range(len(npdy4)),10000)

    splX7 = ip.UnivariateSpline(range(len(npdy7)),npdx7)
    splX7_x = np.linspace(0,range(len(npdx7)),10000)

    splY7 = ip.UnivariateSpline(range(len(npdy7)),npdy7)
    splY7_x = np.linspace(0,range(len(npdy7)),10000)



    '''
    ax = plt.gca()
    ax.xaxis.grid(True)
    ax.yaxis.grid(True)



    #----------보간 함수 띄우기----------
    
    plt.plot(splX4_x, splX4(splX4_x),'red')
    plt.plot(splY4_x, splY4(splY4_x),'pink')

    plt.plot(splX7_x,splX7(splX7_x),'blue')
    plt.plot(splY7_x,splY7(splY7_x),'skyblue')
    plt.figure()
    '''
    ######################### 구간 나누기 ###########################


    temp_First = splX4(1)
    Re_temp = temp_First * 0.01
    Address = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in range(len(pin4_x)):
        temp = splX4(i)

        if (abs(temp_First - temp) > Re_temp):
            Address = i
            break

    for i in range(Address, len(pin4_x)):
        if (splX4(Address) < splX4(i)):
            a = i
            break
        
    min_b = 999999 #top
    for i in range(Address, a):
        if(top_y[i] < min_b):
            b = i
            min_b = top_y[i]

    min_c = 999999 #back
    for i in range(Address, b):
        if(splX4(i) < min_c):
            c = i
            min_c = splX4(c)

    max_d = 0      #impact
    for i in range(b, len(pin4_y)):
        if(splY4(i) > max_d):
            d = i
            max_d = splY4(d)

    min_e = 999999 #finish
    for i in range(b, len(pin4_y)):
        if(splY4(i) < min_e):
            e = i
            min_e = splY4(e)

    '''

    ############## 구간을 나눈 plot ##############
    
    plt.plot(splX4_x, splX4(splX4_x), 'black')
    plt.plot(splY4_x, splY4(splY4_x), 'black')
    
    
    plt.axvline(x=24,lw=1,c='g')
    plt.axvline(x=b,lw=1,c='g')
    plt.axvline(x=c,lw=1,c='g')
    plt.axvline(x=d,lw=1,c='g')
    plt.axvline(x=e,lw=1,c='g')
    ##########################################
    plt.figure()
    '''

    print(Address)
    print(b)
    print(c)
    print(d)
    print(e)

    return Address,c,b,d,e

    #plt.show()











