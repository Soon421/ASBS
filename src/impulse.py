#impulse.py 이 모듈은 정확한 충격량 구하는것만을 목표로함.
#모듈들로부터 import
import time
import csv
from integrate_by_sd import integ, integral__by_SD
from imu_reader import open_serial, read_serial_line
from sl_valve import open1, open2,close1, close2
from watcher import func_watcher
from yaw_estimator import yaw_estimator


# 아두이노연결 (open_serial 함수 이용 간단하게)
ser = open_serial(port="COM8", baudrate=115200)  #아두이노우노, IMU센서



#main 코드 시작
#초기값설정
watcher = [0,0,0,0,0]                            
i=0
j=0   
z=0
integrate_log = []
integrate_time= []
integ_result=0
imu_log = open("imu_log.csv", "w")
imu_log_list=[]
delta_vlist=[]        #적분값들 모아두는 리스트


#main
try:
    #yiled이용해 yaw, timestamp, values 변수를 계속 받아옴(코드가 복잡해질때 변수관리에 더 용이)
    for yaw, timestamp, values in yaw_estimator(ser):    
        #충격량 적분과정
        z,watcher_1,j,watcher = func_watcher(values, watcher,j,z)
        integ_result,z=integral__by_SD(j,z,values,integrate_log,timestamp, integrate_time, delta_vlist)
        i += 1
        csv_line = f"{timestamp}," + ",".join([str(v) for v in values]) + "\n"   
        imu_log.write(csv_line)

        print(integ_result)
        print(watcher_1)
        print(watcher)
        print("j={}".format(j)) 

            
             

            
            
except KeyboardInterrupt:
    print("\n[INFO] 데이터 수신 종료")

finally:
    ser.close
    # ser1.close  
    imu_log.close()
    print("적분된 값은{}이다.".format(delta_vlist))