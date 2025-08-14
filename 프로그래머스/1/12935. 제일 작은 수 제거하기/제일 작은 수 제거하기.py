def solution(arr):
    answer = []
    num = arr.index(min(arr))
    arr.pop(num)
    return arr if arr else [-1]