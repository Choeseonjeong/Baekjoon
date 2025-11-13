def solution(array, n):
    min_diff = min(abs(x-n) for x in array)
    candidates = [x for x in array if abs(x-n) == min_diff]
    return min(candidates)
