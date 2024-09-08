def solution(lottos, win_nums):
    cntUp = 0 # 최소 # 0제외한 값 
    cntDown = 0 # 최대 # 0 더한 값 # 항상 cntDown이 더 큼 
    num = [6,5,4,3,2,1]
    for i in lottos:
        if i in win_nums:
            cntUp+=1
            
    cntDown = lottos.count(0) +  cntUp
    if cntDown > 0:
        if lottos.count(0)==6:
            return [1,6]
        else:
            return num[cntDown-1],num[cntUp-1]
    else:
        return [6,6]