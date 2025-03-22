def solution(price, money, count):
    num = 0
    for i in range(1,count+1):
        num += price*i
    if money < num:
        return num-money
    else:
        return 0