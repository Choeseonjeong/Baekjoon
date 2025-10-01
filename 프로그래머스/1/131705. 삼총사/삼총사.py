from itertools import combinations

def solution(number):
    count = 0
    for arr in combinations(number,3):
        if sum(arr)==0:
            count += 1
    return count