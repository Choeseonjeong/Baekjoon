from collections import Counter
def solution(k, tangerine):
    shop = Counter(tangerine)
    count = 0
    shop = sorted(shop.items(),key=lambda x: x[1],reverse=True)
    for key,val in shop:
        count+=1
        k -= val
        if k<=0:
            break
            
    return count
            