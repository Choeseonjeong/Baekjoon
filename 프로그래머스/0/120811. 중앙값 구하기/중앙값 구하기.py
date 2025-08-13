def solution(array):
    answer = int(len(array)//2)
    array.sort()
    return array[answer]