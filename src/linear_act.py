#linear_act.py
import serial
import time
from imu_reader import open_serial

def main():
    ser=open_serial(port="COM6", baudrate=115200)
    ser.write(b'B\n')
    ser.write(b'f\n')
    time.sleep(0.2)
    ser.write(b'S\n')
    ser.write(b's\n')

def foward(ser):
    ser.write(b'F\n')

def backward(ser):
    ser.write(b'B\n')   

def stop(ser):
    ser.write(b'S\n')

def foward2(ser):
    ser.write(b'f\n')

def backward2(ser):
    ser.write(b'b\n')   

def stop2(ser):
    ser.write(b's\n')

def left_turn(ser):
    backward(ser)
    foward2(ser)

def right_turn(ser):
    foward(ser)
    backward2(ser)

def stopstop(ser):
    stop(ser)
    stop2(ser)



   

if __name__ == "__main__":
    main()    