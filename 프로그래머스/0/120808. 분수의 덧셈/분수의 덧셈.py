import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    up = numer1*denom2 + numer2*denom1
    down = denom1*denom2
    gcd = math.gcd(up,down)
    return [up/gcd,down/gcd]