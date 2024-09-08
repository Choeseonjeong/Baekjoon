def solution(price, money, count):
    num=0
    for i in range(1,count+1):
        num+=i*price
    if money>num:
        return 0
    else:
        return num-money