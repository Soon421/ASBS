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

def foward(ser):
    ser.write(b'F\n')

def backward(ser):
    ser.write(b'B\n')   

def stop(ser):
    ser.write(b'S\n')




if __name__ == "__main__":
    main()    