import sys

n = sys.stdin.readline()
arr1 = list(map(int,input().split()))
n = sys.stdin.readline()
arr2 = list(map(int,input().split()))
dic = {}
for i in arr2:
    dic[i]=0
    
for i in arr1:
    if i in dic:
        dic[i]=1
        
    
for i in dic:
    print(dic[i], end=' ')