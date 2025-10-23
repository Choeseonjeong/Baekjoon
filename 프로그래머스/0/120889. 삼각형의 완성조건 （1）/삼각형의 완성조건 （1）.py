def solution(sides):
    arr = sorted(sides)
    if arr[0]+arr[1] > arr[2]:
        return 1
    return 2