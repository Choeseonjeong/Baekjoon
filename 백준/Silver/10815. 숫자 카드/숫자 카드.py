import sys

N = int(sys.stdin.readline())
arr1 = set(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

dic = dict()

for i in arr1:
    dic[i] = 0
    
arr2 = list(map(int,sys.stdin.readline().split()))

for i in arr2:
    if i in dic:
        print(1,end=' ')
    else:
        print(0,end=' ')