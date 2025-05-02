import sys

n = int(sys.stdin.readline())
result= {}
for i in range(n):
    log = list(input().split()) 
    
    if log[1] == "enter":
        result[log[0]]=1
    else:
        del result[log[0]]

temp = sorted(result.keys(),reverse=True)
for i in temp:
    print(i)