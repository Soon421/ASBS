#main.py, 현재 충격량적분부분까지 테스트 마침.
#모듈들로부터 import
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

close1(ser2)   #좌측후방
close2(ser2)   #우측후방
foward(ser2)
time.sleep(7)


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


        print(watcher)

        # 좌측
        # case1: 속도 충분할 때
        if len(delta_vlist) > 0 and delta_vlist[0]>=0.2:
            open1(ser2)
            backward(ser1)
            time.sleep(1)
            stop(ser1)          
                            
            if yaw > 45 or yaw<-45:
                backward(ser2)
                time.sleep(0.1)
                stop(ser2)
                close1(ser2)
                open2(ser2)
                foward(ser1)  
                time.sleep(1)
                stop(ser1)


               
        #case2: 속도 부족할 때
        elif len(delta_vlist) > 0 and delta_vlist[0]>0 and delta_vlist[0]<0.2:
            open1(ser2)
            backward(ser1)
            time.sleep(1)
            stop(ser1)

        
        #우측
        #case1: 속도 충분할 때
        # if len(delta_vlist) > 0 and delta_vlist[0]>=0.2:
        #     open2(ser2)
        #     backward(ser1)
        #     time.sleep(1)
        #     stop(ser1)          
                            
        #     if yaw > 45 or yaw<-45:
        #         backward(ser2)
        #         time.sleep(0.1)
        #         stop(ser2)
        #         close1(ser2)
        #         open2(ser2)
        #         foward(ser1)
        #         time.sleep(1)
        #         backward(ser1)


               
        # #case2: 속도 부족할 때
        # elif len(delta_vlist) > 0 and delta_vlist[0]>0 and delta_vlist[0]<0.2:
        #     open2(ser2)
        #     backward(ser1)
        #     time.sleep(1)
        #     stop(ser1)
            
         
                   
except KeyboardInterrupt:
    print("\n[INFO] 데이터 수신 종료")

finally:
    ser.close
    # ser1.close  
    imu_log.close()
    print("적분된 값은{}이다.".format(delta_vlist))
    print("yaw값은 {}".format(yaw))
 