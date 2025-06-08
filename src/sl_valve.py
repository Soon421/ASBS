#sl_valve.py
import serial
import time
from imu_reader import open_serial

def main():
    ser=open_serial(port="COM6", baudrate=9600)
    ser.write(b'O\n')
    time.sleep(5)
    ser.write(b'C\n')

def open_l(ser):
    ser.write(b'O1\n')

def close_l(ser):
    ser.write(b'C1\n')    

def open_r(ser):
    ser.write(b'O2\n')

def close_r(ser):
    ser.write(b'C2\n')  
 


if __name__ == "__main__":
    main()
    
   
 



