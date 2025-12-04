def solution(order):
    count = 0
    for num in str(order):
        if int(num) in [3,6,9]:
            count+=1
    return count