import math

def solution(n):
    num = math.sqrt(n)
    if num == int(num):
        return (num+1)**2
    else:
        return -1
