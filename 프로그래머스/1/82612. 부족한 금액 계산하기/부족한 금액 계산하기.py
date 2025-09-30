def solution(price, money, count):
    answer = 0
    while answer < count:
        answer += 1
        money -= price*answer
    return abs(money) if money < 0 else 0