def solution(picture, k):
    answer = []
    for word in picture:
        ch = ''
        for text in word:
            ch+=text*k
        for _ in range(k):
            answer.append(ch)
    return answer