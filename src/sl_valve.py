#sl_valve.py
import serial
import time
from imu_reader import open_serial

def main():
    ser=open_serial(port="COM6", baudrate=9600)
    ser.write(b'O\n')
    time.sleep(5)
    ser.write(b'C\n')

def open(ser1):
    ser1.write(b'O\n')

def close(ser1):
    ser1.write(b'C\n')    


if __name__ == "__main__":
    main()
    
   
 



