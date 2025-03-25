def solution(arr, intervals):
    answer = []
    result = []
    for num in intervals:
        x,y = num
        answer.append(arr[x:y+1])
    for nums in answer:
        result+=nums
    return result