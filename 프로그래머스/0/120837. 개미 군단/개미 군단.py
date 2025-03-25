def solution(hp):  
    cnt = 0
    cnt+=int(hp//5)
    hp = hp%5
    cnt+=int(hp//3)
    hp = hp%3
    cnt+=int(hp//1)
    hp = hp%1
    return cnt
# 5
# 3
# 1