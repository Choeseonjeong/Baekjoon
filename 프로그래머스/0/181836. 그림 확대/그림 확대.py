def solution(picture, k):
    answer = []
    for line in picture:
        result = ''
        for pixel in line:
            result+=pixel*k
        for _ in range(k):       
            answer.append(result)
        
    return answer