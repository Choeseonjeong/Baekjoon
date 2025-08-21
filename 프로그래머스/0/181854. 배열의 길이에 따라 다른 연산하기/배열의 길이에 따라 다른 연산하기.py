def solution(arr, n):
    answer = []
    for idx, val in enumerate(arr):
        if len(arr)%2==1:
            if idx%2==0:
                arr[idx]+=n
        if len(arr)%2==0:
            if idx%2==1:
                arr[idx]+=n
    return arr