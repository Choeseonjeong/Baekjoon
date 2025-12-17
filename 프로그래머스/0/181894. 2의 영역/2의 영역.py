def solution(arr):
    front, end = 0, len(arr) - 1

    while front <= end and arr[front] != 2:
        front += 1

    while front <= end and arr[end] != 2:
        end -= 1

    if front > end:
        return [-1] 

    return arr[front:end+1]
