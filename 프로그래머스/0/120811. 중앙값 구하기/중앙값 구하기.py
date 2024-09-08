def solution(array):
    mid = int(len(array) / 2)
    array.sort()
    return array[mid]
