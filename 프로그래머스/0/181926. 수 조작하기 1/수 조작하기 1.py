def solution(n, control):
    answer = n
    word = {"w":1,"s":-1,"d":10,"a":-10}
    for text in control:
        answer += word[text]
    return answer