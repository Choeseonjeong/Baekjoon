def solution(price, money, count):
    answer = sum([i*price for i in range(1,count+1)])
    return answer-money if answer > money else 0