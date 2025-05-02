import sys

N = int(sys.stdin.readline())
arr = set(map(int,sys.stdin.readline().split()))
N = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))

for i in arr2:
    if i in arr:
        print(1)
    else:
        print(0)