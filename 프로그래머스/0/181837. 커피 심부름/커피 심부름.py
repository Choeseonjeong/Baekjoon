def solution(order):
    a = ["iceamericano", "americanoice","hotamericano", "americanohot","americano","anything"]
    b = ["icecafelatte", "cafelatteice","hotcafelatte", "cafelattehot","cafelatte"]
    answer = 0
    for word in order:
        if word in a:
            answer += 4500
        else:
            answer += 5000
    return answer