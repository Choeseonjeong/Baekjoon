def solution(arr, k):
    num = [-1] * k
    ar = []
    for i in arr:
        if i not in ar:
            ar.append(i)
    
    for i in range(min(k,len(ar))):
        num[i] = ar[i]
    return num