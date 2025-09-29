def solution(order):
    num = [3,6,9]
    answer = sum([1 for i in str(order) if int(i) in num])
    return answer