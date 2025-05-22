#linear_act.py
import serial
import time
from imu_reader import open_serial

def main():
    ser=open_serial(port="COM6", baudrate=9600)
    ser.write(b'F\n')
    time.sleep(3)
    ser.write(b'B\n')
    time.sleep(3)
    ser.write(b'S\n')

def foward2(ser2):
    ser2.write(b'F\n')

def backward2(ser2):
    ser2.write(b'B\n')   

def stop2(ser2):
    ser2.write(b'S\n')

if __name__ == "__main__":
    main()    