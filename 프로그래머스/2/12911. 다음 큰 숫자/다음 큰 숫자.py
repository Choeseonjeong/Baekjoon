def solution(n):
    answer = n+1
    while True:
        a = bin(n)[2:]
        b = bin(answer)[2:]
        if a.count('1') == b.count('1'):
            return answer
        else:
            answer+=1