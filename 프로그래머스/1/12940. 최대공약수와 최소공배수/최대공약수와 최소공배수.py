import math

def solution(n, m):
    num = math.gcd(n,m)
    return [num, n // math.gcd(n, m) * m]