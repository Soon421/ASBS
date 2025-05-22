#sl_valve.py
import serial
import time
from imu_reader import open_serial

def main():
    ser=open_serial(port="COM6", baudrate=9600)
    ser.write(b'O\n')
    time.sleep(5)
    ser.write(b'C\n')

def open1(ser1):
    ser1.write(b'O1\n')

def close1(ser1):
    ser1.write(b'C1\n')    

def open2(ser1):
    ser1.write(b'O2\n')

def close2(ser1):
    ser1.write(b'C2\n')  

def open3(ser2):
    ser2.write(b'O3\n')

def close3(ser2):
    ser2.write(b'C3\n')  

def open4(ser2):
    ser2.write(b'O4\n')

def close4(ser2):
    ser2.write(b'C4\n')  


if __name__ == "__main__":
    main()
    
   
 



