def solution(array):
    answer = 0
    for num in array:
        for n in str(num):
            if n == '7':
                answer+=1
    return answer