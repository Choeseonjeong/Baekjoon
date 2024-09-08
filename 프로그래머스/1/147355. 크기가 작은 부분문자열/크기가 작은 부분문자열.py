def solution(t, p):
    arr=[]
    result=0
    for i in range(0,len(t)-len(p)+1):
        arr.append(t[i:i+len(p)])
    for i in arr:
        if i<=p:
            result+=1
    return result