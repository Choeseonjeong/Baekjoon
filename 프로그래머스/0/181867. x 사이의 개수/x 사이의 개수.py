def solution(arr):
    answer=arr.split("x")
    result = []
    for i in answer:
        result.append(len(i))
    return result