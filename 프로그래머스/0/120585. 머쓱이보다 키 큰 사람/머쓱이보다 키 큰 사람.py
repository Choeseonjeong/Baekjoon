def solution(array, height):
    answer = 0
    for n in array:
        if n > height:
            answer+=1
    return answer