import math

arr = [list(map(int,input().split())) for _ in range(2)]
down = arr[0][1] * arr[1][1]
up = arr[0][0]*arr[1][1] + arr[1][0]*arr[0][1]

g = math.gcd(int(up), int(down))
up //= g
down //= g

print(up ,down)