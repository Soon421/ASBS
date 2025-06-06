#integrate_by_sd.py
import numpy as np
import time


def integ(log_data, time_data):
    calculed_value =np.trapezoid( log_data, time_data )
    
    
    return calculed_value

    
def integral__by_SD(j,z,values,integrate_log, timestamp, integrate_time, delta_vlist):
    integ_result=0
    if j==1:                                                           #여기가 이상함 z 는 원래 가속도의 증가 감소 변화 횟수를 위한 변수였음
        integrate_log.append(values[0])
        integrate_time.append(timestamp)

    if z % 2 == 0 and z != 0: 
        integ_result = integ(integrate_log, integrate_time)
        delta_v=float(integ_result)
        delta_vlist.append(delta_v)   
        integrate_log.clear()             #다음 적분을 위해 적분에 이용한 리스트 초기화
        integrate_time.clear()
        z=0                               #z값을 0으로 초기화해서 적분계산과 리스트 비우는과정이 반복되지 않도록함.
                                          # 이거 자꾸 잔 적분까지 되는거 그냥 막아버릴라고 이렇게 한거인거지?

    return integ_result, z