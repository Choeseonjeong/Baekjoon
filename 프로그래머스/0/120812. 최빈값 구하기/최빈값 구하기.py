def solution(array):
    arr = {}
    for n in array:
        if n in arr:
            arr[n] += 1
        else:
            arr[n] = 1
    maxnum = max(arr.values())
    result = [k for k, v in arr.items() if v == maxnum]
    if len(result) > 1:
        return -1
    else:
        return result[0]