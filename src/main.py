#main.py, 현재 충격량적분부분까지 테스트 마침.
#모듈들로부터 import
import time
import csv
from integrate_by_sd import integ, integral__by_SD
from imu_reader import open_serial, read_serial_line
from sl_valve import open1, open2, open3, open4, close1, close2, close3, close4
from watcher import func_watcher
from yaw_estimator import yaw_estimator


# 아두이노연결 (open_serial 함수 이용 간단하게)
ser = open_serial(port="COM5", baudrate=9600)  #아두이노우노, IMU센서
ser1= open_serial(port="COM6", baudrate=9600)  #아두이노메가, mosfet모듈(솔레노이드밸브) 2개, 모터드라이버(리니어 액츄에이터) 1개 
ser2= open_serial(port="COM7", baudrate=9600)

#초기세팅(각 솔레노이드밸브 전부 열어두기 + 리니어액츄에이터로 브레이크 미리 밟아두기 추가 예정)
open1(ser1)   #좌측전방
open2(ser1)   #우측전방
open3(ser2)   #좌측후방
open4(ser2)   #우측후방


#main 코드 시작
#초기값설정
watcher = [0,0,0,0,0]                            
i=0
j=0   
z=0
integrate_log = []
integrate_time= []
integ_result=0


#main
try:
    #yiled이용해 yaw, timestamp, values 변수를 계속 받아옴(코드가 복잡해질때 변수관리에 더 용이)
    for yaw, timestamp, values in yaw_estimator(ser):    
        #충격량 적분과정
        z,watcher_1,j,watcher = func_watcher(values, watcher,j,z)
        integ_result=integral__by_SD(j,z,values,integrate_log,timestamp, integrate_time)
        i += 1

        print(integ_result)
        print(watcher)
        print(watcher_1)
        print("j={}".format(j)) 

        #충격 감지시 즉각 브레이크제어
        if watcher[0] - watcher_1[0]  >= 3:
            if values[1]>0:       #차가 충돌 후 좌측으로 이동
                close3(ser1)      #좌측후방 브레이크 잠금
            else:                 #차가 충동 후 우측으로 이동
                close4(ser1)      #우측후방 브레이크 잠금

        #case1: 속도 충분할 때
        if integ_result>=50:          
                            
            if yaw > 45 or yaw<-45:
                open(ser1)
        #case2: 속도 부족할 때
        elif integ_result>0 and integ_result<50:
            
            if yaw >45 or yaw<-45:
                open(ser1)
            
             

            
            
except KeyboardInterrupt:
    print("\n[INFO] 데이터 수신 종료")

finally:
    ser.close
    ser1.close  
 