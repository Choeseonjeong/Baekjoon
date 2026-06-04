def solution(arr):
    answer = []
    num = min(sorted(arr))
    if len(arr)<=1:
        return [-1]
    return [i for i in arr if i!= num]