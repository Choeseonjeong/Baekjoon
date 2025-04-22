import sys
n = int(input())
arr = [int(sys.stdin.readline()) for i in range(n)]
arr.sort()
for i in arr:
    print(i)