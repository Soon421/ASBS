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

def foward(ser1):
    ser1.write(b'F\n')

def backward(ser1):
    ser1.write(b'B\n')   

def stop(ser1):
    ser1.write(b'S\n')

if __name__ == "__main__":
    main()    