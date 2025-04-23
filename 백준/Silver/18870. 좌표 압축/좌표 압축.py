n = int(input())
arr=list(map(int,input().split()))
answer = sorted(list(set(arr)))
dic=dict()
for i in range(len(answer)):
    dic[answer[i]]=i
print(' '.join(str(dic[i])for i in arr))