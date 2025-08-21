def solution(order):
    answer = 0
    for word in order:
        if "americano" in word:
            answer+=4500
        elif "cafelatte" in word:
            answer+=5000
        elif "anything" in word:
            answer+=4500
            
    return answer