def solution(arr):
    answer = []
    f, b = 0, len(arr)-1
    while f < b:
        if arr[f] != 2:
            f += 1
        if arr[b] != 2:
            b -= 1
        if arr[f] == 2 and arr[b] == 2:
            return arr[f:b+1]
    return [-1]