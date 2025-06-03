#integrate_by_sd.py
import numpy as np
import time


def integ(log_data, time_data):
    calculed_value =np.trapezoid( log_data, time_data )
    
    
    return calculed_value

    
def integral__by_SD(j,z,values,integrate_log, timestamp, integrate_time):
    integ_result=0
    if j==1:                                                           
        integrate_log.append(values[0])
        integrate_time.append(timestamp)

    if z % 2 == 0 and z != 0: 
        integ_result = integ(integrate_log, integrate_time)    
    

    integrate_log.clear()             #다음 적분을 위해 적분에 이용한 리스트 초기화
    integrate_time.clear()
    
    return integ_result