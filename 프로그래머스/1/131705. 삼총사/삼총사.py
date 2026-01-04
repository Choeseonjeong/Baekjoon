import itertools 
def solution(number):
    arr = []
    for i in itertools.combinations(number,3):
        num = sum(i)
        arr.append(num)
    return arr.count(0)
        