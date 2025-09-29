def solution(array):
    num = sorted(array)[-1]
    return [num,array.index(num)]