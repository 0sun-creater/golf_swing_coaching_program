'''
1. 파라미터에 기본값을 설정해놓으면, 함수 호출 시 값을 전달하지 않았을 경우,
   기본값이 매개변수에 저장된다
2. 기본값이 설정되지 않은 매개변수가 앞쪽에 와야한다
3. 일반 매개변수 먼저, 리스트형, 딕셔너리형
4. 같은 종류의 포인터 가변형 매개변수를 여러개 사용 불가
'''


import numpy as np
import math

'''
1. 3개 점을 기반으로 한 2개 선을 만들고, 각각의 기울기를 구한다
2. (기울기1-기울기2) / (1+기울기1*기울기2)를 구하고 x라 명명
3. x의 arctan 구하기
                            참고자료 https://jsideas.net/vector/
https://m.blog.naver.com/PostView.nhn?blogId=tobsysco&logNo=90189688655&proxyReferer=https:%2F%2Fwww.google.com%2F
https://darkpgmr.tistory.com/121
'''
########## 각도 구하기 ##########
def angle(P1_x,P1_y,P2_x,P2_y,P3_x,P3_y):
    #두 점을 벡터로 변환
    v1 = [P1_x-P2_x,P1_y-P2_y]
    v2 = [P3_x-P2_x,P3_y-P2_y]

    #벡터의 크기 구하기
    distA = math.sqrt(v1[0]**2 + v1[1]**2)
    distB = math.sqrt(v2[0]**2 + v2[1]**2)

    #내적
    ip = v1[0]*v2[0] + v1[1] * v2[1]
    ip2 = distA * distB
    cos =ip/ip2

    x = math.acos(cos)
    deg = math.degrees(x)

    return deg

########## 값 크기 비교 ##########
#앞에 값이 작으면 -1, 크면 1, 같으면 0
def size_compare(point1, point2):
    if point1 < point2:
        return -1
    elif point1 > point2:
        return 1
    else:
        return 0



########## 평균변화율 구하기 ##########
#순간변화율 = 미분한 값
#평균변화율의 값이 더 큰 쪽이 더 빠르게 변화하는 것
def avg_RateChange(s_frame,e_frame,fx):
    y = (fx(e_frame)-fx(s_frame))/(e_frame-s_frame)
    return y



######### 기울기 구하기 ##########
def get_slope(frame, key1_x,key1_y,key2_x, key2_y): #key 인자들에 key번호가 아니라 함수를 넣어야해
    slope= (key2_y(frame)-key1_y(frame))/(key2_x(frame)-key1_x(frame)) # 두 키포인트의 기울기

    #오차범위 추가해서 기울기가 0주변인 것들 찾는거 넣어야해
    return slope



   
########## 넓이 비교하기 ########
'''
    보통 넓이 구할때 x나 y 둘중 하나만 비교
    x나 y중 비교하고 싶은 것을 key에 넣으면 됨

    그냥 두개의 key의 거리를 구하고 싶으면 ex) similar_distance(frame=4, key1=2, key2=3)
    이렇게만 해도 됌
    https://python.bakyeono.net/chapter-3-5.html
    '''
def similar_distance4(frame, key1, key2, key3, key4): # 4개 키포인트 넓이 구하기
    distance1_2= abs(key2(frame)-key1(frame))
    distance3_4= abs(key4(frame)-key3(frame))
    if abs(distance1_2-distance3_4)<10: # 두 구간의 넓이가 같을때 1 반환 (오차율 조절해야해)
        return 1
    else: # 두 구간의 넓이가 다를 때 0 반환
        return 0

def similar_distance2(frame, key1, key2): # 2개 키포인트 넓이 구하기
    distance1_2= abs(key2(frame)-key1(frame))
    return distance1_2
    



########## 키포인트 비교  ##########
    '''
    결과값이 -(음수)이면 오른쪽으로 갔다.
    결과값이 +(양수)이면 왼쪽으로 갔다. 
    '''
def compare_frame(frame1, frame2, key):
    key_compare=key(frame1)-key(frame2) # key 변화정도
    return key_compare

    

##### 1차 미분 #### - 순간변화율
def maxima_minima(spl, xs):
        #미분하고 싶으면 splX.derivative()
        #                maxima_minima(splX, splX_x)
        #plt.plot(xs, spl(xs),'r')
    dy = spl(xs)
    tol = 0.05
    root_index = np.where((dy>-tol)&(dy<tol))

    root = xs[root_index]
    root = set(np.round(root, decimals=2).tolist())
    root = np.array(list(root))
    root.sort()
    #plt.plot(root,spl(root),'o')

    return root

##### 2차 미분 ####
    #극대, 극소점 판별
    #극대(^) =0 / 극소(U) =1
def distinction(spl, root):
    result = []
    for c in range(len(root)):        
        if spl(root)[c] < 0 :
            result.append(1)
        elif spl(root)[c] > 0 :
            result.append(0)
                
    return result

    
