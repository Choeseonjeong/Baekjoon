import math

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def lcm(n, m):
    return n * m // math.gcd(n, m)
        
for i in arr:
    n,m = i
    print(lcm(n,m))