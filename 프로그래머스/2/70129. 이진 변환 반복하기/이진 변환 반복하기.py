def solution(s):
    answer = []
    zeroCnt = 0
    count = 0
    
    while s!='1':
        count+=1
        zeroCnt += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
    return [count,zeroCnt]