import time
import csv
from integrate_by_sd import integ, integral__by_SD
from imu_reader import open_serial, read_serial_line
from sl_valve import open_l, open_r, close_l, close_r
from watcher import func_watcher
from yaw_estimator import yaw_estimator
from linear_act import foward,stop,stopstop,right_turn,left_turn, backward

#######
#####
######
#####
##### 이 코드 그냥 무시하셈셈


# 아두이노연결 (open_serial 함수 이용 간단하게)
ser = open_serial(port="COM8", baudrate=115200)  #아두이노우노, IMU센서
ser1= open_serial(port="COM6", baudrate=115200)  #아두이노메가-전방
ser2= open_serial(port="COM7", baudrate=115200)  #아두이노메가-후방 mosfet모듈(솔레노이드밸브) 2개, 모터드라이버(리니어 액츄에이터) 1개 

#초기세팅(각 솔레노이드밸브 전부 닫아두기 + 리니어액츄에이터로 브레이크 미리 밟아두기 추가 예정)
imu_log = open_l("imu_log.csv", "w")
imu_log_list=[]
delta_vlist=[] 

close_l(ser2)   #좌측후방
close_r(ser2)   #우측후방
foward(ser2)

print('7초 뒤에 미셈셈')
time.sleep(7)
print('미셈')
time.sleep(1.5)

open_l(ser2)
backward(ser1)
time.sleep(1)
stop(ser1)          



backward(ser2)
time.sleep(0.1)
stop(ser2)
close_l(ser2)
open_r(ser2)
foward(ser1)  
time.sleep(1)
stop(ser1)