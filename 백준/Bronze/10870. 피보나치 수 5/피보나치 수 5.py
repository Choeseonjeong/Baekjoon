import sys
input = sys.stdin.readline

N = int(input())
a,b = 0,1
for _ in range(N):
    a,b = b,a+b
print(a)