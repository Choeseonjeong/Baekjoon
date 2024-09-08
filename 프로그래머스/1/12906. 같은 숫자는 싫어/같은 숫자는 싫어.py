def solution(arr):
    a = []
    for i in range(0, len(arr)-1):
        if arr[i] != arr[i+1]:
            a.append(arr[i])
    a.append(arr[-1])  
    return a
