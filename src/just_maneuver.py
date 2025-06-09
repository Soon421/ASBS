import time
import csv
from integrate_by_sd import integ, integral__by_SD
from imu_reader import open_serial, read_serial_line
from sl_valve import open_l, open_r, close_l, close_r
from watcher import func_watcher
from yaw_estimator import yaw_estimator
from linear_act import foward,stop,stopstop,right_turn,left_turn, backward
import threading

#######
#####
######
#####
##### 이 코드 그냥 무시하셈셈


# 아두이노연결 (open_serial 함수 이용 간단하게)
ser = open_serial(port="COM8", baudrate=115200)  #아두이노우노, IMU센서
ser_steer= open_serial(port="COM6", baudrate=115200)  #아두이노메가-전방
ser_rear= open_serial(port="COM7", baudrate=115200)  #아두이노메가-후방 mosfet모듈(솔레노이드밸브) 2개, 모터드라이버(리니어 액츄에이터) 1개 

#초기세팅(각 솔레노이드밸브 전부 닫아두기 + 리니어액츄에이터로 브레이크 미리 밟아두기 추가 예정)
imu_log = open_l("imu_log.csv", "w")
imu_log_list=[]
delta_vlist=[] 

def whole_maneuver():
    
    print('7초 뒤에 미셈셈')
    time.sleep(7)
    print('미셈')
    time.sleep(1.5)

    open_l(ser_rear)
    left_turn(ser_steer)
    time.sleep(0.8)
    stop(ser_steer)          

close_l(ser_rear)   #좌측후방
close_r(ser_rear)   #우측후방
foward(ser_rear)
yaw_handled = False

def noticer():
    print("!!!!!!!!!!!!!!!!")
    
threading.Timer(17, lambda:noticer).start()
threading.Timer(20, lambda: whole_maneuver()).start()

for yaw, timestamp, values in yaw_estimator(ser):
    z,watcher_1,j,watcher = func_watcher(values, watcher,j,z)
    
    i += 1
    csv_line = f"{timestamp}," + ",".join([str(v) for v in values]) + "\n"   
    imu_log.write(csv_line)

    if not yaw_handled and (yaw > 45 or yaw<-45):    #  이거 코드가 이상한데...? 한번 비교해보시길. 나는 바꾼다 보고 확인 바람람
        right_turn(ser_steer)  
        threading.Timer(1.2, lambda: stopstop(ser_steer)).start()
        open_r(ser_rear)
        threading.Timer(0.1, lambda: close_r(ser_steer)).start()
        backward(ser_rear)
        threading.Timer(0.1, lambda: foward(ser_rear)).start()
        threading.Timer(0.1, lambda: close_l(ser_steer)).start()
        threading.Timer(1.5,lambda:open_r(ser_rear)).start()
        yaw_handled= True
    