#yaw_estimator.py
import time
import csv
from integrate_by_sd import integ
from imu_reader import open_serial, read_serial_line

def main():
    ser = open_serial(port="COM8", baudrate=9600)
    
    
    gyroZlist = []      #여기서 gyroZ값만 모으는 리스트 생성
    try:
        for timestamp, values in read_serial_line(ser): 
            if len(values) < 6: continue         # 값이 온전히 안들어오는경우도 진행되도록

            t    = float(timestamp)              #정수화
            gyroZ =float(values[5])
            
            
            gyroZlist.append(gyroZ)              #append 메소드 이용해서 gyroZ값을 리스트에 계속 추가
            yaw = integ(gyroZlist)
            print("{0} estimated yaw: {1}".format(t, yaw))

    except KeyboardInterrupt:
        print("\n[INFO] 데이터 수신 종료")

    finally:
        ser.close()
 
      
def yaw_estimator(ser):
    
    
    gyroZlist = []      #여기서 gyroZ값만 모으는 리스트 생성
    tlist=[]

    for timestamp, values in read_serial_line(ser): 
        if len(values) < 6: continue         # 값이 온전히 안들어오는경우도 진행되도록

        t    = float(timestamp)              # 유리화
        gyroZ =float(values[5])
        
        
        gyroZlist.append(gyroZ)              #append 메소드 이용해서 gyroZ값을 리스트에 계속 추가
        tlist.append(t)
        yaw = integ(gyroZlist,tlist)


        yield yaw, timestamp, values





    


if __name__ == "__main__":
    main()        

