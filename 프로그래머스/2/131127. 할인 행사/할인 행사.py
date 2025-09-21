from collections import Counter

def solution(want, number, discount):
    shop = {}
    for w,n in zip(want,number):
        shop[w] = n
    cnt = 0
    
    for i in range(len(discount)-9):
        days = discount[i:i+10]
        if Counter(shop)==Counter(days):
            cnt+=1
    return cnt