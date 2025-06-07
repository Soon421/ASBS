#watcher.py
def func_watcher(values,watcher,j,z):
    
    watcher_1= list(watcher)                         # 한 루프 전의 watcher를 설정
    for k in [3,2,1,0]:
        watcher[k+1] = watcher[k]                        # watcher 안에 값들을 한칸씩 옆으로 옮김
        
    watcher[0] = values[0]                       # 한 칸씩 밀었으니까 첫번째 칸에 새로 받은 값 채움


    if  watcher[0] - watcher_1[0]  >= 0.07 and watcher[0]>0.15:           
        jj=1
    elif watcher[0]<0:        
        jj=0
    else:
        jj=j
        

        
    if j != jj:
        z+=1
    
    return z,watcher_1,jj,watcher
    


     
#jj 는 이 지역변수로서 갑작스런 가속도 변화가 나타났는지에 대한 값이지만 이 놈은 메인 코드에서 j 라는 값으로 들어갈 거임
