import sys

n,m = map(int,input().split())
N = {}
M = []
for i in range(n):
    a = input()
    N[a] = 0

for i in range(m):
    a = input()
    M.append(a)
result = 0
for i in M:
    if i in N:
        result+=1
print(result)
        