import part_seperate
import JSON_class as key
import function as func
import numpy as np
import statistics

from marker_master_front import marker as marker_master_front
from marker_master_side import marker as marker_master_side
from marker import marker as marker
from matplotlib import pyplot as plt


#### 피드백 리스트
address_feedback=[]
backswing_feedback=[]
swing_feedback=[]
finish_feedback=[]
stands =[]
point =[]

'''
1. 어드레스 -> Address_feedback
2. 테이크어웨이 ~ 백스윙 -> BackSwing_feedback
3. 탑스윙(다운스윙) -> Swing_feedback
4. 임팩트 ~ 피니쉬 -> End_feedback
'''

def main(Impact_frame,id_text):
    address_feedback.clear()
    backswing_feedback.clear()
    swing_feedback.clear()
    finish_feedback.clear()
    stands.clear()
    point.clear()
    ############################################################################
    #address, take_away 구하기
    mov_x,mov_y = part_seperate.read_file(1)
    side_x, side_y = part_seperate.read_file(2)
    address, backswing, top,impact,finish = part_seperate.parts(mov_x,mov_y)

    #ball_x = 370
    #ball_y = 436
    ball_x = 630
    ball_y = 679
    
    address = 30

    #mov_x[frame][keypoint] 모든키포인트, 모든 프레임의 x좌표
    #mov_y[frame][keypoint] 모든키포인트, 모든 프레임의 y좌표
    #그 순간의 프레임

    key0 = key.graph_maker(0,mov_x,mov_y,side_x,side_y) #객체 생성
    key1 = key.graph_maker(1,mov_x,mov_y,side_x,side_y)
    key2 = key.graph_maker(2,mov_x,mov_y,side_x,side_y)
    key3 = key.graph_maker(3,mov_x,mov_y,side_x,side_y)
    key4 = key.graph_maker(4,mov_x,mov_y,side_x,side_y)
    key5 = key.graph_maker(5,mov_x,mov_y,side_x,side_y)
    key6 = key.graph_maker(6,mov_x,mov_y,side_x,side_y)
    key7 = key.graph_maker(7,mov_x,mov_y,side_x,side_y)
    key8 = key.graph_maker(8,mov_x,mov_y,side_x,side_y)
    key9 = key.graph_maker(9,mov_x,mov_y,side_x,side_y)
    key10 = key.graph_maker(10,mov_x,mov_y,side_x,side_y)
    key11 = key.graph_maker(11,mov_x,mov_y,side_x,side_y)
    key12 = key.graph_maker(12,mov_x,mov_y,side_x,side_y)
    key13 = key.graph_maker(13,mov_x,mov_y,side_x,side_y)
    key14 = key.graph_maker(14,mov_x,mov_y,side_x,side_y)
    key15 = key.graph_maker(15,mov_x,mov_y,side_x,side_y)
    key16 = key.graph_maker(16,mov_x,mov_y,side_x,side_y)
    key17 = key.graph_maker(17,mov_x,mov_y,side_x,side_y)
    key18 = key.graph_maker(18,mov_x,mov_y,side_x,side_y)
    key19 = key.graph_maker(19,mov_x,mov_y,side_x,side_y)
    key20 = key.graph_maker(20,mov_x,mov_y,side_x,side_y)
    key21 = key.graph_maker(21,mov_x,mov_y,side_x,side_y)
    key22 = key.graph_maker(22,mov_x,mov_y,side_x,side_y)
    key23 = key.graph_maker(23,mov_x,mov_y,side_x,side_y)
    key24 = key.graph_maker(24,mov_x,mov_y,side_x,side_y)


    ########################### Take Away 구간 나누기 #########################
    takeaway=0
    for i in range(address, top):
        if(key11.splX(i)>key4.splX(i)):
            takeaway=i
            break
    #print(impact)
    impact = Impact_frame
    #print(impact)
    point.append(address)
    point.append(takeaway)
    point.append(backswing)
    point.append(top)
    point.append(impact)
    point.append(finish)
    '''
    #print(point)
    plt.axvline(x=address,lw=1,c='r')
    plt.axvline(x=top,lw=1,c='orange')
    plt.axvline(x=takeaway,lw=1,c='yellow')
    plt.axvline(x=impact,lw=1,c='green')
    plt.axvline(x=finish,lw=1,c='blue')
    '''



    ########################### 영선이 함수 #########################
    def median_angle(angle,frame):
        compare=[]
        for i in range(5):
            compare.append(angle[frame-(i-2)])
            
        return statistics.median(compare)
    ##################################################################

    ########################### Mark 할 배열 만들기 ###########################
    '''
    행 -> 구간 (0: 어드레스 / 1: 어드레스~테이크어웨이 / 2: 테이크어웨이
                3: 백스윙 / 4: 탑스윙 / 5: 탑스윙~임팩트 / 6: 임팩트 / 7: 임팩트~피니쉬 / 8: 피니쉬)
    열 -> 부위 (0: 머리 / 1: 어깨 / 2: 왼팔 / 3: 오른팔 / 4: 왼손목 / 5: 오른손목 / 6: 볼 / 7: 척추
                8: 골반 / 9: 왼무릎 / 10: 오른무릎 / 11: 왼발 / 12: 오른발)

    구간이 아닌 한 frame을 볼때는 앞뒤로 여유 프레임을 두고 마크하는게 좋을듯
    '''
    mark = [[0 for col in range(13)] for row in range(9)]
    side_mark = [[0 for col in range(13)] for row in range(9)]



    ##############################     HEAD    ##############################
    '''
    # [어드레스]  공과 코의 정면 x축 범위는 공 기준으로 양쪽 귀의 25% 범위에 있어야 한다
    ear_rate = (abs(key18.splX(address) - key17.splX(address))) * 0.25
    ball_flag =0
    if(key0.splX(address) > ball_x - ear_rate and key0.splX(address) < ball_x + ear_rate):
        pass
    else:
        #print("[어드레스] 공은 코와 일자가 되어야합니다.")
        #mark[0][0]=1
        ball_flag =1

    '''
    # [전구간] 머리 y위치는 전구간에서 움직이지 않아야한다. 머리의 각도는 175~180 사이에 있어야한다.

    i=address
    b_flag=0
    s_flag=0
    i_flag=0
    while(True):
        head = key0.splY(address) - key0.splY(i)
        if ( head <= 20 ) and ( head >= -20 ):
            # 전 구간에서 머리가 움직이지 않은 상태
            pass
        else:
            if i <top:
                if b_flag ==0:
                    backswing_feedback.append("[백스윙] 머리의 높이는 전구간 일정해야 몸의 균형이 무너지지 않습니다.")
                    mark[3][0]=1
                    if head < 0:
                        backswing_feedback.append("    머리의 높이가 낮아졌습니다.")
                    else :
                        backswing_feedback.append("    머리의 높이가 높아졌습니다.")
                b_flag =1
                
            elif i <impact-15:
                if s_flag==0:
                    swing_feedback.append("[스윙] 머리의 높이는 전구간 일정해야 몸의 균형이 무너지지 않습니다.")
                    mark[5][0]=1
                    if head < 0:
                        swing_feedback.append("    머리의 높이가 낮아졌습니다.")
                    else :
                        swing_feedback.append("    머리의 높이가 높아졌습니다.")
                s_flag =1
                
            elif i <impact:
                if i_flag==0:
                    finish_feedback.append("[임팩트] 머리의 높이는 전구간 일정해야 몸의 균형이 무너지지 않습니다.")
                    mark[6][0]=1
                    if head < 0:
                        finish_feedback.append("    머리의 높이가 낮아졌습니다.")
                    else :
                        finish_feedback.append("    머리의 높이가 높아졌습니다.")
                i_flag =1

        i = i + 1
        if i > impact:
            break
    '''   
    # [전구간] 시선은 공에 맞추기  key 17 18
    sight=[]

    for i in range(top+3):
        sight.append(func.angle(key17.splX(i),key17.splY(i),key18.splX(i),key18.splY(i),key18.splX(i)+100,key18.splY(i)))

    if median_angle(sight,address) < 174:
        mark[0][0]=1
        if median_angle(sight,address) > 160:
            address_feedback.append("[어드레스] 고개가 비스듬합니다.")
        else:
            address_feedback.append("[어드레스] 공을 바라보아야 합니다.")
            
    if median_angle(sight,takeaway) < 165:
        mark[1][0]=1
        backswing_feedback.append("[테이크어웨이] 공을 바라보아야 합니다")
        
    if median_angle(sight,backswing) >= 179 or median_angle(sight,backswing) < 160:
        mark[3][0]=1
        backswing_feedback.append("[백스윙] 공을 바라보아야 합니다")
        
    if median_angle(sight,top) >= 176 or median_angle(sight,top) < 160:
        mark[4][0]=1
        swing_feedback.append("[탑스윙] 공을 바라보아야 합니다")


    # [탑스윙 - 임팩트] 머리는 공의 위치보다 뒤에 와있다. (정면 key 0번은 공의 x좌표보다 작아야한다.)
    if(key0.splX(impact) > ball_x):
        mark[5][0]=1
        mark[5][6]=1
        swing_feedback.append("[스윙] 머리는 공 오른쪽에 와야합니다.")
    '''
    ##############################     SHOLDER    ##############################

    # [어드레스] 어깨와  스탠스의 정면 x축의 길이의 비율은 0.9~1.5의 비율을 갖고 있어야 한다.
    sholder=func.similar_distance2(address,key2.splX,key5.splX)
    foot=func.similar_distance2(address,key11.splX,key14.splX)

    rate=foot/sholder
    if (rate > 1.5 or rate < 0.95):
        mark[0][1]=1
        mark[0][6]=1
        address_feedback.append('[어드레스] 발은 어깨넓이 정도여야 합니다.')



    '''
    # [전구간] 어깨의 각도 확인, [어드레스] 오른쪽 어깨가 더 내려와 있어야 한다.
    front_s_angle=[]
    side_s_angle=[]



    for i in range(finish+3):
        front_s_angle.append(func.angle(key1.splX(i),key1.splY(i),key5.splX(i),key5.splY(i),key5.splX(i)+100,key5.splY(i)))
        side_s_angle.append(func.angle(key1.splX_s(i),key1.splY_s(i),key5.splX_s(i),key5.splY_s(i),key5.splX_s(i)+100,key5.splY_s(i)))



    solder_flag=0

    ##y축 비교해서 어디가 더 내려갔는지 추가
    y_com = func.size_compare(key2.splY(address), key5.splY(address))

    if y_com == 1:
        solder_flag=1
    elif y_com == -1:
        solder_flag=2
        mark[0][1]=1
        address_feedback.append("[어드레스] 왼쪽 어깨보다 오른쪽 어깨가 더 내려가야합니다.")
        

    if median_angle(front_s_angle, address) > 177 and not (solder_flag ==2):
        address_feedback.append("[어드레스] 어깨가 평행합니다. 오른쪽 어깨는 왼쪽 어깨보다 내려가야합니다")
        mark[0][1]=1
    elif median_angle(front_s_angle, address) < 170 and solder_flag ==1:
        address_feedback.append("[어드레스] 오른쪽 어깨가 너무 많이 내려갔습니다")
        mark[0][1]=1
        
    if median_angle(front_s_angle,takeaway) < 176:
        backswing_feedback.append("[테이크어웨이] 어깨가 평행에 가까워야합니다.")
        mark[2][1]=1

    if median_angle(side_s_angle,backswing) >= 156:
        backswing_feedback.append("[백스윙] 어깨가 많이 돌아갔습니다")
        mark[3][1]=1
    elif median_angle(side_s_angle,backswing) < 145:
        backswing_feedback.append("[백스윙] 어깨가 덜 돌아갔습니다")
        mark[3][1]=1
        
    if median_angle(side_s_angle,top) >= 152:
        swing_feedback.append("[탑스윙] 어깨가 많이 돌아갔습니다")
        mark[4][1]=1
    elif median_angle(side_s_angle,top) < 141:
        swing_feedback.append("[탑스윙] 어깨가 덜 돌아갔습니다")
        mark[4][1]=1
        
    if median_angle(front_s_angle,impact) >= 170:
        finish_feedback.append("[임팩트] 어깨가 많이 돌아갔습니다")
        mark[6][1]=1
    elif median_angle(front_s_angle,impact) < 159:
        finish_feedback.append("[임팩트] 어깨가 덜 돌아갔습니다")
        mark[6][1]=1

    if median_angle(side_s_angle,finish) >= 40:
        finish_feedback.append("[피니쉬] 어깨가 많이 돌아갔습니다")
        mark[8][1]=1
    elif median_angle(side_s_angle,finish) < 20:
        finish_feedback.append("[피니쉬] 어깨가 덜 돌아갔습니다")
        mark[8][1]=1


    del front_s_angle
    del side_s_angle



    #오른쪽 어깨와 왼쪽 어깨 x축 비교

    flag = 0
    cross_sholder = 0
    for i in range(top, finish):
        if (key2.splX_s(i) > key5.splX_s(i) and flag == 0):
            flag = 1
            cross_sholder = i

    if ((impact - cross_sholder) > 1):
        finish_feedback.append("[임팩트] 몸이 빨리 돌아갔습니다.")
        side_mark[6][1]=1
        
    elif ((impact - cross_sholder) < -2):
        finish_feedback.append("[임팩트] 몸이 늦게 돌아갔습니다.")
        side_mark[6][1]=1

    '''





    ##############################     ARM    ##############################

    # [어드레스] 왼쪽 겨드랑이 죄어주기
    address_left_under_arm = func.similar_distance2(address, key5.splX, key6.splX)
    if (address_left_under_arm > 0):
        address_feedback.append('[어드레스] 왼쪽 겨드랑이를 죄어주어야 합니다.')
        mark[0][2]=1


    # [어드레스 - 테이크어웨이] 팔 삼각형 유지

    left_a = (func.angle(key5.splX(address),key5.splY(address),key6.splX(address),key6.splY(address),key7.splX(address),key7.splY(address)))
    right_a = (func.angle(key2.splX(address),key2.splY(address),key3.splX(address),key3.splY(address),key4.splX(address),key4.splY(address)))

    left_t = (func.angle(key5.splX(takeaway),key5.splY(takeaway),key6.splX(takeaway),key6.splY(takeaway),key7.splX(takeaway),key7.splY(takeaway)))
    right_t = (func.angle(key2.splX(takeaway),key2.splY(takeaway),key3.splX(takeaway),key3.splY(takeaway),key4.splX(takeaway),key4.splY(takeaway)))

    if left_a < 170:
        address_feedback.append("[어드레스] 왼팔은 펴야합니다.")
        mark[0][2]=1
    if right_a < 165:
        address_feedback.append("[어드레스] 양팔과 어깨로 삼각형 모양이 만들어져야 합니다.")
        mark[0][3]=1
        
    if left_t < 170:
        backswing_feedback.append("[테이크어웨이] 왼팔은 펴야합니다.")
        mark[0][2]=1
        mark[1][2]=1
        mark[2][2]=1
    if right_t < 165:
        backswing_feedback.append("[테이크어웨이] 양팔과 어깨로 삼각형 모양이 만들어져야 합니다.")
        mark[0][3]=1
        mark[1][3]=1
        mark[2][3]=1
    '''
    if ball_flag ==1:        
        # [어드래스] 손목, 볼 위치확인  => 이거 이 피드백 맞음?
        if((key7.splX(address) > ball_x) and (key4.splX(address) < ball_x)):
            pass
        else:
            address_feedback.append("[어드레스] 볼은 중앙에 있어야 합니다.")
            mark[0][4]=1
            mark[0][5]=1
            mark[0][6]=1

    '''
    # [탑] 측면에서 key6번이 key1번과 5번의 x좌표 사이에 있어야 한다.  => 이거 피드백 없음
    if(key1.splX_s(top) < key6.splX_s(top) and key5.splX_s(top) > key6.splX_s(top)):
        pass
    else:
        if(key5.splX_s(top) < key6.splX_s(top)):
            swing_feedback.append("[탑스윙] 왼팔이 많이 굽혀졌습니다.")
            side_mark[4][2]=1

        else:
            swing_feedback.append("[탑스윙] 몸이 과하게 돌아갔습니다.")
            side_mark[4][1]=1


        


    # [백스윙- 탑] (8번의 골반과 어깨의 돌아간 각도의 범위에 포함되어있는 상태에서)
    #          테이크어웨이 이후부터 탑스윙 까지 왼손이 공을 한번이상 가리키고 있어야 한다.
    #         (정면 key6, 7, 공 이 일직선상에 있던 적이 있어야 한다) - 그게 아니라면 팔의 높이가 부족한것
    arm_flag =0
    for i in range(takeaway, top+1):
        line_L = func.angle(key7.splX(i),key7.splY(i),key6.splX(i),key6.splY(i),ball_x,ball_y)
        line_R = func.angle(key4.splX(i),key4.splY(i),key3.splX(i),key3.splY(i),ball_x,ball_y)

        if line_L > 177 or line_R > 177:
            arm_flag = 1
            break

    if arm_flag ==0:
        swing_feedback.append("[탑스윙] 어깨의 회전을 충분히 주어야합니다.")
        mark[3][1]=1


    # [탑] 오른쪽 팔꿈치가 땅바닥과 거의 수평이 된다. (측면 key 2 3번 y의 값)
    key2_e = []
    key3_e = []
    for i in range(top-7, top+3):
        key2_e.append(float(key2.splY_s(i)))
        key3_e.append(float(key3.splY_s(i)))
    elbow = abs(np.asarray(key2_e) - np.asarray(key3_e))
    min_elbow = min(elbow)

    if min_elbow > 5:
        swing_feedback.append("[탑스윙] 오른쪽 팔뚝이 지면과 평행해질 수 있도록 몸의 충분한 회전이 필요합니다.")
        side_mark[4][3]=1

    del key2_e
    del key3_e


    # [임팩트] 볼을 타격하는 순간 양팔을 펴야된다. (key2 3 4 key5 6 7)
    # (key2 3 4 key5 6 7)

    right_arm_impact=[]
    left_arm_impact=[]
    for i in range(impact-1,impact+2): #오차 3프레임
        right_arm_impact.append(func.angle(key2.splX(i),key2.splY(i),key3.splX(i),key3.splY(i),key4.splX(i),key4.splY(i)))
        left_arm_impact.append(func.angle(key5.splX(i),key5.splY(i),key6.splX(i),key6.splY(i),key7.splX(i),key7.splY(i)))

    if max(right_arm_impact) < 170:
        finish_feedback.append("[임팩트] 오른팔을 곧게 뻗어야합니다.")
        mark[6][3]=1
    if max(left_arm_impact)  < 170:
        finish_feedback.append("[임팩트] 왼팔을 곧게 뻗어야합니다.")
        mark[6][2]=1



    # [다운스윙] 왼팔은 곧게 뻗쳐있다. (key 5 6 7)
    #잘 모르겠음 .. 수치상 곧게 뻗쳐있지 않음 코드안짬
    left_arm_down=[]
    for i in range(top,impact+2): #오차 3프레임 (정확한 impact 순간이라 확신이 없어서)
        left_arm_down.append(func.angle(key5.splX(i),key5.splY(i),key6.splX(i),key6.splY(i),key7.splX(i),key7.splY(i)))




    # [다운스윙] 오른쪽 팔꿈치를 옆구리에 붙인다. (key 2 어깨, 3 팔꿈치)
    #정면 key 3번은 2번보다 커야한다
    #작은경우 몸을 느리게 돌렸거나, 팔을 벌려서 쳤거나
    ##판단 불가능.. 팔을 뻗고 있음 -> 옆에 붙이고 있지 않음
                 #다운스윙에서 takeaway 지점을 지난 이후 정도로 볼 수 있음 << 이것또한 눈대중이며, 팔꿈치가 옆구리에 붙었다고 판단하기 힘듬

    a=[]
    b=[]
    for i in range(top,impact+2):
        a.append(float(key2.splX(i)))
        b.append(float(key3.splX(i)))

        
    #측면 key4 7번의 x좌표 값은 어그레스 key0의 x좌표 보다 작은 상태를 유지해야 한다.

    backswing_flag=0
    swing_flag=0
    finish_flag=0
    for i in range(address, finish):

        if(key4.splX_s(i) > key0.splX_s(i) or key7.splX_s(i) > key0.splX_s(i) ):
            if i < top and backswing_flag==0:
                backswing_feedback.append("in으로 치기 위해서는 손목이 코보다 앞으로 나오면 안됩니다.")
                backswing_flag=1
                side_mark[0][1]=1
                side_mark[1][1]=1
                side_mark[2][1]=1
                side_mark[3][1]=1
                side_mark[4][1]=1
            elif i < impact and swing_flag==0:
                swing_feedback.append("in으로 치기 위해서는 손목이 코보다 앞으로 나오면 안됩니다.")
                swing_flag=1
                side_mark[5][1]=1
                side_mark[6][1]=1
            elif i < finish and finish_flag==0:
                finish_feedback.append("in으로 치기 위해서는 손목이 코보다 앞으로 나오면 안됩니다.")
                finish_flag=1
                side_mark[7][1]=1
                side_mark[8][1]=1



    ##############################     spine    ##############################

    #[어드래스] 척추 각도
    spine=[]
    for i in range(len(point)):
        spine.append(func.angle(key1.splX_s(point[i]),key1.splY_s(point[i]),key8.splX_s(point[i]),key8.splY_s(point[i]),(key8.splX_s(point[i])+50),key8.splY_s(point[i])))

    if(spine[0] > 55 and spine[0] < 64):
        pass
    if (spine[0] < 55):
        address_feedback.append("[어드레스] 허리를 더 구부려야합니다.")
        side_mark[0][7]=1
    if (spine[0] > 64):
        address_feedback.append("[어드레스] 허리를 더 펴야합니다.")
        side_mark[0][7]=1
        


    #[어드레스 - 탑] 척추 각도
    if((abs(spine[0] - spine[3])) > 7 ):
        backswing_feedback.append("[어드레스~탑] 척추각을 top스윙 지점까지 유지해야 합니다")
        side_mark[1][7]=1
        side_mark[2][7]=1
        side_mark[3][7]=1
        side_mark[4][7]=1
     



    ##############################     pelvis    ##############################
    '''
    # [전구간] 골반의 각도
    front_g_angle=[]
    side_g_angle=[]

    for i in range(finish+3):
        
        front_g_angle.append(func.angle(key8.splX(i),key8.splY(i),key12.splX(i),key12.splY(i),key12.splX(i)+100,key12.splY(i)))
        side_g_angle.append(func.angle(key8.splX_s(i),key8.splY_s(i),key12.splX_s(i),key12.splY_s(i),key12.splX_s(i)+100,key12.splY_s(i)))


    if median_angle(front_g_angle, address) < 177:
        address_feedback.append("[어드레스] 골반이 바닥과 평행해야합니다.")
        mark[0][8]=1
        
    if median_angle(front_g_angle,takeaway) < 177 :
        backswing_feedback.append("[테이크어웨이] 골반이 바닥과 평행해야합니다.")
        mark[2][8]=1

    if median_angle(side_g_angle,backswing) > 173 :
        backswing_feedback.append("[백스윙] 골반이 많이 돌아갔습니다")
        side_mark[3][8]=1
    elif median_angle(side_g_angle,backswing) <160:
        backswing_feedback.append("[백스윙] 골반이 덜 돌아갔습니다")
        side_mark[3][8]=1
       
    if median_angle(side_g_angle,top) >= 172:
        swing_feedback.append("[탑스윙] 골반이 많이 돌아갔습니다")
        side_mark[4][8]=1
    elif median_angle(side_g_angle,top) < 165:
        swing_feedback.append("[탑스윙] 골반이 덜 돌아갔습니다")
        side_mark[4][8]=1
        
    if median_angle(front_g_angle,impact) >=175 :
        finish_feedback.append("[임팩트] 골반이 많이 돌아갔습니다")
        mark[6][8]=1
    elif median_angle(front_g_angle,impact) < 167 :
        finish_feedback.append("[임팩트] 골반이 덜 돌아갔습니다")
        mark[6][8]=1

    if median_angle(side_g_angle,finish) > 15:
        finish_feedback.append("[피니쉬] 골반이 많이 돌아갔습니다")
        side_mark[8][8]=1
    elif median_angle(side_g_angle,finish) < 5 :
        finish_feedback.append("[피니쉬] 골반이 덜 돌아갔습니다")
        side_mark[8][8]=1


    del front_g_angle
    del side_g_angle

    '''



    ##############################     knee    ##############################

    # [어드레스] = 측면에서 왼쪽 160~170도, 오른쪽 150~165도
    side_address_left_knee_angle=func.angle(key12.splX_s(address),key12.splY_s(address),key13.splX_s(address),key13.splY_s(address),key14.splX_s(address),key14.splY_s(address))
    side_address_right_knee_angle=func.angle(key9.splX_s(address),key9.splY_s(address),key10.splX_s(address),key10.splY_s(address),key11.splX_s(address),key11.splY_s(address))

    if(side_address_left_knee_angle < 155):
        address_feedback.append('[어드레스] 왼쪽 무릎 각도가 기준보다 더 굽혀졌습니다.')
        side_mark[0][9]=1
    if(side_address_left_knee_angle > 170):
        address_feedback.append('[어드레스] 왼쪽 무릎 각도가 기준보다 덜 굽혀졌습니다.')
        side_mark[0][9]=1
    if(side_address_right_knee_angle < 150):
        address_feedback.append('[어드레스] 오른쪽 무릎 각도가 기준보다 더 굽혀졌습니다.')
        side_mark[0][10]=1
    if(side_address_right_knee_angle > 165):
        address_feedback.append('[어드레스] 오른쪽 무릎 각도가 기준보다 덜 굽혀졌습니다.')
        side_mark[0][10]=1



    # [어드레스 - 테이크어웨이] 측면 무릎각은 각도는 10도가 변하면 안된다.
    side_takeaway_left_knee_angle=func.angle(key12.splX_s(takeaway),key12.splY_s(takeaway),key13.splX_s(takeaway),key13.splY_s(takeaway),key14.splX_s(takeaway),key14.splY_s(takeaway))
    side_takeaway_right_knee_angle=func.angle(key9.splX_s(takeaway),key9.splY_s(takeaway),key10.splX_s(takeaway),key10.splY_s(takeaway),key11.splX_s(takeaway),key11.splY_s(takeaway))


    left_knee_angle_compare=side_address_left_knee_angle-side_takeaway_left_knee_angle
    right_knee_angle_compare=side_address_right_knee_angle-side_takeaway_right_knee_angle
    if(abs(left_knee_angle_compare) > 10 or abs(right_knee_angle_compare) > 10):
        backswing_feedback.append('[어드레스 ~ 테이크어웨이] 무릎의 각도는 유지 되어야합니다.')
        side_mark[1][9]=1
        side_mark[1][10]=1


    # [어드레스 - 테이크어웨이] 정면 무릎 모양 확인 (10% 오차가 존재한다)
    error= foot * 10/100

    compare_left_knee_x=func.compare_frame(address,takeaway,key13.splX)
    compare_left_knee_y=func.compare_frame(address,takeaway,key13.splY)
    compare_right_knee_x=func.compare_frame(address,takeaway,key10.splX)
    compare_right_knee_y=func.compare_frame(address,takeaway,key10.splY)

    if (abs(compare_left_knee_x) > error or abs(compare_right_knee_x) > error):
        backswing_feedback.append('[어드레스 ~ 테이크어웨이] 무릎은 최대한 움직이면 안됩니다.')
        mark[1][9]=1
        mark[1][10]=1


    # [테이크어웨이 - 탑]정면 왼쪽 무릎 안쪽으로 최소 4% 이상은 움직여야 함
    minimum = (key13.splX(address)-key10.splX(address)) * 4/100

    go_left_knee_x=func.compare_frame(takeaway,top,key13.splX)

    if(go_left_knee_x < minimum):
        backswing_feedback.append('[테이크어웨이 ~ 백스윙] 왼쪽 무릎은 안쪽으로 가야합니다.')
        mark[3][9]=1


    # 오른발의 안쪽에 힘을 주고 있으면 좋다. key10번의 x값 변화 비율  [오차율 확인~!]
     
    for i in range(3):
        if (key10.splX(point[0]) + 5 < key10.splX(point[i+1])):
            backswing_feedback.append("[어드레스 ~ 탑스윙]오른무릎이 안쪽으로 돌지 않도록 해야합니다.")
            mark[0][10]=1
            mark[1][10]=1
            mark[2][10]=1
            mark[3][10]=1
            mark[4][10]=1
            
        elif (key10.splX(point[0]) -15 > key10.splX(point[i+1])):
            backswing_feedback.append("[어드레스 ~ 탑스윙] 오른발 안쪽에 힘을 주어 균형을 유지해야합니다.")
            mark[0][10]=1
            mark[1][10]=1
            mark[2][10]=1
            mark[3][10]=1
            mark[4][10]=1


    # [탑스윙 - 임팩트] 임팩트 순간 두 무릎이 어드레스 때의 무릎 좌표를 지나야 한다.
    right_knee_check = func.compare_frame(impact, address, key10.splX)
    left_knee_check = func.compare_frame(impact, address, key13.splX)


    if(right_knee_check <= 0 and left_knee_check <= 0):
        swing_feedback.append("[스윙] 두 무릎이 좀 더 빠르게 목표를 향해 움직여야합니다.")
        mark[5][9]=1
        mark[5][10]=1
    elif(right_knee_check <= 0):
        swing_feedback.append("[스윙] 오른 무릎이 좀 더 빠르게 목표를 향해 움직여야합니다.")
        mark[5][10]=1
    elif(left_knee_check <= 0):
        swing_feedback.append("[스윙] 왼 무릎이 좀 더 빠르게 목표를 향해 움직여야합니다.")
        mark[5][9]=1


    # [탑스윙 - 임팩트] 무릎은 탑스윙부터 임팩트까지 부드럽게 유지되어있어야 한다.

    left_knee_d=key13.splX.derivative()
    right_knee_d=key10.splX.derivative()

    left_knee_root=func.maxima_minima(left_knee_d,key13.splX_x)
    right_knee_root=func.maxima_minima(right_knee_d,key10.splX_x)

    left_knee_range=[]
    right_knee_range=[]

    for i in range(0, len(left_knee_root)):
        if (left_knee_root[i] > top + 3 and left_knee_root[i] < impact - 5):
            left_knee_range.append(left_knee_root[i])
                   
    for i in range(0, len(right_knee_root)):
        if (right_knee_root[i] > top + 3 and right_knee_root[i] < impact - 5):
            right_knee_range.append(right_knee_root[i])

    if (len(left_knee_range) != 0 or len(right_knee_range) != 0):
        swing_feedback.append("[스윙] 무릎은 부드럽게 움직여야 합니다.")
        mark[5][9]=1
        mark[5][10]=1



    # [탑스윙 - 임팩트] 오른쪽 무릎이 아래로 눌린다. (어드레스 때 무릎 거리의 25%는 움직여야돼)
    right_minimum=(key13.splX(address)-key10.splX(address)) * 25/100 * -1
    go_right_knee_x=func.compare_frame(top,impact,key10.splX)

    if(go_right_knee_x > right_minimum):
        swing_feedback.append('[스윙] 오른쪽 무릎은 안쪽으로 움직여야 합니다.')
        mark[5][10]=1

    '''
    # [임팩트] 왼다리는 뻗어 있어야 한다. (정면 key12 13 14 각도 실험해 봐야함)
    left_knee_angle=func.angle(key12.splX(impact),key12.splY(impact),key13.splX(impact), key13.splY(impact),key14.splX(impact),key14.splY(impact))
    print(left_knee_angle)

    l=[]
    for i in range(finish):
        l.append((key12.splX(i),key12.splY(i),key13.splX(i), key13.splY(i),key14.splX(i),key14.splY(i)))

    '''

    ##############################     foot    ##############################

    # [어드래스] 스탠스 확인

    i = address
    right_F = (180 - func.angle(key24.splX(i),key24.splY(i),key22.splX(i),key22.splY(i),(key22.splX(i)-50),key22.splY(i)) )
    left_F = (180 - func.angle(key21.splX(i),key21.splY(i),key19.splX(i),key19.splY(i),(key19.splX(i)+50),key19.splY(i)))

    ## 직접 실험해서 범위를 수정해야 함 ~!
    if (left_F > 35 and left_F < 75 and right_F > 75 and right_F < 105):
        stands.append("오픈 스탠스 입니다")

    elif (left_F >= 75 and left_F < 105 and right_F > 75 and right_F < 105):
        stands.append("스퀘어 스탠스 입니다")

    else:
        stands.append("클로즈드 스탠스 입니다")

      
    #오른발의 발뒤꿈치가 측면에서 약간 들린다
    #feedback : 오른발의 엄지발가락에 힘을 주어 약간 들리게 한 후 임펙트 하세요.
    #print(key24.splY(top) - key24.splY(impact))
    if((key24.splY(top) - key24.splY(impact)) > 5):
        pass
    else:
        swing_feedback.append("[스윙] 오른발의 엄지발가락에 힘을 주어 약간 들리게 한 후 임펙트 하세요.")
        mark[5][12]=1



    '''
    영상에서 오른발을 제데로 검출하는 영상이 적어 실제로 테스트를 해 봐야 함!
    '''

        
    # [테이크어웨이 - 탑스윙] 왼쪽 발뒤꿈치 올라감    (보기만해도 좋아지는 골프영상)
    # [탑스윙 - 임펙트] 왼쪽 발뒤꿈치 제자리로 내려감
    i = top
    toe_r = func.angle(key20.splX(i),key20.splY(i),key19.splX(i),key19.splY(i),(key19.splX(i)+50),key19.splY(i))
    if( toe_r > 20 and toe_r < 45):
        pass
    else:
        backswing_feedback.append("[백스윙] 왼발은 살짝 올라가야합니다.")
        mark[2][11]=1
        mark[3][11]=1
        mark[4][11]=1
        
    '''
    plt.plot(key14.splY_x, key14.splY(key14.splY_x), 'r')
    plt.plot(key19.splY_x, key19.splY(key19.splY_x), 'b')

    plt.plot(key20.splY_x, key20.splY(key20.splY_x), 'pink')
    plt.plot(key21.splY_x, key21.splY(key21.splY_x), 'skyblue')


    test1 = []

    for i in range(145):
        test1.append(func.angle(key20.splX(i),key20.splY(i),key19.splX(i),key19.splY(i),(key19.splX(i)+50),key19.splY(i)))


    plt.plot(test1)
    '''

    '''
    보기만 해도 좋아지는 골프스윙을 테스트한 결과
    오른발의 너무 미세하게 움직여서 올리고 돌아오고 판단이 어렵다.
    그래서 각도로 접근하였음
    하지만 각도는 탑 스윙 지점에만 특징을 뽑아낼 수 있다 그래서 탑 지점에서 올렸는지만 판단만 가능하게 만들었음
    다른 지점에서는 key포인트 값이 너무 붙어있어서 각도로 접근하기에 큰 위험이 따른다.
    실제로  촬영 했을때  발의 좌표값이 잘 나온다면 적용은 할 수있을 것 같지만 현재 영상으로는 판단 불가
    '''
    stands.append(" ")
    address_feedback.append(" ")
    backswing_feedback.append(" ")
    swing_feedback.append(" ")
    finish_feedback.append(" ")


    marker(point, mov_x, mov_y, side_x, side_y, mark, side_mark)
    marker_master_front(point, mov_x, mov_y, side_x, side_y,id_text)
    marker_master_side(point, mov_x, mov_y, side_x, side_y)

