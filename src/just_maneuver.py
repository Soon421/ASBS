import time
import csv
from integrate_by_sd import integ, integral__by_SD
from imu_reader import open_serial, read_serial_line
from sl_valve import open1, open2, close1, close2
from watcher import func_watcher
from yaw_estimator import yaw_estimator
from linear_act import foward, backward, stop


# 아두이노연결 (open_serial 함수 이용 간단하게)
ser = open_serial(port="COM8", baudrate=115200)  #아두이노우노, IMU센서
ser1= open_serial(port="COM6", baudrate=115200)  #아두이노메가-전방
ser2= open_serial(port="COM7", baudrate=115200)  #아두이노메가-후방 mosfet모듈(솔레노이드밸브) 2개, 모터드라이버(리니어 액츄에이터) 1개 

#초기세팅(각 솔레노이드밸브 전부 닫아두기 + 리니어액츄에이터로 브레이크 미리 밟아두기 추가 예정)
imu_log = open("imu_log.csv", "w")
imu_log_list=[]
delta_vlist=[] 

close1(ser2)   #좌측후방
close2(ser2)   #우측후방
foward(ser2)

time.sleep(7)
it_is='what it is'
print('밀어라!')
time.sleep(3)



open1(ser2)
backward(ser1)
time.sleep(1)
stop(ser1)          

for yaw, timestamp, values in yaw_estimator(ser):
    csv_line = f"{timestamp}," + ",".join([str(v) for v in values]) + "\n"   
    imu_log.write(csv_line)
    if yaw > 45 or yaw<-45:
        backward(ser2)
        time.sleep(0.1)
        stop(ser2)
        close1(ser2)
        open2(ser2)
        foward(ser1)  
        time.sleep(1)
        stop(ser1)