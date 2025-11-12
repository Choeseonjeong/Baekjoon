def solution(array):
    answer = 0
    for num in array:
        answer += str(num).count(str(7))
    return answer