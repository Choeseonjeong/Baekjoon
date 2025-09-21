import math

def solution(arr):
    def lcm(a,b):
        return a*b // math.gcd(a,b)
    
    n = arr[0]
    for i in arr[1:]:
        n = lcm(n,i)
    return n