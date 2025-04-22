import math

a,b = map(int,input().split())
result = a*b // math.gcd(a,b)

print(result)