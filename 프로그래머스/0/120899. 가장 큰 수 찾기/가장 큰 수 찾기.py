
def solution(array):
    arrays = sorted(array)
    return arrays[-1], array.index(arrays[-1])
