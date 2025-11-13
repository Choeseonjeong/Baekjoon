import math
def solution(n1, d1, n2, d2):
    a,b = n1*d2+n2*d1, d1*d2
    gcd=math.gcd(a,b)
    a = a // gcd
    b = b // gcd
    return [a,b]